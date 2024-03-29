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


class AdcpConfigurationEc150(object):
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
        'ec150_mode': 'str',
        'depth_cell_size': 'int',
        'max_current_speed': 'float',
        'pulse_type': 'str',
        'ping_average': 'int'
    }

    attribute_map = {
        'ec150_mode': 'ec150-mode',
        'depth_cell_size': 'depth-cell-size',
        'max_current_speed': 'max-current-speed',
        'pulse_type': 'pulse-type',
        'ping_average': 'ping-average'
    }

    def __init__(self, ec150_mode=None, depth_cell_size=None, max_current_speed=None, pulse_type=None, ping_average=None):  # noqa: E501
        """AdcpConfigurationEc150 - a model defined in Swagger"""  # noqa: E501

        self._ec150_mode = None
        self._depth_cell_size = None
        self._max_current_speed = None
        self._pulse_type = None
        self._ping_average = None
        self.discriminator = None

        if ec150_mode is not None:
            self.ec150_mode = ec150_mode
        if depth_cell_size is not None:
            self.depth_cell_size = depth_cell_size
        if max_current_speed is not None:
            self.max_current_speed = max_current_speed
        if pulse_type is not None:
            self.pulse_type = pulse_type
        if ping_average is not None:
            self.ping_average = ping_average

    @property
    def ec150_mode(self):
        """Gets the ec150_mode of this AdcpConfigurationEc150.  # noqa: E501


        :return: The ec150_mode of this AdcpConfigurationEc150.  # noqa: E501
        :rtype: str
        """
        return self._ec150_mode

    @ec150_mode.setter
    def ec150_mode(self, ec150_mode):
        """Sets the ec150_mode of this AdcpConfigurationEc150.


        :param ec150_mode: The ec150_mode of this AdcpConfigurationEc150.  # noqa: E501
        :type: str
        """
        allowed_values = ["adcp", "echoSounder"]  # noqa: E501
        if ec150_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `ec150_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(ec150_mode, allowed_values)
            )

        self._ec150_mode = ec150_mode

    @property
    def depth_cell_size(self):
        """Gets the depth_cell_size of this AdcpConfigurationEc150.  # noqa: E501


        :return: The depth_cell_size of this AdcpConfigurationEc150.  # noqa: E501
        :rtype: int
        """
        return self._depth_cell_size

    @depth_cell_size.setter
    def depth_cell_size(self, depth_cell_size):
        """Sets the depth_cell_size of this AdcpConfigurationEc150.


        :param depth_cell_size: The depth_cell_size of this AdcpConfigurationEc150.  # noqa: E501
        :type: int
        """

        self._depth_cell_size = depth_cell_size

    @property
    def max_current_speed(self):
        """Gets the max_current_speed of this AdcpConfigurationEc150.  # noqa: E501


        :return: The max_current_speed of this AdcpConfigurationEc150.  # noqa: E501
        :rtype: float
        """
        return self._max_current_speed

    @max_current_speed.setter
    def max_current_speed(self, max_current_speed):
        """Sets the max_current_speed of this AdcpConfigurationEc150.


        :param max_current_speed: The max_current_speed of this AdcpConfigurationEc150.  # noqa: E501
        :type: float
        """

        self._max_current_speed = max_current_speed

    @property
    def pulse_type(self):
        """Gets the pulse_type of this AdcpConfigurationEc150.  # noqa: E501


        :return: The pulse_type of this AdcpConfigurationEc150.  # noqa: E501
        :rtype: str
        """
        return self._pulse_type

    @pulse_type.setter
    def pulse_type(self, pulse_type):
        """Sets the pulse_type of this AdcpConfigurationEc150.


        :param pulse_type: The pulse_type of this AdcpConfigurationEc150.  # noqa: E501
        :type: str
        """
        allowed_values = ["cw", "lfmUp"]  # noqa: E501
        if pulse_type not in allowed_values:
            raise ValueError(
                "Invalid value for `pulse_type` ({0}), must be one of {1}"  # noqa: E501
                .format(pulse_type, allowed_values)
            )

        self._pulse_type = pulse_type

    @property
    def ping_average(self):
        """Gets the ping_average of this AdcpConfigurationEc150.  # noqa: E501


        :return: The ping_average of this AdcpConfigurationEc150.  # noqa: E501
        :rtype: int
        """
        return self._ping_average

    @ping_average.setter
    def ping_average(self, ping_average):
        """Sets the ping_average of this AdcpConfigurationEc150.


        :param ping_average: The ping_average of this AdcpConfigurationEc150.  # noqa: E501
        :type: int
        """

        self._ping_average = ping_average

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
        if issubclass(AdcpConfigurationEc150, dict):
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
        if not isinstance(other, AdcpConfigurationEc150):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
