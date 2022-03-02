# coding: utf-8

"""
    REST API for the EK80 Echo Sounder

    This API is for internal Simrad/Kongsberg Maritime use only.  The API, and the documentation of it, is currently under construction and is subject to change without further notice  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class PingConfiguration(object):
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
        'pings': 'list[Ping]',
        'fans': 'list[RxFan]',
        'transducers': 'list[Transducer]'
    }

    attribute_map = {
        'pings': 'pings',
        'fans': 'fans',
        'transducers': 'transducers'
    }

    def __init__(self, pings=None, fans=None, transducers=None):  # noqa: E501
        """PingConfiguration - a model defined in Swagger"""  # noqa: E501

        self._pings = None
        self._fans = None
        self._transducers = None
        self.discriminator = None

        if pings is not None:
            self.pings = pings
        if fans is not None:
            self.fans = fans
        if transducers is not None:
            self.transducers = transducers

    @property
    def pings(self):
        """Gets the pings of this PingConfiguration.  # noqa: E501


        :return: The pings of this PingConfiguration.  # noqa: E501
        :rtype: list[Ping]
        """
        return self._pings

    @pings.setter
    def pings(self, pings):
        """Sets the pings of this PingConfiguration.


        :param pings: The pings of this PingConfiguration.  # noqa: E501
        :type: list[Ping]
        """

        self._pings = pings

    @property
    def fans(self):
        """Gets the fans of this PingConfiguration.  # noqa: E501


        :return: The fans of this PingConfiguration.  # noqa: E501
        :rtype: list[RxFan]
        """
        return self._fans

    @fans.setter
    def fans(self, fans):
        """Sets the fans of this PingConfiguration.


        :param fans: The fans of this PingConfiguration.  # noqa: E501
        :type: list[RxFan]
        """

        self._fans = fans

    @property
    def transducers(self):
        """Gets the transducers of this PingConfiguration.  # noqa: E501


        :return: The transducers of this PingConfiguration.  # noqa: E501
        :rtype: list[Transducer]
        """
        return self._transducers

    @transducers.setter
    def transducers(self, transducers):
        """Sets the transducers of this PingConfiguration.


        :param transducers: The transducers of this PingConfiguration.  # noqa: E501
        :type: list[Transducer]
        """

        self._transducers = transducers

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
        if issubclass(PingConfiguration, dict):
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
        if not isinstance(other, PingConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
