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


class TsDetectionSettings(object):
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
        'layer_type': 'str',
        'min_ts_value': 'float',
        'min_echo_length': 'float',
        'max_echo_length': 'float',
        'min_spacing': 'float',
        'max_phase_deviation': 'float',
        'max_gain_compensation': 'float',
        'format_type': 'str'
    }

    attribute_map = {
        'range': 'range',
        'range_start': 'range-start',
        'layer_type': 'layer-type',
        'min_ts_value': 'min-ts-value',
        'min_echo_length': 'min-echo-length',
        'max_echo_length': 'max-echo-length',
        'min_spacing': 'min-spacing',
        'max_phase_deviation': 'max-phase-deviation',
        'max_gain_compensation': 'max-gain-compensation',
        'format_type': 'format-type'
    }

    def __init__(self, range=1000.0, range_start=0.0, layer_type='surface', min_ts_value=-50.0, min_echo_length=0.8, max_echo_length=1.8, min_spacing=0.0, max_phase_deviation=20.0, max_gain_compensation=3.0, format_type='EK60'):  # noqa: E501
        """TsDetectionSettings - a model defined in Swagger"""  # noqa: E501

        self._range = None
        self._range_start = None
        self._layer_type = None
        self._min_ts_value = None
        self._min_echo_length = None
        self._max_echo_length = None
        self._min_spacing = None
        self._max_phase_deviation = None
        self._max_gain_compensation = None
        self._format_type = None
        self.discriminator = None

        self.range = range
        self.range_start = range_start
        if layer_type is not None:
            self.layer_type = layer_type
        if min_ts_value is not None:
            self.min_ts_value = min_ts_value
        if min_echo_length is not None:
            self.min_echo_length = min_echo_length
        if max_echo_length is not None:
            self.max_echo_length = max_echo_length
        if min_spacing is not None:
            self.min_spacing = min_spacing
        if max_phase_deviation is not None:
            self.max_phase_deviation = max_phase_deviation
        if max_gain_compensation is not None:
            self.max_gain_compensation = max_gain_compensation
        if format_type is not None:
            self.format_type = format_type

    @property
    def range(self):
        """Gets the range of this TsDetectionSettings.  # noqa: E501


        :return: The range of this TsDetectionSettings.  # noqa: E501
        :rtype: float
        """
        return self._range

    @range.setter
    def range(self, range):
        """Sets the range of this TsDetectionSettings.


        :param range: The range of this TsDetectionSettings.  # noqa: E501
        :type: float
        """
        if range is None:
            raise ValueError("Invalid value for `range`, must not be `None`")  # noqa: E501
        if range is not None and range > 20000:  # noqa: E501
            raise ValueError("Invalid value for `range`, must be a value less than or equal to `20000`")  # noqa: E501
        if range is not None and range < 0:  # noqa: E501
            raise ValueError("Invalid value for `range`, must be a value greater than or equal to `0`")  # noqa: E501

        self._range = range

    @property
    def range_start(self):
        """Gets the range_start of this TsDetectionSettings.  # noqa: E501


        :return: The range_start of this TsDetectionSettings.  # noqa: E501
        :rtype: float
        """
        return self._range_start

    @range_start.setter
    def range_start(self, range_start):
        """Sets the range_start of this TsDetectionSettings.


        :param range_start: The range_start of this TsDetectionSettings.  # noqa: E501
        :type: float
        """
        if range_start is None:
            raise ValueError("Invalid value for `range_start`, must not be `None`")  # noqa: E501
        if range_start is not None and range_start > 20000:  # noqa: E501
            raise ValueError("Invalid value for `range_start`, must be a value less than or equal to `20000`")  # noqa: E501
        if range_start is not None and range_start < -20000:  # noqa: E501
            raise ValueError("Invalid value for `range_start`, must be a value greater than or equal to `-20000`")  # noqa: E501

        self._range_start = range_start

    @property
    def layer_type(self):
        """Gets the layer_type of this TsDetectionSettings.  # noqa: E501


        :return: The layer_type of this TsDetectionSettings.  # noqa: E501
        :rtype: str
        """
        return self._layer_type

    @layer_type.setter
    def layer_type(self, layer_type):
        """Sets the layer_type of this TsDetectionSettings.


        :param layer_type: The layer_type of this TsDetectionSettings.  # noqa: E501
        :type: str
        """
        allowed_values = ["surface", "bottom", "pelagic"]  # noqa: E501
        if layer_type not in allowed_values:
            raise ValueError(
                "Invalid value for `layer_type` ({0}), must be one of {1}"  # noqa: E501
                .format(layer_type, allowed_values)
            )

        self._layer_type = layer_type

    @property
    def min_ts_value(self):
        """Gets the min_ts_value of this TsDetectionSettings.  # noqa: E501


        :return: The min_ts_value of this TsDetectionSettings.  # noqa: E501
        :rtype: float
        """
        return self._min_ts_value

    @min_ts_value.setter
    def min_ts_value(self, min_ts_value):
        """Sets the min_ts_value of this TsDetectionSettings.


        :param min_ts_value: The min_ts_value of this TsDetectionSettings.  # noqa: E501
        :type: float
        """
        if min_ts_value is not None and min_ts_value > 50:  # noqa: E501
            raise ValueError("Invalid value for `min_ts_value`, must be a value less than or equal to `50`")  # noqa: E501
        if min_ts_value is not None and min_ts_value < -150:  # noqa: E501
            raise ValueError("Invalid value for `min_ts_value`, must be a value greater than or equal to `-150`")  # noqa: E501

        self._min_ts_value = min_ts_value

    @property
    def min_echo_length(self):
        """Gets the min_echo_length of this TsDetectionSettings.  # noqa: E501


        :return: The min_echo_length of this TsDetectionSettings.  # noqa: E501
        :rtype: float
        """
        return self._min_echo_length

    @min_echo_length.setter
    def min_echo_length(self, min_echo_length):
        """Sets the min_echo_length of this TsDetectionSettings.


        :param min_echo_length: The min_echo_length of this TsDetectionSettings.  # noqa: E501
        :type: float
        """
        if min_echo_length is not None and min_echo_length > 20:  # noqa: E501
            raise ValueError("Invalid value for `min_echo_length`, must be a value less than or equal to `20`")  # noqa: E501
        if min_echo_length is not None and min_echo_length < 0:  # noqa: E501
            raise ValueError("Invalid value for `min_echo_length`, must be a value greater than or equal to `0`")  # noqa: E501

        self._min_echo_length = min_echo_length

    @property
    def max_echo_length(self):
        """Gets the max_echo_length of this TsDetectionSettings.  # noqa: E501


        :return: The max_echo_length of this TsDetectionSettings.  # noqa: E501
        :rtype: float
        """
        return self._max_echo_length

    @max_echo_length.setter
    def max_echo_length(self, max_echo_length):
        """Sets the max_echo_length of this TsDetectionSettings.


        :param max_echo_length: The max_echo_length of this TsDetectionSettings.  # noqa: E501
        :type: float
        """
        if max_echo_length is not None and max_echo_length > 20:  # noqa: E501
            raise ValueError("Invalid value for `max_echo_length`, must be a value less than or equal to `20`")  # noqa: E501
        if max_echo_length is not None and max_echo_length < 0:  # noqa: E501
            raise ValueError("Invalid value for `max_echo_length`, must be a value greater than or equal to `0`")  # noqa: E501

        self._max_echo_length = max_echo_length

    @property
    def min_spacing(self):
        """Gets the min_spacing of this TsDetectionSettings.  # noqa: E501


        :return: The min_spacing of this TsDetectionSettings.  # noqa: E501
        :rtype: float
        """
        return self._min_spacing

    @min_spacing.setter
    def min_spacing(self, min_spacing):
        """Sets the min_spacing of this TsDetectionSettings.


        :param min_spacing: The min_spacing of this TsDetectionSettings.  # noqa: E501
        :type: float
        """
        if min_spacing is not None and min_spacing > 12:  # noqa: E501
            raise ValueError("Invalid value for `min_spacing`, must be a value less than or equal to `12`")  # noqa: E501
        if min_spacing is not None and min_spacing < 0:  # noqa: E501
            raise ValueError("Invalid value for `min_spacing`, must be a value greater than or equal to `0`")  # noqa: E501

        self._min_spacing = min_spacing

    @property
    def max_phase_deviation(self):
        """Gets the max_phase_deviation of this TsDetectionSettings.  # noqa: E501


        :return: The max_phase_deviation of this TsDetectionSettings.  # noqa: E501
        :rtype: float
        """
        return self._max_phase_deviation

    @max_phase_deviation.setter
    def max_phase_deviation(self, max_phase_deviation):
        """Sets the max_phase_deviation of this TsDetectionSettings.


        :param max_phase_deviation: The max_phase_deviation of this TsDetectionSettings.  # noqa: E501
        :type: float
        """
        if max_phase_deviation is not None and max_phase_deviation > 100:  # noqa: E501
            raise ValueError("Invalid value for `max_phase_deviation`, must be a value less than or equal to `100`")  # noqa: E501
        if max_phase_deviation is not None and max_phase_deviation < 0:  # noqa: E501
            raise ValueError("Invalid value for `max_phase_deviation`, must be a value greater than or equal to `0`")  # noqa: E501

        self._max_phase_deviation = max_phase_deviation

    @property
    def max_gain_compensation(self):
        """Gets the max_gain_compensation of this TsDetectionSettings.  # noqa: E501


        :return: The max_gain_compensation of this TsDetectionSettings.  # noqa: E501
        :rtype: float
        """
        return self._max_gain_compensation

    @max_gain_compensation.setter
    def max_gain_compensation(self, max_gain_compensation):
        """Sets the max_gain_compensation of this TsDetectionSettings.


        :param max_gain_compensation: The max_gain_compensation of this TsDetectionSettings.  # noqa: E501
        :type: float
        """
        if max_gain_compensation is not None and max_gain_compensation > 12:  # noqa: E501
            raise ValueError("Invalid value for `max_gain_compensation`, must be a value less than or equal to `12`")  # noqa: E501
        if max_gain_compensation is not None and max_gain_compensation < 0:  # noqa: E501
            raise ValueError("Invalid value for `max_gain_compensation`, must be a value greater than or equal to `0`")  # noqa: E501

        self._max_gain_compensation = max_gain_compensation

    @property
    def format_type(self):
        """Gets the format_type of this TsDetectionSettings.  # noqa: E501


        :return: The format_type of this TsDetectionSettings.  # noqa: E501
        :rtype: str
        """
        return self._format_type

    @format_type.setter
    def format_type(self, format_type):
        """Sets the format_type of this TsDetectionSettings.


        :param format_type: The format_type of this TsDetectionSettings.  # noqa: E501
        :type: str
        """
        allowed_values = ["EK60", "EK500", "HAC"]  # noqa: E501
        if format_type not in allowed_values:
            raise ValueError(
                "Invalid value for `format_type` ({0}), must be one of {1}"  # noqa: E501
                .format(format_type, allowed_values)
            )

        self._format_type = format_type

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
        if issubclass(TsDetectionSettings, dict):
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
        if not isinstance(other, TsDetectionSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
