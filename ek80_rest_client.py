# -*- coding: utf-8 -*-
"""


@author: Rick Towler
"""


import uuid
import datetime
import ek80_data_client
import ek80_param_client
from ek80_data_client.rest import ApiException
from PyQt5 import QtCore
import ek80_subscription
from zmq.eventloop import ioloop


ioloop.install()


class ek80_rest_client(QtCore.QObject):

    #  define our signals
    subscriptionData = QtCore.pyqtSignal(int, dict)


    def __init__(self, server_address='localhost', param_server_port=12345,
            data_server_port=12346, name=None, parent=None):

        super(ek80_rest_client, self).__init__(parent)


        if name:
            self.name = str(name)
        else:
            self.name = str(uuid.uuid1())

        self.subscriptions = {}
        self.n_subscriptions = 0
        self.next_server_port = 24240
        self.server_address = server_address

        #  create instances of our ek80_data_client and ek80_data_clients
        self.param_client_config = ek80_param_client.Configuration()
        self.param_client_config.host="http://" + server_address + ":" + str(param_server_port)
        self.param_api_client = ek80_param_client.ApiClient(configuration=self.param_client_config)

        self.data_client_config = ek80_data_client.Configuration()
        self.data_client_config.host="http://" + server_address + ":" + str(data_server_port)
        self.data_api_client = ek80_data_client.ApiClient(configuration=self.data_client_config)


    def get_channels(self):
        '''
        get_channels returns a list containing the installed echosounder channels
        '''

        try:

            pca = ek80_param_client.PingConfigurationApi(self.param_api_client)
            channels = pca.ping_configuration_get_channels()

        except ApiException as e:
            print("Exception when calling get_transceivers: %s\n" % e)

        return channels


    def create_bottom_detection_subscription(self, channel_id, upper_detector_limit=10,
            lower_detector_limit=1000, bottom_back_step=-50, name=None,
            server_port=None):


        self.n_subscriptions += 1
        if name:
            name = str(name)
        else:
            name = "%i-bottom_detection" % (self.n_subscriptions)


        #  create an instance of the create subscription API
        api_instance = ek80_data_client.CreateADataSubscriptionApi(self.data_api_client)

        #  create our settings and spec objects
        sub_settings = ek80_data_client.BottomDetectionSettings()
        sub_spec = ek80_data_client.BottomDetectionSubscriptionSpecification()

        #  set the various properties
        sub_settings.upper_detector_limit = upper_detector_limit
        sub_settings.lower_detector_limit = lower_detector_limit
        sub_settings.bottom_back_step = bottom_back_step
        sub_spec.channel_id = channel_id
        sub_spec.settings = sub_settings
        sub_spec.subscriber_name = self.name
        sub_spec.subscription_name = name

        #  now try to create the subscription
        try:
            #  create the subscription
            sub_id = api_instance.create_bottom_detection_subscription(sub_spec)
            self.subscriptions[sub_id] = {'name':name, 'channel_id':channel_id}

        except ApiException as e:
            print("Exception when calling CreateADataSubscriptionApi->create_bottom_detection_subscription: %s\n" % e)


        self.subscriptions[sub_id] = ek80_subscription.ek80_subscription(sub_id, name,
                channel_id, self.data_api_client)

        self.subscriptions[sub_id].start_subscription(self.server_address,
                self.next_server_port)
        self.next_server_port += 1

        print(self.subscriptions)


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

