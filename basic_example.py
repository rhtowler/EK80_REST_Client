"""


"""

from PyQt5 import QtCore
import ek80_rest_client


class basic_example(QtCore.QObject):

    stopClient = QtCore.pyqtSignal()

    def __init__(self, server_address, clean_server=False, parent=None):
        #  initialize the superclass
        super(basic_example, self).__init__(parent)

        #  store some important parameters
        self.client = ek80_rest_client.ek80_rest_client(server_address=server_address)
        self.client.subscriptionData.connect(self.subscriptionDataAvailable)
        self.client.cleanupComplete.connect(self.clientStopped)
        self.stopClient.connect(self.client.cleanup_client)

        #  check if we need to wipe all of the subscriptions (and endpoints)
        #  from the server. This is sometimes needed while developing client
        #  apps after they crash and leave their bits around on the server.
        if clean_server:
            self.client.cleanup_server()

        #  get this started...
        QtCore.QTimer.singleShot(0, self.startApp)


    def startApp(self):

        self.channels = self.client.get_channels()
        print(self.channels)

        if len(self.channels) > 0:
            id = self.client.create_bottom_detection_subscription(self.channels[0])

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
    import sys
    import argparse

    #  define the default EK80 server IP address. If an address is not passed
    #  on the command line, this address will be used
    server_address = '192.168.0.131'

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
    parser = argparse.ArgumentParser(description='Example showing a simple usage of the ek80 REST client.')
    parser.add_argument("-s", "--server", help="Specify the EK80 server IP")
    parser.add_argument("-c", "--clean", help="Set to True to remove all server subscriptions before running.")
    args = parser.parse_args()
    if (args.server):
        server_address = str(args.server)
    if (args.clean):
        clean_server = True

    #  create an instance of QCoreApplication and and instance of the our example application
    app = QtCore.QCoreApplication(sys.argv)
    example_app = basic_example(server_address, clean_server=clean_server,
            parent=app)

    #  and start the event loop
    sys.exit(app.exec_())
