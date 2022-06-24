"""
telegram_blaster.py

This application creates bottom depth and echogram subscriptions for
all channels and then broadcasts Q Telegrams derived from these data
on the network. This can be used to send data to Echolog500 for
"liveview" applications where Echolog80 does not work well.


"""

import logging
import collections
import yaml
from PyQt5 import QtCore
import ek80_rest_client


class telegram_blaster(QtCore.QObject):

    stopClient = QtCore.pyqtSignal()

    def __init__(self, config_file, clean_server=False, parent=None):
        #  initialize the superclass
        super(telegram_blaster, self).__init__(parent)

        #  store our command line args
        self.config_file = config_file
        self.clean_server = clean_server

        #  start things up after we get the event loop running by using a timer
        QtCore.QTimer.singleShot(0, self.startApp)


    def startApp(self):

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

        #  create an instance of the client and connect some signals

        self.logger.debug("Connecting to EK80 server at %s." %
                self.configuration['application']['ek80_server_ip'])
        self.client = ek80_rest_client.ek80_rest_client(server_address=
                self.configuration['application']['ek80_server_ip'])
        self.client.subscriptionData.connect(self.subscriptionDataAvailable)
        self.client.cleanupComplete.connect(self.clientStopped)
        self.stopClient.connect(self.client.cleanup_client)

        #  check if we need to wipe all of the subscriptions (and endpoints)
        #  from the server. This is sometimes needed while developing client
        #  apps after they crash and leave their bits around on the server.
        if self.clean_server:
            self.logger.debug("Removing and cleaning up all connections on the server. (-c==True)")
            self.client.cleanup_server()


        #  get the list of channels
        self.channels = self.client.get_channels()
        chan_string = ', '.join(self.channels)
        self.logger.debug("Channels found: %s", chan_string)

        self.bottom_sub_ids = []
        self.echogram_sub_ids = []
        if len(self.channels) > 0:
            for channel in self.channels:

                add_channel, channel_config = self.get_channel_configuration(channel)

                if add_channel:
                    #  this channel has either an explicit entry or a "default"
                    #  entry exists and will be used.
                    self.logger.debug("Adding channel %s ", channel)

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
                            range_start=channel_config['surface_echogram_start'])
                    self.echogram_sub_ids.append(echogram_sub)

                else:
                    #  we're not adding this channel
                    self.logger.debug("Channel %s not found in config file. Skipping.",
                            channel)

        else:
            #  no channels?
            self.logger.critical("No channels found! Nothing to do so we're exiting...")
            QtCore.QCoreApplication.instance().quit()
            return


    def stopApp(self):

        self.logger.debug("Cleaning up the client...")
        self.stopClient.emit()


    @QtCore.pyqtSlot()
    def clientStopped(self):

        self.logger.debug("Client cleanup complete.")
        self.logger.info("Application exiting...")
        QtCore.QCoreApplication.instance().quit()
        return


    @QtCore.pyqtSlot(object, str, dict)
    def subscriptionDataAvailable(self, clientObj, data_type, data):

        if data_type == 'bottom detection':
            #  print the results
            print(data)
        elif data_type == 'echogram':
            print(data)
        else:
            print('type: ', data_type)
            print(data)


    def get_channel_configuration(self, channel_name):
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
        config = {}

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


def exitHandler(a,b=None):
    '''
    exitHandler is called when CTRL-c is pressed on Windows
    '''
    global ctrlc_pressed

    if not ctrlc_pressed:
        #  make sure we only act on the first ctrl-c press
        ctrlc_pressed = True
        print("CTRL-C detected. Shutting down...")
        example_app.stopApp()

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
        example_app.stopApp()

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
        win32api.SetConsoleCtrlHandler(exitHandler, True)
    else:
        #  On linux we can use signal to get not only ctrl-c, but
        #  termination and hangup signals also.
        import signal
        signal.signal(signal.SIGINT, signal_handler)
        signal.signal(signal.SIGTERM, signal_handler)
        signal.signal(signal.SIGHUP, signal_handler)

    #  parse the command line arguments
    parser = argparse.ArgumentParser(description='TelegramBlaster uses the EK80 REST client to subscribe to ' +
            'data channels and broadcast EK500 style telegrams on the local network.')
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
