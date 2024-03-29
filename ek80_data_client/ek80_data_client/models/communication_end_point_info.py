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


class CommunicationEndPointInfo(object):
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
        'name': 'str',
        'configuration': 'str',
        'communication_type': 'str',
        'communication_end_point_id': 'int'
    }

    attribute_map = {
        'name': 'name',
        'configuration': 'configuration',
        'communication_type': 'communication-type',
        'communication_end_point_id': 'communication-end-point-id'
    }

    def __init__(self, name=None, configuration=None, communication_type=None, communication_end_point_id=None):  # noqa: E501
        """CommunicationEndPointInfo - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._configuration = None
        self._communication_type = None
        self._communication_end_point_id = None
        self.discriminator = None

        self.name = name
        self.configuration = configuration
        self.communication_type = communication_type
        self.communication_end_point_id = communication_end_point_id

    @property
    def name(self):
        """Gets the name of this CommunicationEndPointInfo.  # noqa: E501


        :return: The name of this CommunicationEndPointInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CommunicationEndPointInfo.


        :param name: The name of this CommunicationEndPointInfo.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def configuration(self):
        """Gets the configuration of this CommunicationEndPointInfo.  # noqa: E501


        :return: The configuration of this CommunicationEndPointInfo.  # noqa: E501
        :rtype: str
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """Sets the configuration of this CommunicationEndPointInfo.


        :param configuration: The configuration of this CommunicationEndPointInfo.  # noqa: E501
        :type: str
        """
        if configuration is None:
            raise ValueError("Invalid value for `configuration`, must not be `None`")  # noqa: E501

        self._configuration = configuration

    @property
    def communication_type(self):
        """Gets the communication_type of this CommunicationEndPointInfo.  # noqa: E501


        :return: The communication_type of this CommunicationEndPointInfo.  # noqa: E501
        :rtype: str
        """
        return self._communication_type

    @communication_type.setter
    def communication_type(self, communication_type):
        """Sets the communication_type of this CommunicationEndPointInfo.


        :param communication_type: The communication_type of this CommunicationEndPointInfo.  # noqa: E501
        :type: str
        """
        if communication_type is None:
            raise ValueError("Invalid value for `communication_type`, must not be `None`")  # noqa: E501
        allowed_values = ["zero-mq", "mq-tt", "grpc", "dds", "tcp", "udp"]  # noqa: E501
        if communication_type not in allowed_values:
            raise ValueError(
                "Invalid value for `communication_type` ({0}), must be one of {1}"  # noqa: E501
                .format(communication_type, allowed_values)
            )

        self._communication_type = communication_type

    @property
    def communication_end_point_id(self):
        """Gets the communication_end_point_id of this CommunicationEndPointInfo.  # noqa: E501


        :return: The communication_end_point_id of this CommunicationEndPointInfo.  # noqa: E501
        :rtype: int
        """
        return self._communication_end_point_id

    @communication_end_point_id.setter
    def communication_end_point_id(self, communication_end_point_id):
        """Sets the communication_end_point_id of this CommunicationEndPointInfo.


        :param communication_end_point_id: The communication_end_point_id of this CommunicationEndPointInfo.  # noqa: E501
        :type: int
        """
        if communication_end_point_id is None:
            raise ValueError("Invalid value for `communication_end_point_id`, must not be `None`")  # noqa: E501

        self._communication_end_point_id = communication_end_point_id

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
        if issubclass(CommunicationEndPointInfo, dict):
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
        if not isinstance(other, CommunicationEndPointInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
