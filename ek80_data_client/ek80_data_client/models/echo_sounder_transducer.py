# coding: utf-8

"""
    REST API for setting up data subscriptions on the EK80 Echo Sounder

    The API, and the documentation of it, is currently under construction and is subject to change without further notice  # How to start data output  1. Create a subscription  2. Create a communication end point  3. Add the subscription to the communication end point    A link example, [kongsberg.com](http://www.kongsberg.com).  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class EchoSounderTransducer(object):
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
        'acoustic_source_name': 'str',
        'pings': 'list[EchoSounderPing]',
        'installation': 'Installation'
    }

    attribute_map = {
        'acoustic_source_name': 'acoustic-source-name',
        'pings': 'pings',
        'installation': 'installation'
    }

    def __init__(self, acoustic_source_name=None, pings=None, installation=None):  # noqa: E501
        """EchoSounderTransducer - a model defined in Swagger"""  # noqa: E501

        self._acoustic_source_name = None
        self._pings = None
        self._installation = None
        self.discriminator = None

        if acoustic_source_name is not None:
            self.acoustic_source_name = acoustic_source_name
        if pings is not None:
            self.pings = pings
        if installation is not None:
            self.installation = installation

    @property
    def acoustic_source_name(self):
        """Gets the acoustic_source_name of this EchoSounderTransducer.  # noqa: E501


        :return: The acoustic_source_name of this EchoSounderTransducer.  # noqa: E501
        :rtype: str
        """
        return self._acoustic_source_name

    @acoustic_source_name.setter
    def acoustic_source_name(self, acoustic_source_name):
        """Sets the acoustic_source_name of this EchoSounderTransducer.


        :param acoustic_source_name: The acoustic_source_name of this EchoSounderTransducer.  # noqa: E501
        :type: str
        """

        self._acoustic_source_name = acoustic_source_name

    @property
    def pings(self):
        """Gets the pings of this EchoSounderTransducer.  # noqa: E501


        :return: The pings of this EchoSounderTransducer.  # noqa: E501
        :rtype: list[EchoSounderPing]
        """
        return self._pings

    @pings.setter
    def pings(self, pings):
        """Sets the pings of this EchoSounderTransducer.


        :param pings: The pings of this EchoSounderTransducer.  # noqa: E501
        :type: list[EchoSounderPing]
        """

        self._pings = pings

    @property
    def installation(self):
        """Gets the installation of this EchoSounderTransducer.  # noqa: E501


        :return: The installation of this EchoSounderTransducer.  # noqa: E501
        :rtype: Installation
        """
        return self._installation

    @installation.setter
    def installation(self, installation):
        """Sets the installation of this EchoSounderTransducer.


        :param installation: The installation of this EchoSounderTransducer.  # noqa: E501
        :type: Installation
        """

        self._installation = installation

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
        if issubclass(EchoSounderTransducer, dict):
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
        if not isinstance(other, EchoSounderTransducer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
