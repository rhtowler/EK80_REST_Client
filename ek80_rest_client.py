# -*- coding: utf-8 -*-
"""


@author: Rick Towler
"""


import uuid
import datetime
import zmq
import ek80_data_client
import ek80_param_client
from ek80_data_client.rest import ApiException
from PyQt5 import QtCore


class ek80_rest_client(QtCore.QObject):

    #  set the zmq message polling interval in ms
    ZMQ_POLL_INTERVAL = 10


    #  define our signals
    subscriptionData = QtCore.pyqtSignal(int, dict)


    def __init__(self, server_address='localhost', param_server_port=12345,
            data_server_port=12346, name=None, parent=None):

        super(ek80_rest_client, self).__init__(parent)

        #  clients must have unique names. If you do not provide one, a
        #  unique UUID will be generated.
        if name:
            self.name = str(name)
        else:
            self.name = str(uuid.uuid1())

        #  initialize some attributes
        self.endpoints = {}
        self.subscriptions = {}
        self.n_subscriptions = 0
        self.next_server_port = 24240
        self.server_address = server_address

        #  create instances of our ek80_data_client and ek80_parameter_clients
        self.param_client_config = ek80_param_client.Configuration()
        self.param_client_config.host="http://" + server_address + ":" + str(param_server_port)
        self.param_api_client = ek80_param_client.ApiClient(configuration=self.param_client_config)
        self.data_client_config = ek80_data_client.Configuration()
        self.data_client_config.host="http://" + server_address + ":" + str(data_server_port)
        self.data_api_client = ek80_data_client.ApiClient(configuration=self.data_client_config)

        #  create a timer to poll the zero-mq subscriptions
        self.poll_timer = QtCore.QTimer(self)
        self.poll_timer.timeout.connect(self.poll_zmq_messages)


    def create_server_endpoint(self, name=None):
        '''
        create_server_endpoint is an internal method that creates an endpoint
        on the server. Think of an endpoint as a socket where data from subscriptions
        is sent. Multiple subscriptions can share an endpoint.

        name (str) - A unique name for the endpoint.
        '''

        #  set the endpoint name - this must be unique for each endpoint
        if name:
            name = str(name)
        else:
            #  generate a unique name using the client name and server port
            name = self.name + '-' + self.next_server_port

        #  create an instance of the CommunicationEndPoints API
        api_instance = ek80_data_client.CommunicationEndPointsApi(self.data_api_client)

        #  craft the endpoint address string
        endpoint = 'tcp://' + self.server_address + ':' + str(self.next_server_port)

        #  create an instance of the end point settings object. This client always
        #  uses the zero-mq messaging system which as of 21.15 is the only system
        #  that is implemented.
        com_settings = ek80_data_client.CommunicationEndPointSettings(name, endpoint, 'zero-mq')

        #  create the endpoint - this returns the endpoint ID
        endpoint_id = api_instance.create_communication_end_point(com_settings)

        #  create the zmq subscriber for this endpoint
        zmq_context = zmq.Context()
        zmq_sock = self.context.socket(zmq.SUB)
        zmq_sock.connect (endpoint)
        zmq_sock.setsockopt(zmq.SUBSCRIBE, b'')

        #  add this endpoint to the endpoints dict
        self.endpoints[endpoint_id] = {'endpoint':endpoint, 'zmq_context':zmq_context,
                'zmq_socket':zmq_sock, 'subscriptions':[]}

        #  check if we're polling and if not, start
        if not self.poll_timer.isActive():
            self.poll_timer.start(self.ZMQ_POLL_INTERVAL)

        #  increment the server port
        self.next_server_port += 1

        #  return the endpoint id
        return endpoint_id


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


    def update_bottom_detection_subscription(self, sub_id, upper_detector_limit=10,
            lower_detector_limit=1000, bottom_back_step=-50):

        if self.subscriptions[sub_id]['type'] != 'bottom':
            raise ValueError('Error updating bottom detector subscription. Subscription ' +
                    '%i is not a bottom detection subscription' % (sub_id))

        sub_settings = ek80_data_client.BottomDetectionSettings()

        #  set the various properties
        sub_settings.upper_detector_limit = upper_detector_limit
        sub_settings.lower_detector_limit = lower_detector_limit
        sub_settings.bottom_back_step = bottom_back_step

        api_instance = ek80_data_client.BottomDetectionSubscriptionsApi()

        api_instance.update_bottom_detection_subscription(subscription_id, settings)


    def create_bottom_detection_subscription(self, channel_id, upper_detector_limit=10,
            lower_detector_limit=1000, bottom_back_step=-50, name=None,
            server_port=None, endpoint_id=None):

        #  increment the subscription counter
        self.n_subscriptions += 1

        #  if a subscription name is provided, use it, otherwise create one.
        #  The subscription name must be unique.
        if name:
            name = str(name)
        else:
            name = "%i-bottom_detection" % (self.n_subscriptions)

        #  check if we've been provided an endpoint to use. If not, generate one.
        if endpoint_id not in self.endpoints:
            endpoint_id, endpoint = self.create_server_endpoint()
            self.endpoints[endpoint_id] = {'endpoint':endpoint, 'subscriptions':[]}

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

            #  add this sub to the subscriptions dict
            self.subscriptions[sub_id] = {'name':name, 'channel_id':channel_id,
                    'endpoint_id':endpoint_id, 'settings':sub_settings,
                    'spec':sub_spec, 'type':'bottom'}

            #  and connect the subscription to the endpoint
            subscription_output_args = ek80_data_client.SubscriptionOutputArgs(sub_id, 'c-struct')
            api_instance.add_subscription_to_end_point(endpoint_id, subscription_output_args)
            self.endpoints[endpoint_id]['subscriptions'].append(sub_id)

        except ApiException as e:
            print("Exception when calling CreateADataSubscriptionApi->create_bottom_detection_subscription: %s\n" % e)


    def poll_messages(self):


        poll_result = self.socket_sub.poll(timeout=0)
        if poll_result == zmq.POLLIN:
            msg = self.socket_sub.recv()
            print(msg)



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

