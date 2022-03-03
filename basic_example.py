"""


"""
from PyQt5 import QtCore
import ek80_rest_client
import datetime


class basic_example(QtCore.QObject):

    def __init__(self, server_address, parent=None):
        #  initialize the superclass
        super(basic_example, self).__init__(parent)

        #  store some important parameters
        self.client = ek80_rest_client.ek80_rest_client(server_address=server_address)

        #  get this started...
        QtCore.QTimer.singleShot(0, self.startApp)


    def startApp(self):

        self.channels = self.client.get_channels()
        print(self.channels)

        if len(self.channels) > 0:
            id = self.client.create_bottom_detection_subscription(self.channels[0])



    @QtCore.pyqtSlot(object, tuple)
    def processSubscriptionData(self, erClientObj, data):

        #  the data passed to processSubscriptionData is a tuple.  The specific
        #  format varies depending on the subscription type but all subscriptions
        #  share the first 4 fields:
        #    (subscription type, subscription ID, channel ID, time, ...
        #
        #  These will be documented better but for now look at the simradClientDatChannel
        #  processPRDdata method for details.

        print(data)

        if data[0] == 'bottomdetection':
            #  convert the date to something readable
            #
            #  all dates are in Python's timestamp which is the number of seconds
            #  since the epoch which for most platforms is Jan 1, 1970.  First
            #  we convert to a datetime tuple:
            #    (year, month, day, hour, min, sec, microsec)
            dt = datetime.datetime.utcfromtimestamp(data[3])

            #  print the results
            print (data[0] + ' from channel ' + data[2] + ' at ' + str(dt.hour).rjust(2,'0') +
                   ':' + str(dt.minute).rjust(2,'0') + ':' + str(dt.second).rjust(2,'0') + '.' +
                   str(dt.microsecond/10000).rjust(2,'0') + '  Depth:' + str(data[4]))





if __name__ == '__main__':

    import sys

    #  define the server's IP address, username and password
    server_address = 'localhost'


    app = QtCore.QCoreApplication(sys.argv)
    form = basic_example(server_address)
    sys.exit(app.exec_())
