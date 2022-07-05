"""
telegram_blaster.py

This application creates bottom depth and echogram subscriptions for
all channels and then broadcasts Q Telegrams derived from these data
on the network. This can be used to send data to Echolog500 for
"liveview" applications where Echolog80 does not work well.


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

    def __init__(self, config_file, clean_server=False, parent=None):
        #  initialize the superclass
        super(telegram_blaster, self).__init__(parent)

        #  store our command line args
        self.config_file = config_file
        self.clean_server = clean_server

        #  define some initial properties
        self.udp_socket = None

        #  create a timer for polling the server
        self.param_timer = QtCore.QTimer(self)
        self.param_timer.timeout.connect(self.poll_parameters)

        #  create a timer for reestablishing a lost connection.
        self.retry_timer = QtCore.QTimer(self)
        self.retry_timer.timeout.connect(self.reestablish_connection)

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
        self.retry_timer.setInterval(self.configuration['application']['lost_server_retry_interval_ms'])
        self.retry_timer.setSingleShot(True)

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

        #  create subscriptions to receive data required to send our EK500 telegrams
        #  of choice. Currently that is VL, D, B, and Q telegrams so we subscribe to
        #  echogram and bottom detections for our channels of interest
        self.bottom_sub_ids = []
        self.echogram_sub_ids = []
        if len(self.channels) > 0:
            for channel in self.channels:

                #  process the channel config data to determine if we're adding
                #  this channel and return the config parameters.
                add_channel, channel_config = self.get_channel_configuration(channel)

                if add_channel:
                    #  this channel has either an explicit entry or a "default"
                    #  entry exists and will be used.
                    self.logger.info("Adding channel %s ", channel)

                    #  add the bottom detection subscription
                    bottom_detect_sub = self.client.create_bottom_detection_subscription(channel,
                            upper_detector_limit=channel_config['upper_detector_limit'],
                            lower_detector_limit=channel_config['lower_detector_limit'],
                            bottom_back_step=channel_config['bottom_back_step'])
                    self.bottom_sub_ids.append(bottom_detect_sub)

                    #  add the surface echogram subscription
                    echogram_sub = self.client.create_echogram_subscription(channel,
                            pixel_count=channel_config['surface_echogram_count'],
                            range=channel_config['surface_echogram_range'],
                            range_start=channel_config['surface_echogram_start'],
                            ek500_db_format=True)
                    self.echogram_sub_ids.append(echogram_sub)

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

            print(nav_data)

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

        self.logger.info("Trying to (re)connect to EK80 server")

        #  try to get the navigation data. This call will succeed
        try:
            _ = self.client.get_navigation()

        except Exception:
            self.retry_timer.start()
            return

        self.logger.info("Cleaning up old subscriptions...")
        self.client.cleanup_client(quiet=True)

        self.logger.info("Creating new subscriptions...")
        self.create_subscritions()

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
    def get_header_data(self,  datetime_val):

        #get the header info for the B/VL datagrams (i.e a string "VL,HHMMSShh,YYMMDD, "):
        #get time as string HHMMSShh: RICK- ok to just strip out the excessive millesecond places, as opposed to round?
        header_time = datetime_val.strftime("%H%M%S%f")[:-4]

        #get year, month, day zero padded (i.e day 6 = 06) as a string YYMMDD
        header_date = datetime_val.strftime("%y%m%d")
        #combine as datetime string "VL,HHMMSShh,YYMMDD, "; convert to a byte
        header_bytes = bytes(('VL,' +header_time+ ','+header_date+', '), 'utf-8')

        return header_bytes


    @QtCore.pyqtSlot(object, str, dict)
    def subscription_data_available(self, clientObj, data_type, data):

        if data_type == 'bottom detection':

            #  you should have enough data from the bottom detection
            #  subscription to create both a B and VL datagram so you
            #  would do that here


            #  create the header
            header_bytes = self.get_header_data( data['pingTime'])
            #  get the vessel log distance formatted as a C float
            dist_bytes = struct.pack('f', data['vesselLogDistance'])
            #  pack the data as a properly formatted byte array
            telegram_bytes = header_bytes + dist_bytes
            #  and then send the datagram
            self.send_telegram(telegram_bytes)


        elif data_type == 'echogram':

            #  here you would piece together the Q datagram and then
            #  pack the datagram into a byte array

            #  and then send the datagram
            #self.send_telegram(telegram_bytes)

            #  but for now, print the results
            print(data)
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
        example_app.stop_app()

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
        example_app.stop_app()

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

    args = parser.parse_args()

    if (args.clean):
        clean_server = True
    if (args.config_file):
        config_file = os.path.normpath(str(args.config_file))

    #  create an instance of QCoreApplication and and instance of the our example application
    app = QtCore.QCoreApplication(sys.argv)
    example_app = telegram_blaster(config_file, clean_server=clean_server,
            parent=app)

    #  and start the event loop
    sys.exit(app.exec_())
