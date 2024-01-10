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


class AdcpQualitySettings(object):
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
        'range': 'float',
        'range_start': 'float',
        'stop_at_bottom': 'str',
        'quality_factor_average': 'bool',
        'use_heave_adjustment': 'bool'
    }

    attribute_map = {
        'range': 'range',
        'range_start': 'range-start',
        'stop_at_bottom': 'stop-at-bottom',
        'quality_factor_average': 'quality-factor-average',
        'use_heave_adjustment': 'use-heave-adjustment'
    }

    def __init__(self, range=None, range_start=0.0, stop_at_bottom='full', quality_factor_average=False, use_heave_adjustment=True):  # noqa: E501
        """AdcpQualitySettings - a model defined in Swagger"""  # noqa: E501

        self._range = None
        self._range_start = None
        self._stop_at_bottom = None
        self._quality_factor_average = None
        self._use_heave_adjustment = None
        self.discriminator = None

        self.range = range
        if range_start is not None:
            self.range_start = range_start
        if stop_at_bottom is not None:
            self.stop_at_bottom = stop_at_bottom
        if quality_factor_average is not None:
            self.quality_factor_average = quality_factor_average
        if use_heave_adjustment is not None:
            self.use_heave_adjustment = use_heave_adjustment

    @property
    def range(self):
        """Gets the range of this AdcpQualitySettings.  # noqa: E501


        :return: The range of this AdcpQualitySettings.  # noqa: E501
        :rtype: float
        """
        return self._range

    @range.setter
    def range(self, range):
        """Sets the range of this AdcpQualitySettings.


        :param range: The range of this AdcpQualitySettings.  # noqa: E501
        :type: float
        """
        if range is None:
            raise ValueError("Invalid value for `range`, must not be `None`")  # noqa: E501
        if range is not None and range > 20000:  # noqa: E501
            raise ValueError("Invalid value for `range`, must be a value less than or equal to `20000`")  # noqa: E501

        self._range = range

    @property
    def range_start(self):
        """Gets the range_start of this AdcpQualitySettings.  # noqa: E501


        :return: The range_start of this AdcpQualitySettings.  # noqa: E501
        :rtype: float
        """
        return self._range_start

    @range_start.setter
    def range_start(self, range_start):
        """Sets the range_start of this AdcpQualitySettings.


        :param range_start: The range_start of this AdcpQualitySettings.  # noqa: E501
        :type: float
        """
        if range_start is not None and range_start > 20000:  # noqa: E501
            raise ValueError("Invalid value for `range_start`, must be a value less than or equal to `20000`")  # noqa: E501
        if range_start is not None and range_start < -20000:  # noqa: E501
            raise ValueError("Invalid value for `range_start`, must be a value greater than or equal to `-20000`")  # noqa: E501

        self._range_start = range_start

    @property
    def stop_at_bottom(self):
        """Gets the stop_at_bottom of this AdcpQualitySettings.  # noqa: E501


        :return: The stop_at_bottom of this AdcpQualitySettings.  # noqa: E501
        :rtype: str
        """
        return self._stop_at_bottom

    @stop_at_bottom.setter
    def stop_at_bottom(self, stop_at_bottom):
        """Sets the stop_at_bottom of this AdcpQualitySettings.


        :param stop_at_bottom: The stop_at_bottom of this AdcpQualitySettings.  # noqa: E501
        :type: str
        """
        allowed_values = ["full", "first-hit", "last-hit"]  # noqa: E501
        if stop_at_bottom not in allowed_values:
            raise ValueError(
                "Invalid value for `stop_at_bottom` ({0}), must be one of {1}"  # noqa: E501
                .format(stop_at_bottom, allowed_values)
            )

        self._stop_at_bottom = stop_at_bottom

    @property
    def quality_factor_average(self):
        """Gets the quality_factor_average of this AdcpQualitySettings.  # noqa: E501


        :return: The quality_factor_average of this AdcpQualitySettings.  # noqa: E501
        :rtype: bool
        """
        return self._quality_factor_average

    @quality_factor_average.setter
    def quality_factor_average(self, quality_factor_average):
        """Sets the quality_factor_average of this AdcpQualitySettings.


        :param quality_factor_average: The quality_factor_average of this AdcpQualitySettings.  # noqa: E501
        :type: bool
        """

        self._quality_factor_average = quality_factor_average

    @property
    def use_heave_adjustment(self):
        """Gets the use_heave_adjustment of this AdcpQualitySettings.  # noqa: E501


        :return: The use_heave_adjustment of this AdcpQualitySettings.  # noqa: E501
        :rtype: bool
        """
        return self._use_heave_adjustment

    @use_heave_adjustment.setter
    def use_heave_adjustment(self, use_heave_adjustment):
        """Sets the use_heave_adjustment of this AdcpQualitySettings.


        :param use_heave_adjustment: The use_heave_adjustment of this AdcpQualitySettings.  # noqa: E501
        :type: bool
        """

        self._use_heave_adjustment = use_heave_adjustment

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
        if issubclass(AdcpQualitySettings, dict):
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
        if not isinstance(other, AdcpQualitySettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
