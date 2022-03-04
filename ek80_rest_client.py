# coding=utf-8
#
#     National Oceanic and Atmospheric Administration (NOAA)
#     Alaskan Fisheries Science Center (AFSC)
#     Resource Assessment and Conservation Engineering (RACE)
#     Midwater Assessment and Conservation Engineering (MACE)
#
#  THIS SOFTWARE AND ITS DOCUMENTATION ARE CONSIDERED TO BE IN THE PUBLIC DOMAIN
#  AND THUS ARE AVAILABLE FOR UNRESTRICTED PUBLIC USE. THEY ARE FURNISHED "AS
#  IS."  THE AUTHORS, THE UNITED STATES GOVERNMENT, ITS INSTRUMENTALITIES,
#  OFFICERS, EMPLOYEES, AND AGENTS MAKE NO WARRANTY, EXPRESS OR IMPLIED,
#  AS TO THE USEFULNESS OF THE SOFTWARE AND DOCUMENTATION FOR ANY PURPOSE.
#  THEY ASSUME NO RESPONSIBILITY (1) FOR THE USE OF THE SOFTWARE AND
#  DOCUMENTATION; OR (2) TO PROVIDE TECHNICAL SUPPORT TO USERS.
#
"""
.. module:: ek80_rest_client.ek80_rest_client

    :synopsis: ek80_rest_client provides a simplified interface for
               the EK80 application REST server.

| Developed by:  Rick Towler   <rick.towler@noaa.gov>
| National Oceanic and Atmospheric Administration (NOAA)
| National Marine Fisheries Service (NMFS)
| Alaska Fisheries Science Center (AFSC)
| Midwater Assesment and Conservation Engineering Group (MACE)
|
| Author:
|       Rick Towler   <rick.towler@noaa.gov>
| Maintained by:
|       Rick Towler   <rick.towler@noaa.gov>
"""


import uuid
import datetime
import zmq
import ek80_data_client
import ek80_param_client
from ek80_data_client.rest import ApiException
from google.protobuf.json_format import MessageToDict
import ek80_datagrams_v2115_pb2 as ek80_datagrams_pb2
from PyQt5 import QtCore


class ek80_rest_client(QtCore.QObject):

    #  set the zmq message polling interval in ms
    ZMQ_POLL_INTERVAL = 10

    #  define our signals
    subscriptionData = QtCore.pyqtSignal(object, str, dict)
    cleanupComplete = QtCore.pyqtSignal()


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

        #  THIS IS A HACK - THE SWAGGER CLIENTS CAN'T CONNECT WITH A "REAL" IP
        #  NEED TO TRY WITH FIREWALL DISABLED
        server_address = 'localhost'

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


    def delete_bottom_detection_subscription(self, sub_id, endpoint_id=None,
            cleanup=False):
        '''
        delete_bottom_detection_subscription deletes the specified bottom
        detection subscription. It also disconnects the subscription from
        its endpoint. IT DOES NOT DELETE THE ENDPOINT.

        Args:
            sub_id (int):
                The subscription ID of the bottom detection subscription
                you are deleting.

        Returns:
            None

        Raises:
            ValueError: Raises ValueError if the subscription id doesn't exist or if
                        the subscription is not a bottom detection subscription.
        '''
        #  check if this is a valid subscription and if it is a bottom detection sub.
        #  we skip this check if we're cleaning up
        if not cleanup:
            if sub_id not in self.subscriptions:
                raise ValueError('%i is not a valid subscription id' % (sub_id))
            if self.subscriptions[sub_id]['type'] != 'bottom':
                raise ValueError('Error deleting bottom detector subscription. ' +
                        'Subscription %i is not a bottom detection subscription.' % (sub_id))

        #  if we aren't given an endpoint - get it from the subscriptions dict
        if endpoint_id is None:
            endpoint_id = self.subscriptions[sub_id]['endpoint_id']

        #  create an instance of the bottom detections subs api
        api_instance = ek80_data_client.BottomDetectionSubscriptionsApi(self.data_api_client)

        #  remove the subscription from its endpoint
        api_instance = ek80_data_client.CommunicationEndPointsApi(self.data_api_client)

        try:
            api_instance.remove_subscription_from_end_point(endpoint_id, sub_id)
        except:
            pass

        #  create an instance of the bottom detections subs api
        api_instance = ek80_data_client.BottomDetectionSubscriptionsApi(self.data_api_client)

        #  delete the bottom detection subscription
        try:
            api_instance.delete_bottom_detection_subscription(sub_id)
        except:
            pass

        #  update the endpoint's subscriptions list and remove the subscription
        #  from our subscriptions dict.
        if not cleanup:
            self.endpoints[endpoint_id]['subscriptions'].remove(sub_id)
            del self.subscriptions[sub_id]


    def get_bottom_detection_subscription(self, sub_id):
        '''

        Args:
            sub_id (int):
                The subscription ID of the bottom detection subscription
                you are requesting the state of.

        Returns:
            Dictionary with the following fields:

                    subscription_id (int)
                    channel_id (str)
                    subscription_name (str)
                    subscriber_name (str)
                    upper_detector_limit (float)
                    lower_detector_limit (float)
                    bottom_back_step (float)

        Raises:
            ValueError: Raises ValueError if the subscription id doesn't exist or if
                        the subscription is not a bottom detection subscription.

        '''

        #  check if this is a valid subscription and if it is a bottom detection sub.
        if sub_id not in self.subscriptions:
            raise ValueError('%i is not a valid subscription id' % (sub_id))
        if self.subscriptions[sub_id]['type'] != 'bottom':
            raise ValueError('Error getting bottom detector subscription configuration. ' +
                    'Subscription %i is not a bottom detection subscription.' % (sub_id))

        #  create an instance of the bottom detections subs api
        api_instance = ek80_data_client.BottomDetectionSubscriptionsApi(self.data_api_client)

        #  and use it to update our subscription
        sub_spec = api_instance.get_bottom_detection_subscription(sub_id)

        #  create the return dict
        settings = {'subscription_id':sub_id,
                    'channel_id': sub_spec.channel_id,
                    'subscription_name':sub_spec.subscription_name,
                    'subscriber_name': sub_spec.subscriber_name,
                    'upper_detector_limit':sub_spec.settings.upper_detector_limit,
                    'lower_detector_limit': sub_spec.settings.lower_detector_limit,
                    'bottom_back_step':sub_spec.settings.bottom_back_step
                    }

        return settings


    def update_bottom_detection_subscription(self, sub_id, upper_detector_limit=10,
            lower_detector_limit=1000, bottom_back_step=-50):
        '''

        Args:
            sub_id (TYPE):
                DESCRIPTION
            upper_detector_limit (TYPE):
                Optional; DESCRIPTION Defaults to 10.
            lower_detector_limit (TYPE):
                Optional; DESCRIPTION Defaults to 1000.
            bottom_back_step (TYPE):
                Optional; DESCRIPTION Defaults to -50.

        Returns:
            None

        Raises:
            ValueError: Raises ValueError if the subscription id doesn't exist or if
                        the subscription is not a bottom detection subscription.
        '''

        if sub_id not in self.subscriptions:
            raise ValueError('%i is not a valid subscription id' % (sub_id))

        if self.subscriptions[sub_id]['type'] != 'bottom':
            raise ValueError('Error updating bottom detector subscription. Subscription ' +
                    '%i is not a bottom detection subscription' % (sub_id))

        #  create a bottom detection settings obj
        sub_settings = ek80_data_client.BottomDetectionSettings()

        #  set the various properties
        sub_settings.upper_detector_limit = upper_detector_limit
        sub_settings.lower_detector_limit = lower_detector_limit
        sub_settings.bottom_back_step = bottom_back_step

        #  create an instance of the bottom detections subs api
        api_instance = ek80_data_client.BottomDetectionSubscriptionsApi(self.data_api_client)

        #  and use it to update our subscription
        api_instance.update_bottom_detection_subscription(sub_id, sub_settings)


    def create_bottom_detection_subscription(self, channel_id, upper_detector_limit=10,
            lower_detector_limit=1000, bottom_back_step=-50, name=None,
            server_port=None, endpoint_id=None):
        '''

        Args:
            channel_id (TYPE):
                DESCRIPTION
            upper_detector_limit (TYPE):
                Optional; DESCRIPTION Defaults to 10.
            lower_detector_limit (TYPE):
                Optional; DESCRIPTION Defaults to 1000.
            bottom_back_step (TYPE):
                Optional; DESCRIPTION Defaults to -50.
            name (TYPE):
                Optional; DESCRIPTION Defaults to None.
            server_port (TYPE):
                Optional; DESCRIPTION Defaults to None.
            endpoint_id (TYPE):
                Optional; DESCRIPTION Defaults to None.

        Returns:
            None

        '''

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
            endpoint_id = self.create_server_endpoint()

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
                    'endpoint_id':endpoint_id, 'type':'bottom',
                    'cleanup':self.delete_bottom_detection_subscription}

            #  and connect the subscription to the endpoint
            subscription_output_args = ek80_data_client.SubscriptionOutputArgs(sub_id, 'proto-buf')
            api_instance = ek80_data_client.CommunicationEndPointsApi(self.data_api_client)
            api_instance.add_subscription_to_end_point(endpoint_id, subscription_output_args)
            self.endpoints[endpoint_id]['subscriptions'].append(sub_id)

        except ApiException as e:
            print("Exception when calling CreateADataSubscriptionApi->create_bottom_detection_subscription: %s\n" % e)


    def poll_zmq_messages(self):
        '''

        Returns:
            None

        '''

        #  poll each of our endpoints
        for endpoint_id in self.endpoints:

            #  check if a message is available
            has_msg = self.endpoints[endpoint_id]['zmq_socket'].poll(timeout=0)
            if has_msg == zmq.POLLIN:
                #  a message is available - get it. The protobuf zmq messages
                #  are multipart where the first part is the message type
                #  and the second is the serialized protobuf data
                msg = self.endpoints[endpoint_id]['zmq_socket'].recv_multipart()

                #  process the message based on the type
                if msg[0].decode("utf-8") == 'Bot.PB.v1':
                    #  set the type
                    data_type = 'bottom_detection'
                    dg_dict = {}

                    #  create the protobuf object and decode
                    dg_data = ek80_datagrams_pb2.BottomDetectionDatagram()
                    dg_data.ParseFromString(msg[1])

                    #  convert the message obj to a dict
                    dg_dict = MessageToDict(dg_data)

                    #  and convert the ping_time to a datetime
                    dg_dict['pingTime'] = self.convert_nt_time(dg_dict['pingTime'])

                    #  emit the data signal
                    self.subscriptionData.emit(self, data_type, dg_dict)

                else:
                    print('New message type: ' +  msg[0].decode("utf-8"))


    @QtCore.pyqtSlot()
    def cleanup_client(self):
        '''
        cleanup_client should be called when you're done using the client
        to ensure that all of the client's subscriptions and endpoints
        are deleted from the server.

        If you do not call this method, or your application crashes without
        calling it, any subscriptions and endpoints you created will remain
        active on the server and the endpoint address will be unavailable
        for new endpoints.

        '''

        #  stop the polling timer if it is running
        if self.poll_timer.isActive():
            self.poll_timer.stop()

        #  delete all existing subscriptions
        for sub_id in self.subscriptions:
            self.subscriptions[sub_id]['cleanup'](sub_id, cleanup=True)

        #  and remove all existing endpoints
        for endpoint_id in self.endpoints:
            self.delete_server_endpoint(endpoint_id)

        self.subscriptions = {}
        self.endpoints = {}

        self.cleanupComplete.emit()


    def cleanup_server(self):
        '''
        cleanup_server removes ALL subscriptions and endpoints on a server.
        A properly working client application should clean up after itself
        and you should never need to call this method. But during development
        it is common for your application to crash, leaving subscriptions
        and endpoints strewn about the server like so much flotsam on the
        beach. You can call this method before making any subscriptions to
        clean these up.

        Returns:
            None

        '''

        #  stop the polling timer if it is running
        if self.poll_timer.isActive():
            self.poll_timer.stop()

        #  create an instance of the CommunicationEndPoints API
        api_instance = ek80_data_client.CommunicationEndPointsApi(self.data_api_client)

        #  get a list of all active endpoints
        endpoints = api_instance.get_active_communication_end_points()

        #  worth thru the endpoints
        for endpoint in endpoints:
            #  get the endpoint id
            endpoint_id = endpoint.communication_end_point_id

            #  get a list of subs associated with this endpoint
            subscriptions = api_instance.get_subscriptions_by_end_point(endpoint_id)

            #  work thru the subscriptions, deleting them as we go
            for sub in subscriptions:
                if sub.subscription_type == 'bottom detection':
                    self.delete_bottom_detection_subscription(sub.subscription_id,
                            endpoint_id=endpoint_id, cleanup=True)
                else:
                    print("New sub type found: " + sub.subscription_type)

            #  and delete the endpoint
            api_instance.delete_communication_end_point(endpoint_id)

        self.subscriptions = {}
        self.endpoints = {}


    def delete_server_endpoint(self, endpoint_id):
        '''

        Args:
            endpoint_id (TYPE):
                DESCRIPTION

        Returns:
            None

        Raises:
            ValueError: DESCRIPTION
        '''

        #  check if this is a valid endpoint
        if endpoint_id not in self.endpoints:
            raise ValueError('%i is not a valid endpoint id' % (endpoint_id))

        #  create an instance of the CommunicationEndPoints API
        api_instance = ek80_data_client.CommunicationEndPointsApi(self.data_api_client)

        #  and delete the endpoint
        api_instance.delete_communication_end_point(endpoint_id)


    def create_server_endpoint(self, name=None):
        '''
        create_server_endpoint is an internal method that creates an endpoint
        on the server. Think of an endpoint as a socket where data from subscriptions
        is sent. Multiple subscriptions can share an endpoint.

        Args:
            name (TYPE):
                Optional; A unique name for the endpoint. If no name is passed
                a name will be generated. Defaults to None.

        Returns:
        {0}int: The endpoint id

        '''

        #  set the endpoint name - this must be unique for each endpoint
        if name:
            name = str(name)
        else:
            #  generate a unique name using the client name and server port
            name = self.name + '-' + str(self.next_server_port)

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
        zmq_sock = zmq_context.socket(zmq.SUB)
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


    def convert_nt_time(self, nt_time):
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
        ts = (int(nt_time) - d) / 10000000.0

        return datetime.datetime.fromtimestamp(ts)

