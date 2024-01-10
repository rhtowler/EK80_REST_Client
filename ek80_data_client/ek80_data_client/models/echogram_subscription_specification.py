# coding: utf-8

"""
    REST API for setting up data subscriptions on the EK80 Echo Sounder

    The API, and the documentation of it, is still under construction. Feel free to experiment with it, but Kongsberg is only able to provide very limited support at the moment.  # How to start data output  1. Create a subscription  2. Create a communication end point  3. Add the subscription to the communication end point      # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class EchogramSubscriptionSpecification(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'channel_id': 'str',
        'settings': 'EchogramSettings',
        'subscription_name': 'str',
        'subscriber_name': 'str'
    }

    attribute_map = {
        'channel_id': 'channel-id',
        'settings': 'settings',
        'subscription_name': 'subscription-name',
        'subscriber_name': 'subscriber-name'
    }

    def __init__(self, channel_id='WBT 998500-15 ES18_ES', settings=None, subscription_name=None, subscriber_name=None):  # noqa: E501
        """EchogramSubscriptionSpecification - a model defined in Swagger"""  # noqa: E501

        self._channel_id = None
        self._settings = None
        self._subscription_name = None
        self._subscriber_name = None
        self.discriminator = None

        self.channel_id = channel_id
        self.settings = settings
        if subscription_name is not None:
            self.subscription_name = subscription_name
        if subscriber_name is not None:
            self.subscriber_name = subscriber_name

    @property
    def channel_id(self):
        """Gets the channel_id of this EchogramSubscriptionSpecification.  # noqa: E501


        :return: The channel_id of this EchogramSubscriptionSpecification.  # noqa: E501
        :rtype: str
        """
        return self._channel_id

    @channel_id.setter
    def channel_id(self, channel_id):
        """Sets the channel_id of this EchogramSubscriptionSpecification.


        :param channel_id: The channel_id of this EchogramSubscriptionSpecification.  # noqa: E501
        :type: str
        """
        if channel_id is None:
            raise ValueError("Invalid value for `channel_id`, must not be `None`")  # noqa: E501

        self._channel_id = channel_id

    @property
    def settings(self):
        """Gets the settings of this EchogramSubscriptionSpecification.  # noqa: E501


        :return: The settings of this EchogramSubscriptionSpecification.  # noqa: E501
        :rtype: EchogramSettings
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this EchogramSubscriptionSpecification.


        :param settings: The settings of this EchogramSubscriptionSpecification.  # noqa: E501
        :type: EchogramSettings
        """
        if settings is None:
            raise ValueError("Invalid value for `settings`, must not be `None`")  # noqa: E501

        self._settings = settings

    @property
    def subscription_name(self):
        """Gets the subscription_name of this EchogramSubscriptionSpecification.  # noqa: E501


        :return: The subscription_name of this EchogramSubscriptionSpecification.  # noqa: E501
        :rtype: str
        """
        return self._subscription_name

    @subscription_name.setter
    def subscription_name(self, subscription_name):
        """Sets the subscription_name of this EchogramSubscriptionSpecification.


        :param subscription_name: The subscription_name of this EchogramSubscriptionSpecification.  # noqa: E501
        :type: str
        """

        self._subscription_name = subscription_name

    @property
    def subscriber_name(self):
        """Gets the subscriber_name of this EchogramSubscriptionSpecification.  # noqa: E501


        :return: The subscriber_name of this EchogramSubscriptionSpecification.  # noqa: E501
        :rtype: str
        """
        return self._subscriber_name

    @subscriber_name.setter
    def subscriber_name(self, subscriber_name):
        """Sets the subscriber_name of this EchogramSubscriptionSpecification.


        :param subscriber_name: The subscriber_name of this EchogramSubscriptionSpecification.  # noqa: E501
        :type: str
        """

        self._subscriber_name = subscriber_name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(EchogramSubscriptionSpecification, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, EchogramSubscriptionSpecification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
