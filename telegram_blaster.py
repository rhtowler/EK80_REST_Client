"""
QTelegramBlaster.py

This application creates bottom depth and echogram subscriptions for
all channels and then broadcasts Q Telegrams derived from these data
on the network. This can be used to send data to Echolog500 for
"liveview" applications where Echolog80 does not work well.


"""

from PyQt5 import QtCore
import ek80_rest_client


class telegram_blaster(QtCore.QObject):

    stopClient = QtCore.pyqtSignal()

    def __init__(self, config_file, clean_server=False, parent=None):
        #  initialize the superclass
        super(telegram_blaster, self).__init__(parent)

        self.config_file = config_file



        #  check if we need to wipe all of the subscriptions (and endpoints)
        #  from the server. This is sometimes needed while developing client
        #  apps after they crash and leave their bits around on the server.
        if clean_server:
            self.client.cleanup_server()

        #  get this started...
        QtCore.QTimer.singleShot(0, self.startApp)


    def startApp(self):

        #  bump the cursor
        print()

        #  read the configuration file
        with open(self.config_file, 'r') as cf_file:
            try:
                config = yaml.safe_load(cf_file)
            except yaml.YAMLError as exc:
                print('Error reading configuration file ' + self.config_file)
                print('  Error string:' + str(exc))
                print('  Exiting...')
                QtCore.QCoreApplication.instance().quit()
                return

        #  create a logger to log to the console
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(config['log_level'])
        formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(module)s - %(message)s')
        consoleLogger = logging.StreamHandler(sys.stdout)
        consoleLogger.setFormatter(formatter)
        self.logger.addHandler(consoleLogger)



        #  create an instance of the client and connect some signals
        self.client = ek80_rest_client.ek80_rest_client(server_address=server_address)
        self.client.subscriptionData.connect(self.subscriptionDataAvailable)
        self.client.cleanupComplete.connect(self.clientStopped)
        self.stopClient.connect(self.client.cleanup_client)


        #  get the list of channels
        self.channels = self.client.get_channels()
        print(self.channels)

        self.bottom_sub_ids = []
        for channel in self.channels:
            self.bottom_sub_ids.append(self.client.create_bottom_detection_subscription(channel))

        else:
            print('No channels found. Exiting...')
            QtCore.QCoreApplication.instance().quit()
            return


    def stopApp(self):

        print("Cleaning up the client...")
        self.stopClient.emit()


    @QtCore.pyqtSlot()
    def clientStopped(self):

        print("Client cleanup complete.")
        print("Application exiting...")
        QtCore.QCoreApplication.instance().quit()
        return


    @QtCore.pyqtSlot(object, str, dict)
    def subscriptionDataAvailable(self, clientObj, data_type, data):

        if data_type == 'bottom_detection':
            #  print the results
            print(data)




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
