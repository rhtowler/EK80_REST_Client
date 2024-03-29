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


class OctopusPingParameters(object):
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
        'max_vessel_speed': 'float',
        'max_current_speed': 'float',
        'depth_cell_size': 'float',
        'auto_depth_cell_size': 'bool'
    }

    attribute_map = {
        'max_vessel_speed': 'max-vessel-speed',
        'max_current_speed': 'max-current-speed',
        'depth_cell_size': 'depth-cell-size',
        'auto_depth_cell_size': 'auto-depth-cell-size'
    }

    def __init__(self, max_vessel_speed=None, max_current_speed=None, depth_cell_size=None, auto_depth_cell_size=None):  # noqa: E501
        """OctopusPingParameters - a model defined in Swagger"""  # noqa: E501

        self._max_vessel_speed = None
        self._max_current_speed = None
        self._depth_cell_size = None
        self._auto_depth_cell_size = None
        self.discriminator = None

        if max_vessel_speed is not None:
            self.max_vessel_speed = max_vessel_speed
        if max_current_speed is not None:
            self.max_current_speed = max_current_speed
        if depth_cell_size is not None:
            self.depth_cell_size = depth_cell_size
        if auto_depth_cell_size is not None:
            self.auto_depth_cell_size = auto_depth_cell_size

    @property
    def max_vessel_speed(self):
        """Gets the max_vessel_speed of this OctopusPingParameters.  # noqa: E501


        :return: The max_vessel_speed of this OctopusPingParameters.  # noqa: E501
        :rtype: float
        """
        return self._max_vessel_speed

    @max_vessel_speed.setter
    def max_vessel_speed(self, max_vessel_speed):
        """Sets the max_vessel_speed of this OctopusPingParameters.


        :param max_vessel_speed: The max_vessel_speed of this OctopusPingParameters.  # noqa: E501
        :type: float
        """

        self._max_vessel_speed = max_vessel_speed

    @property
    def max_current_speed(self):
        """Gets the max_current_speed of this OctopusPingParameters.  # noqa: E501


        :return: The max_current_speed of this OctopusPingParameters.  # noqa: E501
        :rtype: float
        """
        return self._max_current_speed

    @max_current_speed.setter
    def max_current_speed(self, max_current_speed):
        """Sets the max_current_speed of this OctopusPingParameters.


        :param max_current_speed: The max_current_speed of this OctopusPingParameters.  # noqa: E501
        :type: float
        """

        self._max_current_speed = max_current_speed

    @property
    def depth_cell_size(self):
        """Gets the depth_cell_size of this OctopusPingParameters.  # noqa: E501


        :return: The depth_cell_size of this OctopusPingParameters.  # noqa: E501
        :rtype: float
        """
        return self._depth_cell_size

    @depth_cell_size.setter
    def depth_cell_size(self, depth_cell_size):
        """Sets the depth_cell_size of this OctopusPingParameters.


        :param depth_cell_size: The depth_cell_size of this OctopusPingParameters.  # noqa: E501
        :type: float
        """

        self._depth_cell_size = depth_cell_size

    @property
    def auto_depth_cell_size(self):
        """Gets the auto_depth_cell_size of this OctopusPingParameters.  # noqa: E501


        :return: The auto_depth_cell_size of this OctopusPingParameters.  # noqa: E501
        :rtype: bool
        """
        return self._auto_depth_cell_size

    @auto_depth_cell_size.setter
    def auto_depth_cell_size(self, auto_depth_cell_size):
        """Sets the auto_depth_cell_size of this OctopusPingParameters.


        :param auto_depth_cell_size: The auto_depth_cell_size of this OctopusPingParameters.  # noqa: E501
        :type: bool
        """

        self._auto_depth_cell_size = auto_depth_cell_size

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
        if issubclass(OctopusPingParameters, dict):
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
        if not isinstance(other, OctopusPingParameters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
