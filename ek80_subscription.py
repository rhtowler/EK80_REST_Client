# -*- coding: utf-8 -*-
"""


@author: Rick Towler
"""

import datetime
from PyQt5 import QtCore
import ek80_data_client
import zmq



class ek80_subscription(QtCore.QObject):

    #  define our signals
    datChannelError = QtCore.pyqtSignal(str, str)

    def __init__(self, id, name, channel_id, data_api_client, parent=None):

        super(ek80_subscription, self).__init__(parent)

        self.id = id
        self.name = name
        self.channel_id = channel_id
        self.data_api_client = data_api_client


    def start_subscription(self, server_address, server_port, endpoint_name=None):

        if endpoint_name:
            endpoint_name = str(endpoint_name)
        else:
            endpoint_name = self.name

        api_instance = ek80_data_client.CommunicationEndPointsApi(self.data_api_client)
        endpoint = 'tcp://' + server_address + ':' + str(server_port)
        endpoint = 'tcp://161.55.246.23:22330'
        endpoint = 'tcp://192.168.0.131:22333'


        com_settings = ek80_data_client.CommunicationEndPointSettings('test4', endpoint, 'zero-mq')
        self.endpoint_id = api_instance.create_communication_end_point(com_settings)


        subscription_output_args = ek80_data_client.SubscriptionOutputArgs(self.id, 'c-struct')
        api_instance.add_subscription_to_end_point(self.endpoint_id, subscription_output_args)

        self.context = zmq.Context()
        self.socket_sub = self.context.socket(zmq.SUB)
        self.socket_sub.connect (endpoint)
        self.socket_sub.setsockopt(zmq.SUBSCRIBE, b'')

        self.poll_timer = QtCore.QTimer(self)
        self.poll_timer.timeout.connect(self.poll_messages)
        self.poll_timer.start(10)


    def poll_messages(self):


        poll_result = self.socket_sub.poll(timeout=0)
        if poll_result == zmq.POLLIN:
            msg = self.socket_sub.recv()
            print(msg)

#
#        try:
#            msg_data = self.socket.recv(flags=zmq.NOBLOCK)
#            print(msg_data)
#        except:
#            #  no messages available
#            pass


    def convert_nt_time(self, l, h):
        '''
        convert_nt_time is an internal function that converts 64-bit "NT" time
        (an integer specifying the number of 100-nanosecond intervals which have
        passed since January 1, 1601) to Unix time (number of seconds that have
        elapsed since 00:00:00 Coordinated Universal Time (UTC), Thursday, 1
        January 1970)

        The input 64-bit value is split into the two 32 bits "l" and "h"
        '''
        #  difference between 1601 and 1970
        d = 116444736000000000

        #  shift and divide by 10 million to convert to seconds
        ts = (((int(h)<< 32) + int(l))-d) / 10000000.0

        return datetime.fromtimestamp(ts)



#    def processPRDdata(self, subObj):
#        '''
#        processPRDdata processes complete PRD datagrams creating a tuple containing
#        the processed data. It then emits a signal containing the data .
#        '''
#
#        ekdbCC = 0.01175898421         #  EK500 dB conversion factor (10 * log10(2) / 256)
#
##        #  extract ping time
##        time = self.__convNTtime(array.array('L', subObj.buffer[0:4])[0],
##                                 array.array('L', subObj.buffer[4:8])[0])
#
#        #  process buffer based on subscription type
#        type = subObj.type.lower()
#        if type == 'bottomdetection':
#            #  construct the BottomDetection tuple
#            cbData = (subObj.type,                                      #  type
#                            subObj.id,                                        #  id
#                            subObj.channel,                                   #  channel
#                            time,                                                               #  time
#                            array.array('d', subObj.buffer[8:16])[0],       #  depth
#                            array.array('d', subObj.buffer[16:24])[0],      #  reflectivity
#                            array.array('d', subObj.buffer[24:32])[0])      #  distance
#
#
#        elif type == 'tsdetection':
#            #  determine the number of echotraces
#            nTraces = array.array('H', subObj.buffer[8:10])[0]
#
#            #  construct the echotrace list
#            echotraces = []
#            for i in range(nTraces):
#                idx = (i * 48) + 10
#                echotraces.append((array.array('d', subObj.buffer[idx:idx+8])[0],
#                                  array.array('d', subObj.buffer[idx+8:idx+16])[0],
#                                  array.array('d', subObj.buffer[idx+16:idx+24])[0],
#                                  array.array('d', subObj.buffer[idx+24:idx+32])[0],
#                                  array.array('d', subObj.buffer[idx+32:idx+40])[0],
#                                  array.array('d', subObj.buffer[idx+40:idx+48])[0]))
#
#            #  construct the TSDetection tuple
#            cbData = (subObj.type,
#                      subObj.id,                                        #  id
#                      subObj.channel,                                   #  channel
#                      time,                                             #  time
#                      nTraces,                                          #  number of echotraces
#                      echotraces)                                       #  echotrace tuples
#
#
#        elif type == 'sampledata':
#            if subObj.sampleType.lower() == 'powerangle':
#                #  get the number of power and angle values
#                #nPowerVals = array.array('L', subObj.buffer[8:12])[0]
#                #nAngleVals = array.array('L', subObj.buffer[12:16])[0]
#
#                #  extract the power and angle data
#                powAng = array.array('h', subObj.buffer[16:])
#                #  separate power and angle values
#                power = powAng[0::2].tolist()
#                angle = powAng[1::2].tolist()
#                powAng = []
#
#                #  convert power data
#                if subObj.EKdBS  == 0:
#                    power = map(lambda x: x*ekdbCC, power)
#
#                cbData = (subObj.type,
#                          subObj.sampleType,
#                          subObj.id,                                        #  id
#                          subObj.channel,                                   #  channel
#                          time,                                             #  time
#                          power,                                            #  power data
#                          angle)                                            #  angle data
#
#            else:
#                #  extract the sample data
#                sampData = array.array('h', subObj.buffer[8:]).tolist()
#
#                #  convert power data
#                if subObj.EKdB  == 0:
#                    sampData = map(lambda x: x*ekdbCC, sampData)
#
#                cbData = (subObj.type,
#                          subObj.sampleType,
#                          subObj.id,                                        #  id
#                          subObj.channel,                                   #  channel
#                          time,                                             #  time
#                          sampData)                                         #  sample data
#
#
#        elif type == 'echogram' or type == 'targetsechogram':
#            #  extract the sample data
#            echogram = array.array('h', subObj.buffer[8:]).tolist()
#
#            #  convert power data
#            if subObj.EKdB == 0:
#                echogram = map(lambda x: x*ekdbCC, echogram)
#
#            cbData = (subObj.type,                                      #  type
#                      subObj.sampleType,                                #  TVG type
#                      subObj.id,                                        #  id
#                      subObj.channel,                                   #  channel
#                      time,                                             #  time
#                      echogram)                                         #  echogram data
#
#
#        elif type == 'integration' or type == 'targetsintegration':
#            #  extract the sa value
#            sa = array.array('d', subObj.buffer[8:16])[0]
#
#            cbData = (subObj.type,                                      #  type
#                      subObj.id,                                        #  id
#                      subObj.channel,                                   #  channel
#                      time,                                             #  time
#                      sa)                                               #  sa

