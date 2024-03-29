# coding: utf-8

"""
    REST API for the EK80 Echo Sounder

    The API, and the documentation of it, is still under construction. Feel free to experiment with it, but Kongsberg is only able to provide very limited support at the moment.  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class PingGroup(object):
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
        'ping_group_name': 'str',
        'interval': 'int',
        'ping_mode': 'str',
        'ping_group_pings': 'list[PingGroupPing]'
    }

    attribute_map = {
        'ping_group_name': 'ping-group-name',
        'interval': 'interval',
        'ping_mode': 'ping-mode',
        'ping_group_pings': 'ping-group-pings'
    }

    def __init__(self, ping_group_name=None, interval=None, ping_mode=None, ping_group_pings=None):  # noqa: E501
        """PingGroup - a model defined in Swagger"""  # noqa: E501

        self._ping_group_name = None
        self._interval = None
        self._ping_mode = None
        self._ping_group_pings = None
        self.discriminator = None

        if ping_group_name is not None:
            self.ping_group_name = ping_group_name
        if interval is not None:
            self.interval = interval
        if ping_mode is not None:
            self.ping_mode = ping_mode
        if ping_group_pings is not None:
            self.ping_group_pings = ping_group_pings

    @property
    def ping_group_name(self):
        """Gets the ping_group_name of this PingGroup.  # noqa: E501


        :return: The ping_group_name of this PingGroup.  # noqa: E501
        :rtype: str
        """
        return self._ping_group_name

    @ping_group_name.setter
    def ping_group_name(self, ping_group_name):
        """Sets the ping_group_name of this PingGroup.


        :param ping_group_name: The ping_group_name of this PingGroup.  # noqa: E501
        :type: str
        """

        self._ping_group_name = ping_group_name

    @property
    def interval(self):
        """Gets the interval of this PingGroup.  # noqa: E501


        :return: The interval of this PingGroup.  # noqa: E501
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this PingGroup.


        :param interval: The interval of this PingGroup.  # noqa: E501
        :type: int
        """

        self._interval = interval

    @property
    def ping_mode(self):
        """Gets the ping_mode of this PingGroup.  # noqa: E501


        :return: The ping_mode of this PingGroup.  # noqa: E501
        :rtype: str
        """
        return self._ping_mode

    @ping_mode.setter
    def ping_mode(self, ping_mode):
        """Sets the ping_mode of this PingGroup.


        :param ping_mode: The ping_mode of this PingGroup.  # noqa: E501
        :type: str
        """
        allowed_values = ["single", "interval", "maximum"]  # noqa: E501
        if ping_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `ping_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(ping_mode, allowed_values)
            )

        self._ping_mode = ping_mode

    @property
    def ping_group_pings(self):
        """Gets the ping_group_pings of this PingGroup.  # noqa: E501


        :return: The ping_group_pings of this PingGroup.  # noqa: E501
        :rtype: list[PingGroupPing]
        """
        return self._ping_group_pings

    @ping_group_pings.setter
    def ping_group_pings(self, ping_group_pings):
        """Sets the ping_group_pings of this PingGroup.


        :param ping_group_pings: The ping_group_pings of this PingGroup.  # noqa: E501
        :type: list[PingGroupPing]
        """

        self._ping_group_pings = ping_group_pings

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
        if issubclass(PingGroup, dict):
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
        if not isinstance(other, PingGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
