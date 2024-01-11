"""
telegram_blaster.py

telegram_blaster connects to an instance of the EK80 application using
the REST interface and creates bottom depth and echogram subscriptions for
the channels defined in the telegram_blaster.yml config file. It then 
broadcasts EK500 Q Telegrams derived from these data on the network.

This can be used to send data to Echolog500 for "liveview" applications
where Echolog80 does not work well.

Note: If this application crashes or if execution is halted, any endpoints
it has created will remain on the EK80 server. The application is not
sophisticated enough at this time to 


"""

import struct
import logging
import collections
import yaml
import urllib3
from PyQt5 import QtCore, QtNetwork
import ek80_rest_client


class telegram_blaster(QtCore.QObject):

    stopClient = QtCore.pyqtSignal()

    #  specify the delay, in seconds, between when the application connects
    #  and when it tries to create subscriptions. If telegram_blaster is
    #  already running when you start EK80, it can request the list of channels
    #  before the EK80 application has fully initialized resulting in an
    #  empty channel list. 
    CONNECT_DELAY = 10
    
    #  specify the number of datagrams to send before disconnecting in test mode
    TEST_DATAGRAMS_LIMIT = 10

    def __init__(self, config_file, clean_server=False, test_run=False, parent=None):
        #  initialize the superclass
        super(telegram_blaster, self).__init__(parent)

        #  store our command line args
        self.config_file = config_file
        self.clean_server = clean_server
        self.test_run = test_run

        #  define some initial properties
        self.udp_socket = None
        self.just_connected = False
        self.n_test_datagrams = 0

        #  create a timer for polling the server
        self.param_timer = QtCore.QTimer(self)
        self.param_timer.timeout.connect(self.poll_parameters)

        #  create a timer for reestablishing a lost connection.
        self.retry_timer = QtCore.QTimer(self)
        self.retry_timer.timeout.connect(self.reestablish_connection)
        self.retry_timer.setSingleShot(True)

        #  start things up after we get the event loop running by using a timer
        QtCore.QTimer.singleShot(0, self.start_app)


    def start_app(self):

        #  bump the cursor
        print()

        #  read the configuration file
        with open(self.config_file, 'r') as cf_file:
            try:
                self.configuration = yaml.safe_load(cf_file)
            except yaml.YAMLError as exc:
                print('Error reading configuration file ' + self.config_file)
                print('  Error string:' + str(exc))
                print('  Exiting...')
                QtCore.QCoreApplication.instance().quit()
                return

        #  create a logger to log to the console
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(self.configuration['application']['log_level'])
        formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(module)s - %(message)s')
        consoleLogger = logging.StreamHandler(sys.stdout)
        consoleLogger.setFormatter(formatter)
        self.logger.addHandler(consoleLogger)
        self.logger.info("Starting telegram_blaster...")

        #  create the local UDP port we'll use to transmit datagrams
        host_address = QtNetwork.QHostAddress(self.configuration['application']['local_udp_ip'])
        port = int(self.configuration['application']['local_udp_port'])

        self.logger.info("Opening telegram server on interface %s port %i",
                            host_address.toString(), port)
        self.udp_socket = QtNetwork.QUdpSocket()
        self.udp_socket.bind(host_address, port)

        #  build a dict containing IP and port info for our clients
        self.logger.info("Building client list...")
        self.clients = {}
        client_ips = self.configuration['clients']['client_ips']
        client_ports = self.configuration['clients']['client_ports']
        if len(client_ips) != len(client_ports):
            if len(client_ports) == 1 and len(client_ips) > 1:
                #  only one port is provided and so we assume we're using
                #  that port for all IPs
                client_ports = [client_ports[0]] * len(client_ips)
            else:
                #  don't know what to do. Both not enough and too many
                #  ports defined. There should either be an n:1 or 1:1
                #  ratio of ports to addresses
                self.logger.critical("Client IP and port mismatch. Check the clients " +
                        " section of the YML configuration file.")
                QtCore.QCoreApplication.instance().quit()
                return

        #  now create a dict keyed by a string comprised of the IP and port
        #  of the client whose elements are a dict containing the Qt host
        #  address
        for i in range(len(client_ips)):
            host_address = QtNetwork.QHostAddress(client_ips[i])
            port = int(client_ports[i])
            client_id = host_address.toString() + ':' + str(port)
            self.clients[client_id] = {'host_address':host_address, 'port':port}

        #  set the connection retry timer interval
        self.retry_timer_interval = self.configuration['application']['lost_server_retry_interval_ms']
        
        #  lastly, set the polling timer interval and start it
        self.param_timer.setInterval(self.configuration['application']['polled_param_interval_ms'])

        #  create an instance of the client and connect some signals
        self.logger.debug("Connecting to EK80 server at %s." %
                self.configuration['application']['ek80_server_ip'])
        self.client = ek80_rest_client.ek80_rest_client(server_address=
                self.configuration['application']['ek80_server_ip'])
        self.client.subscriptionData.connect(self.subscription_data_available)
        self.client.cleanupComplete.connect(self.client_stopped)
        self.stopClient.connect(self.client.cleanup_client)

        #  check if we need to wipe all of the subscriptions (and endpoints)
        #  from the server. This is sometimes needed while developing client
        #  apps after they crash and leave their bits around on the server.
        if self.clean_server:
            self.logger.debug("Removing and cleaning up all connections on the server. (-c==True)")
            try:
                self.client.cleanup_server()
            except:
                self.logger.debug("Error cleaning up server?!?")
                pass

        #  create our subscriptions
        try:
            self.create_subscritions()
        except urllib3.exceptions.MaxRetryError:
            #  we couldn't connect to the server so start retrying
            self.retry_timer.start()
            return
        except Exception as e:
            #  some other issue, raise it
            raise(e)

        #  we're "connected" so start polling parameters
        self.param_timer.start()


    def create_subscritions(self):

        #  get the list of channels
        self.logger.info("Getting channel information from EK80 server...")
        self.channels = self.client.get_channels()
        chan_string = ', '.join(self.channels)
        self.logger.info("Channels found: %s", chan_string)

        #  initialize some attributes that help us track and store subscription data
        self.bottom_sub_ids = []
        self.surface_echogram_sub_ids = []
        self.bottom_echogram_sub_ids = []
        self.channel_id_map = {}
        self.last_vl_ping = -1
        self.last_q_channel_number = 0

        #  Q telegrams contain data from both the surface and bottom echogram subscriptions.
        #  Since these data are received in separate callback calls, we need to buffer the
        #  data for each ping so we can send it after we receive both the surface and bottom
        #  data. Create a dict well key by channel ID that we can use to do this.
        self.q_data_buffer = {}

        #  create subscriptions to receive data required to send our EK500 telegrams
        #  of choice. Currently that is VL, D, B, and Q telegrams so we subscribe to
        #  surface and bottom echograms and bottom detections for our channels of interest
        if len(self.channels) > 0:
            for channel in self.channels:

                #  process the channel config data to determine if we're adding
                #  this channel and return the config parameters.
                add_channel, channel_config = self.get_channel_configuration(channel)

                if add_channel:
                    #  this channel has either an explicit entry or a "default"
                    #  entry exists and will be used.
                    self.logger.info("Adding channel %s ", channel)

                    #  Create a mapping of channel ID to telegram number
                    if 'q_telegram_channel' in channel_config:
                        self.channel_id_map[channel] = channel_config['q_telegram_channel']
                        self.last_q_channel_number = channel_config['q_telegram_channel']
                    else:
                        #  the channel number isn't defined, make one up
                        this_q_channel_number = self.last_q_channel_number + 1
                        self.channel_id_map[channel] = this_q_channel_number
                        self.last_q_channel_number = this_q_channel_number

                    #  initialize the Q datagram buffer for this channel - we'll use ping
                    #  number to determine if we've rx'd data from both subscriptions
                    self.q_data_buffer[channel] = {'surface_ping_number':-1, 'surface_data':[],
                            'bottom_ping_number':-1, 'bottom_data':[]}

                    #  add the bottom detection subscription
                    bottom_detect_sub = self.client.create_bottom_detection_subscription(channel,
                            upper_detector_limit=channel_config['upper_detector_limit'],
                            lower_detector_limit=channel_config['lower_detector_limit'],
                            bottom_back_step=channel_config['bottom_back_step'])
                    self.bottom_sub_ids.append(bottom_detect_sub)

                    #  add the surface echogram subscription
                    surface_echogram_sub = self.client.create_echogram_subscription(channel,
                            pixel_count=channel_config['surface_echogram_count'],
                            range=channel_config['surface_echogram_range'],
                            range_start=channel_config['surface_echogram_start'],
                            ek500_db_format=True)
                    self.surface_echogram_sub_ids.append(surface_echogram_sub)

                    #  add the bottom echogram subscription
                    bottom_echogram_sub = self.client.create_echogram_subscription(channel,
                            pixel_count=channel_config['bottom_echogram_count'],
                            range=channel_config['bottom_echogram_range'],
                            range_start=channel_config['bottom_echogram_start'],
                            echogram_type='bottom', ek500_db_format=True)
                    self.bottom_echogram_sub_ids.append(bottom_echogram_sub)

                else:
                    #  we're not adding this channel
                    self.logger.info("Channel %s not found in config file. Skipping.",
                            channel)

        else:
            #  no channels?
            self.logger.error("No channels found! What are we doing here???")


    @QtCore.pyqtSlot()
    def poll_parameters(self):
        '''
        poll_parameters is called by a timer to poll the server for data
        that isn't available via subscription.

        poll_parameters is also used as a heartbeat check for the EK80 server.
        If we lose the connection to the server, the requests here will fail.

        '''

        try:

            #  get the navigation data - this can be used to generate a GL datagram
            nav_data = self.client.get_navigation()

            #  there seems to be a bug in the EK80 REST API where the time (and VL) are
            #  returned as 0. Until that is fixed, we'll get time from the motion data.
            motion_data = self.client.get_motion()
            gl_time = self.get_header_time(motion_data.time)

            #  if we have valid GPS data, send the GL datagram
            if (not nav_data.has_timed_out and
                    nav_data.position.input_status.lower() == 'ok'):
                #  get the GL datagram as an array of bytes
                gl_bytes = self.get_gl_telegram(nav_data.position.latitude,
                        nav_data.position.longitude, gl_time)

                #  and then send the datagram
                self.send_telegram(gl_bytes)
                
                
            #  THIS BLOCK SHOULD BE USED IN CONJUNCTION WITH A CHECK AGAINST
            #  A LIST OF SUBSCRIBED CHANNELS TO DETERMINE IF A NEW CHANNEL HAS
            #  BEEN ADDED OR ONE HAS BEEN REMOVED. ADDITIONAL CODE WILL NEED TO BE
            #  ADDED TO PERFORM THE COMPARISON AND ADD OR REMOVE SPECIFIC CHANNELS.
            #  THE CURRENT DESIGN ADDS ALL CHANNELS AT ONCE IN CREATE_SUBSCRIPTIONS
            #  AND THIS WILL NEED TO BE CHANGED TO ADD ONE SUBSCRIPTION AT A TIME
            #  wILL ALSO NEED TO ADD A METHOD TO REMOVE A SPECIFIC SUBSCRIPTION.
#            #  
#            if len(self.channels) == 0:
#                print("NOONAN!")
#                self.channels = self.client.get_channels()
#            else:
#                print("GotChans!")
                
        except urllib3.exceptions.NewConnectionError:
            print("CON ERROR")

        except urllib3.exceptions.MaxRetryError:
            #  we've lost connection - stop polling and start trying to reconnect
            self.param_timer.stop()
            self.logger.error("Lost connection to EK80 server at %s" %
                    (self.configuration['application']['ek80_server_ip']))
            self.logger.info("Attempting to reconnect to EK80 server at %s" %
                    (self.configuration['application']['ek80_server_ip']))

            self.reestablish_connection()


    @QtCore.pyqtSlot()
    def reestablish_connection(self):
        '''
        reestablish_connection is called by the retry_timer to periodically
        try to connect to the EK80 application after the connection is lost.
        This allows telegram_blaster to automatically reconnect after the
        EK80 has been restarted.
        '''

        #  check if we just connected, or if we're still trying to connect
        if not self.just_connected:

            self.logger.info("Trying to (re)connect to EK80 server")

            #  try to get the navigation data. This call will succeed if the
            #  EK80 server is available.
            try:
                _ = self.client.get_navigation()

            except Exception:
                #  server is not available, we'll delay a bit and try again
                self.retry_timer.start(self.retry_timer_interval)
                return

            #  the get_navigation call succeeded so the server is available. We
            #  will clean up all connections to ensure that we can connect without
            #  issue. This is brute force and will break the connections of other
            #  REST clients so this will need to be rethought if we're running
            #  multiple REST clients.
            self.logger.info("Connected. Cleaning up old subscriptions...")
            self.client.cleanup_client(quiet=True)
            
            #  wait a bit to ensure that the EK80 application is fully initialized
            self.just_connected = True
            self.logger.info("Waiting " + str(self.CONNECT_DELAY) + 
                    " seconds to allow EK80 application to fully initialize...")
            self.retry_timer.start(self.CONNECT_DELAY * 1000)

        else:
            #  we've just finished our delay between connection and querying channels
            #  set just_connected to False, create our subscriptions, and kick off the
            #  param timer.
            self.just_connected = False
            
            self.logger.info("Creating new subscriptions...")
            self.create_subscritions()

            #  start the param timer to get the polled data
            self.param_timer.start()
            

    def stop_app(self):

        #  stop all timers
        self.param_timer.stop()
        self.retry_timer.stop()

        self.logger.debug("Cleaning up the client...")
        try:
            self.stopClient.emit()
        except:
            pass


    def client_stopped(self):

        self.logger.debug("Client cleanup complete.")

        if self.udp_socket:
            self.udp_socket.close()

        self.logger.info("Application exiting...")
        QtCore.QCoreApplication.instance().quit()
        return


    def get_header_date(self,  datetime_val):

        #get year, month, day zero padded (i.e day 6 = 06) as a string YYMMDD
        header_date = datetime_val.strftime("%y%m%d")

        return header_date


    def get_header_time(self,  datetime_val):
        '''
        get_header_time returns the time as a string ub EK500 telegram format.
        For example: datetime object: datetime.datetime(2022, 7, 9, 10, 58, 1, 734927)
                     returned string: '10580173'

        '''
        #  get time as string HHMMSSmm. Since strftime %f always returns microseconds
        #  padded to 6 places, we can simply drop the last four chars to return a time
        #  close enough for what we're doing.
        header_time = datetime_val.strftime("%H%M%S%f")[:-4]
        return header_time


    def get_gl_telegram(self,  lat,  lon,  postion_time):
        '''
        get_gl_telegram returns a byte array containing an EK500 GL telegram
        containing the provided lat, lon, and time. The GL telegram string is
        in the form LLMM.MMMM,N,LLLMM.MMMM,W
        '''

        #  split the position strings
        lat_split = str.split(str(lat), '.')
        lon_split = str.split(str(abs(lon)), '.')

        #  get the degrees
        lat_deg = lat_split[0].zfill(2)
        lon_deg = lon_split[0].zfill(3)

        #  convert the rest to decimal minutes (MM.MMMM)
        #  zero pad result to ensure decimal minute string is 7 chars long
        lat_mm = '%07.4f' % (float('.' + lat_split[1]) * 60)
        lon_mm = '%07.4f' % (float('.' + lon_split[1]) * 60)

        #  and assign W/N as needed
        lat_loc = 'N' if lat >= 0 else 'S'
        lon_loc = 'E' if lon >= 0 else 'W'

        #combine as a string
        pos_str = (lat_deg + lat_mm + ',' + lat_loc +
                ',' + lon_deg + lon_mm + ',' + lon_loc)

        #pack the data as a byte array and return
        gl_bytes = bytes(('GL,'+postion_time+','+pos_str), 'utf-8')
        return gl_bytes


    @QtCore.pyqtSlot(object, str, dict)
    def subscription_data_available(self, clientObj, data_type, data):

        if data_type == 'bottom detection':

            #  you should have enough data from the bottom detection
            #  subscription to create both a B and VL datagram so you
            #  would do that here

            #get your header row
            header_date = self.get_header_date(data['pingTime'])
            header_time = self.get_header_time(data['pingTime'])

            #  check if we should emit a VL telegram - we do this only once per ping
            if self.last_vl_ping != data['pingNumber'] and 'vesselLogDistance' in data:
                #  this is a new ping - send VL
                header_bytes = bytes(('VL,' +header_time+ ','+header_date+', '), 'utf-8')
                dist_bytes = struct.pack('f', data['vesselLogDistance'])
                dist_datagram_bytes = header_bytes + dist_bytes
                self.send_telegram(dist_datagram_bytes)
                self.last_vl_ping = data['pingNumber']

        elif data_type == 'echogram':

            #  This is echogram subscription data. Since each channel has two echogram subscriptions
            #  (bottom and surface) and we need to build Q telegrams using data from both, we have
            #  to determine which subscription this is, buffer the data, and if we have both the
            #  the surface and bottom data for this channel we then need to transmit the Q telegram.

            #  first determine if this is a bottom or surface subscription
            if data['subscriptionId'] in self.surface_echogram_sub_ids:
                #  this is a surface subscription - buffer the data
                self.q_data_buffer[data['dataSource']]['surface_ping_number'] = data['pingNumber']
                self.q_data_buffer[data['dataSource']]['surface_data'] = data['data']
            elif data['subscriptionId'] in self.bottom_echogram_sub_ids:
                #  this is a bottom subscription - buffer the data
                self.q_data_buffer[data['dataSource']]['bottom_ping_number'] = data['pingNumber']
                self.q_data_buffer[data['dataSource']]['bottom_data'] = data['data']

            #  compare the ping numbers of the buffered data to determine if we've rx'd both for this ping
            if (self.q_data_buffer[data['dataSource']]['bottom_ping_number'] ==
                    self.q_data_buffer[data['dataSource']]['surface_ping_number']):

                #  we have rx'd data from both surface and bottom subs. Create the Q telegram
                channel_name_bytes = bytes('Q' + str(self.channel_id_map[data['dataSource']]),  'utf-8')

                # get the time properly formatted
                header_time_bytes = bytes(self.get_header_time(data['pingTime']),  'utf-8')

                #  TVG type- for now, set as '20logR' as required by Echoview; this corresponds to '0' according to EK500 documentation
                tvg_type_bytes = struct.pack('l', 0)

                #  get bottom depth, layer parameters packaged up as required
                bottom_depth_bytes = struct.pack('f', data['bottomDepth'])
                surface_upper_bytes = struct.pack('f', self.configuration['channels'][data['dataSource']]['surface_echogram_start'])
                #  surface echogram lower bound = surface echogram start + range
                surface_echogram_lower = self.configuration['channels'][data['dataSource']]['surface_echogram_start'] +self.configuration['channels'][data['dataSource']]['surface_echogram_range']
                surface_lower_bytes = struct.pack('f', surface_echogram_lower)
                surface_count = struct.pack('l', self.configuration['channels'][data['dataSource']]['surface_echogram_count'])

                #for bottom echograms - lower = bottom_echogram_start
                bottom_echogram_upper = data['bottomDepth'] + self.configuration['channels'][data['dataSource']]['bottom_echogram_start']
                bottom_echogram_lower = bottom_echogram_upper + self.configuration['channels'][data['dataSource']]['bottom_echogram_range']
                bottom_lower_bytes = struct.pack('f', bottom_echogram_lower)
                bottom_upper_bytes = struct.pack('f', bottom_echogram_upper)
                bottom_count = struct.pack('l', self.configuration['channels'][data['dataSource']]['bottom_echogram_count'])


                #finally, pack the Echogram data up
                data_bytes = (self.q_data_buffer[data['dataSource']]['surface_data'].tobytes() +
                        self.q_data_buffer[data['dataSource']]['bottom_data'].tobytes())

                #also get a 1-space separator char (",")
                sep = bytes(',',  'utf-8')

                #add it all together for a telegram- this follows EK500 format but there are no separators after TVG type- seems like there should
                #be something?
                telegram_bytes = (channel_name_bytes + sep + header_time_bytes + sep +
                        tvg_type_bytes + bottom_depth_bytes  + surface_upper_bytes +
                        surface_lower_bytes + surface_count + bottom_upper_bytes +
                        bottom_lower_bytes + bottom_count + data_bytes)

                #  and then send the datagram
                self.send_telegram(telegram_bytes)

        else:
            print('type: ', data_type)
            print(data)


    def send_telegram(self, telegram_bytes):
        '''
        send_telegram sends a telegram packed as a byte array to
        the configured clients.

        Args:
            telegram_bytes (bytearr):
                The the EK500 telegram you are sending packed into
                a byte array

        Returns:
            A dict keyed by client IP:port that contains the number of
            bytes sent to each client. You can compare this to the length
            of your telegram to determine if there was an issue sending to
            that client.

        '''

        #  get the telegram length and type
        telegram_length = len(telegram_bytes)
        telegram_type = telegram_bytes[0:2].decode("utf-8")

        #  now send it to each of our clients
        sent_bytes = {}
        for address_key,  client in self.clients.items():
            #  send the telegram
            bytes_sent = self.udp_socket.writeDatagram(telegram_bytes,
                    client['host_address'], client['port'])
            #  keep track of how many bytes we send to each client
            sent_bytes[address_key] = bytes_sent
            #  check if we were able to send the full datagram
            if bytes_sent != telegram_length:
                #  nope, log the error
                error_str = ("Incomplete %s telegram sent to %s:%i. " %
                        (telegram_type, client['host_address'].toString(),
                        client['port']))
                error_str += ('Telegram length: %i, Bytes sent: %i' %
                        (telegram_length, bytes_sent))
                self.logger.error(error_str)
            else:
                #  yes, output some debug info
                self.logger.debug('Sent %i byte %s telegram to %s:%i' %
                    (telegram_length, telegram_type,
                    client['host_address'].toString(), client['port']))

        #  if we're testing, keep track of the number of telegrams sent and
        #  exit when the number hits the limit.
        if self.test_run:
            self.n_test_datagrams += 1
            if self.n_test_datagrams == self.TEST_DATAGRAMS_LIMIT:
                self.stop_app()

        return sent_bytes


    def get_channel_configuration(self, channel_name, defaults={}):
        '''get_channel_configuration returns a bool specifying if the channel should
        be utilized and a dict containing any channel configuration parameters.

        It first looks for channel specific entries, if that isn't found it checks
        for a 'default' entry. If a channel specific entry doesn't exist and there
        is no 'default' section, the channel is not used by the application.
        '''

        def update( d, u):
            """
            Update a nested dictionary or similar mapping.

            Source: https://stackoverflow.com/questions/3232943/update-value-of-a-nested-dictionary-of-varying-depth
            Credit: Alex Martelli / Alex Telon
            """
            for k, v in u.items():
                if isinstance(v, collections.abc.Mapping):
                    #  if a value is None, just assign the value, otherwise keep going
                    if d.get(k, {}) is None:
                        d[k] = v
                    else:
                        d[k] = update(d.get(k, {}), v)
                else:
                    d[k] = v
            return d

        add_channel = False

        #  start with the default channel configuration
        config = defaults

        # Look for a channel specific entry first
        if channel_name in self.configuration['channels']:
            #  update this channel's config with the channel specific settings
            config = update(config, self.configuration['channels'][channel_name])
            #  we add channels that are explicitly configured in the config file
            add_channel = True

        # If that fails, check for a default section
        elif 'default' in self.configuration['channels']:
            #  update this channel's config with the channels specific settings
            config = update(config, self.configuration['channels']['default'])
            #  we add all channels if there is a 'default' section in the config file
            add_channel = True

        return add_channel, config


def exit_handler(a,b=None):
    '''
    exit_handler is called when CTRL-c is pressed on Windows
    '''
    global ctrlc_pressed

    if not ctrlc_pressed:
        #  make sure we only act on the first ctrl-c press
        ctrlc_pressed = True
        print("CTRL-C detected. Shutting down...")
        console_app.stop_app()

    return True


def signal_handler(*args):
    '''
    signal_handler is called when ctrl-c is pressed when the python console
    has focus. On Linux this is also called when the terminal window is closed
    or when the Python process gets the SIGTERM signal.
    '''
    global ctrlc_pressed

    if not ctrlc_pressed:
        #  make sure we only act on the first ctrl-c press
        ctrlc_pressed = True
        print("CTRL-C or SIGTERM/SIGHUP detected. Shutting down...")
        console_app.stop_app()

    return True


if __name__ == '__main__':
    import os
    import sys
    import argparse

    #  define the default config file - a config file is required
    config_file = './telegram_blaster.yml'

    #  by default we will not "clean" all of the subscriptions and endpoints
    #  from the server. Normally you wouldn't want or need to do this but during
    #  application development your application may crash and not clean up
    #  after itself. When this happens, you will not be able to
    clean_server = False

    #  create a state variable to track if the user typed ctrl-c to exit
    ctrlc_pressed = False
    
    #  test run 
    test_run = False

    #  Set up the handlers to trap ctrl-c
    if sys.platform == "win32":
        #  On Windows, we use win32api.SetConsoleCtrlHandler to catch ctrl-c
        import win32api
        win32api.SetConsoleCtrlHandler(exit_handler, True)
    else:
        #  On linux we can use signal to get not only ctrl-c, but
        #  termination and hangup signals also.
        import signal
        signal.signal(signal.SIGINT, signal_handler)
        signal.signal(signal.SIGTERM, signal_handler)
        signal.signal(signal.SIGHUP, signal_handler)

    #  parse the command line arguments
    parser = argparse.ArgumentParser(description='telegram_blaster uses the EK80 REST client to subscribe to ' +
            'data channels and broadcast EK500 style telegrams on the network.')
    parser.add_argument("-c", "--clean", help="Set to True to remove all server subscriptions before running.")
    parser.add_argument("-f", "--config_file", help="Specify the path to the yml configuration file.")
    parser.add_argument("-t", "--test_run", help="Set to True to emit a limited number of telegrams and exit." +
            " This is useful when running in an IDE where exiting using ctrl-c doesn't work.")

    args = parser.parse_args()

    if (args.clean):
        clean_server = True
    if (args.test_run):
        test_run = True
    if (args.config_file):
        config_file = os.path.normpath(str(args.config_file))

    #  create an instance of QCoreApplication and and instance of the our example application
    app = QtCore.QCoreApplication(sys.argv)
    console_app = telegram_blaster(config_file, clean_server=clean_server, test_run=test_run,
            parent=app)

    #  and start the event loop
    sys.exit(app.exec_())
