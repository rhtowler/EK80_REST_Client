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


class EchogramSettings(object):
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
        'pixel_count': 'float',
        'range': 'float',
        'range_start': 'float',
        'tvg_function': 'float',
        'bottom_gain': 'float',
        'tvg_type': 'str',
        'bottom_tvg_type': 'str',
        'echogram_type': 'str',
        'compression_type': 'str',
        'expansion_type': 'str',
        'echogram_heave': 'int',
        'echogram_ping_filter_state': 'int',
        'echogram_min_pixel_value': 'float',
        'echogram_transducer_depth': 'int',
        'echogram_delay': 'int',
        'echogram_temporal_average': 'float',
        'echogram_stop_at_bottom': 'bool',
        'echogram_bottom_margin': 'float'
    }

    attribute_map = {
        'pixel_count': 'pixel-count',
        'range': 'range',
        'range_start': 'range-start',
        'tvg_function': 'tvg-function',
        'bottom_gain': 'bottom-gain',
        'tvg_type': 'tvg-type',
        'bottom_tvg_type': 'bottom-tvg-type',
        'echogram_type': 'echogram-type',
        'compression_type': 'compression-type',
        'expansion_type': 'expansion-type',
        'echogram_heave': 'echogram-heave',
        'echogram_ping_filter_state': 'echogram-ping-filter-state',
        'echogram_min_pixel_value': 'echogram-min-pixel-value',
        'echogram_transducer_depth': 'echogram-transducer-depth',
        'echogram_delay': 'echogram-delay',
        'echogram_temporal_average': 'echogram-temporal-average',
        'echogram_stop_at_bottom': 'echogram-stop-at-bottom',
        'echogram_bottom_margin': 'echogram-bottom-margin'
    }

    def __init__(self, pixel_count=500.0, range=100.0, range_start=0.0, tvg_function=20.0, bottom_gain=0.0, tvg_type='sv', bottom_tvg_type='none', echogram_type='surface', compression_type='mean', expansion_type='interpolate', echogram_heave=1, echogram_ping_filter_state=0, echogram_min_pixel_value=-100.0, echogram_transducer_depth=1, echogram_delay=1, echogram_temporal_average=-1.0, echogram_stop_at_bottom=False, echogram_bottom_margin=0.5):  # noqa: E501
        """EchogramSettings - a model defined in Swagger"""  # noqa: E501

        self._pixel_count = None
        self._range = None
        self._range_start = None
        self._tvg_function = None
        self._bottom_gain = None
        self._tvg_type = None
        self._bottom_tvg_type = None
        self._echogram_type = None
        self._compression_type = None
        self._expansion_type = None
        self._echogram_heave = None
        self._echogram_ping_filter_state = None
        self._echogram_min_pixel_value = None
        self._echogram_transducer_depth = None
        self._echogram_delay = None
        self._echogram_temporal_average = None
        self._echogram_stop_at_bottom = None
        self._echogram_bottom_margin = None
        self.discriminator = None

        self.pixel_count = pixel_count
        self.range = range
        if range_start is not None:
            self.range_start = range_start
        if tvg_function is not None:
            self.tvg_function = tvg_function
        if bottom_gain is not None:
            self.bottom_gain = bottom_gain
        if tvg_type is not None:
            self.tvg_type = tvg_type
        if bottom_tvg_type is not None:
            self.bottom_tvg_type = bottom_tvg_type
        if echogram_type is not None:
            self.echogram_type = echogram_type
        if compression_type is not None:
            self.compression_type = compression_type
        if expansion_type is not None:
            self.expansion_type = expansion_type
        if echogram_heave is not None:
            self.echogram_heave = echogram_heave
        if echogram_ping_filter_state is not None:
            self.echogram_ping_filter_state = echogram_ping_filter_state
        if echogram_min_pixel_value is not None:
            self.echogram_min_pixel_value = echogram_min_pixel_value
        if echogram_transducer_depth is not None:
            self.echogram_transducer_depth = echogram_transducer_depth
        if echogram_delay is not None:
            self.echogram_delay = echogram_delay
        if echogram_temporal_average is not None:
            self.echogram_temporal_average = echogram_temporal_average
        if echogram_stop_at_bottom is not None:
            self.echogram_stop_at_bottom = echogram_stop_at_bottom
        if echogram_bottom_margin is not None:
            self.echogram_bottom_margin = echogram_bottom_margin

    @property
    def pixel_count(self):
        """Gets the pixel_count of this EchogramSettings.  # noqa: E501


        :return: The pixel_count of this EchogramSettings.  # noqa: E501
        :rtype: float
        """
        return self._pixel_count

    @pixel_count.setter
    def pixel_count(self, pixel_count):
        """Sets the pixel_count of this EchogramSettings.


        :param pixel_count: The pixel_count of this EchogramSettings.  # noqa: E501
        :type: float
        """
        if pixel_count is None:
            raise ValueError("Invalid value for `pixel_count`, must not be `None`")  # noqa: E501
        if pixel_count is not None and pixel_count > 10000:  # noqa: E501
            raise ValueError("Invalid value for `pixel_count`, must be a value less than or equal to `10000`")  # noqa: E501
        if pixel_count is not None and pixel_count < 0:  # noqa: E501
            raise ValueError("Invalid value for `pixel_count`, must be a value greater than or equal to `0`")  # noqa: E501

        self._pixel_count = pixel_count

    @property
    def range(self):
        """Gets the range of this EchogramSettings.  # noqa: E501


        :return: The range of this EchogramSettings.  # noqa: E501
        :rtype: float
        """
        return self._range

    @range.setter
    def range(self, range):
        """Sets the range of this EchogramSettings.


        :param range: The range of this EchogramSettings.  # noqa: E501
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
        """Gets the range_start of this EchogramSettings.  # noqa: E501


        :return: The range_start of this EchogramSettings.  # noqa: E501
        :rtype: float
        """
        return self._range_start

    @range_start.setter
    def range_start(self, range_start):
        """Sets the range_start of this EchogramSettings.


        :param range_start: The range_start of this EchogramSettings.  # noqa: E501
        :type: float
        """
        if range_start is not None and range_start > 20000:  # noqa: E501
            raise ValueError("Invalid value for `range_start`, must be a value less than or equal to `20000`")  # noqa: E501
        if range_start is not None and range_start < -20000:  # noqa: E501
            raise ValueError("Invalid value for `range_start`, must be a value greater than or equal to `-20000`")  # noqa: E501

        self._range_start = range_start

    @property
    def tvg_function(self):
        """Gets the tvg_function of this EchogramSettings.  # noqa: E501


        :return: The tvg_function of this EchogramSettings.  # noqa: E501
        :rtype: float
        """
        return self._tvg_function

    @tvg_function.setter
    def tvg_function(self, tvg_function):
        """Sets the tvg_function of this EchogramSettings.


        :param tvg_function: The tvg_function of this EchogramSettings.  # noqa: E501
        :type: float
        """
        if tvg_function is not None and tvg_function > 100:  # noqa: E501
            raise ValueError("Invalid value for `tvg_function`, must be a value less than or equal to `100`")  # noqa: E501
        if tvg_function is not None and tvg_function < 0:  # noqa: E501
            raise ValueError("Invalid value for `tvg_function`, must be a value greater than or equal to `0`")  # noqa: E501

        self._tvg_function = tvg_function

    @property
    def bottom_gain(self):
        """Gets the bottom_gain of this EchogramSettings.  # noqa: E501


        :return: The bottom_gain of this EchogramSettings.  # noqa: E501
        :rtype: float
        """
        return self._bottom_gain

    @bottom_gain.setter
    def bottom_gain(self, bottom_gain):
        """Sets the bottom_gain of this EchogramSettings.


        :param bottom_gain: The bottom_gain of this EchogramSettings.  # noqa: E501
        :type: float
        """
        if bottom_gain is not None and bottom_gain > 100:  # noqa: E501
            raise ValueError("Invalid value for `bottom_gain`, must be a value less than or equal to `100`")  # noqa: E501
        if bottom_gain is not None and bottom_gain < -100:  # noqa: E501
            raise ValueError("Invalid value for `bottom_gain`, must be a value greater than or equal to `-100`")  # noqa: E501

        self._bottom_gain = bottom_gain

    @property
    def tvg_type(self):
        """Gets the tvg_type of this EchogramSettings.  # noqa: E501


        :return: The tvg_type of this EchogramSettings.  # noqa: E501
        :rtype: str
        """
        return self._tvg_type

    @tvg_type.setter
    def tvg_type(self, tvg_type):
        """Sets the tvg_type of this EchogramSettings.


        :param tvg_type: The tvg_type of this EchogramSettings.  # noqa: E501
        :type: str
        """
        allowed_values = ["sv", "pr", "sp", "ts", "ss", "sp-and-ts", "user", "s-process-chain"]  # noqa: E501
        if tvg_type not in allowed_values:
            raise ValueError(
                "Invalid value for `tvg_type` ({0}), must be one of {1}"  # noqa: E501
                .format(tvg_type, allowed_values)
            )

        self._tvg_type = tvg_type

    @property
    def bottom_tvg_type(self):
        """Gets the bottom_tvg_type of this EchogramSettings.  # noqa: E501


        :return: The bottom_tvg_type of this EchogramSettings.  # noqa: E501
        :rtype: str
        """
        return self._bottom_tvg_type

    @bottom_tvg_type.setter
    def bottom_tvg_type(self, bottom_tvg_type):
        """Sets the bottom_tvg_type of this EchogramSettings.


        :param bottom_tvg_type: The bottom_tvg_type of this EchogramSettings.  # noqa: E501
        :type: str
        """
        allowed_values = ["none", "sv", "ts", "user"]  # noqa: E501
        if bottom_tvg_type not in allowed_values:
            raise ValueError(
                "Invalid value for `bottom_tvg_type` ({0}), must be one of {1}"  # noqa: E501
                .format(bottom_tvg_type, allowed_values)
            )

        self._bottom_tvg_type = bottom_tvg_type

    @property
    def echogram_type(self):
        """Gets the echogram_type of this EchogramSettings.  # noqa: E501


        :return: The echogram_type of this EchogramSettings.  # noqa: E501
        :rtype: str
        """
        return self._echogram_type

    @echogram_type.setter
    def echogram_type(self, echogram_type):
        """Sets the echogram_type of this EchogramSettings.


        :param echogram_type: The echogram_type of this EchogramSettings.  # noqa: E501
        :type: str
        """
        allowed_values = ["surface", "bottom", "trawl"]  # noqa: E501
        if echogram_type not in allowed_values:
            raise ValueError(
                "Invalid value for `echogram_type` ({0}), must be one of {1}"  # noqa: E501
                .format(echogram_type, allowed_values)
            )

        self._echogram_type = echogram_type

    @property
    def compression_type(self):
        """Gets the compression_type of this EchogramSettings.  # noqa: E501


        :return: The compression_type of this EchogramSettings.  # noqa: E501
        :rtype: str
        """
        return self._compression_type

    @compression_type.setter
    def compression_type(self, compression_type):
        """Sets the compression_type of this EchogramSettings.


        :param compression_type: The compression_type of this EchogramSettings.  # noqa: E501
        :type: str
        """
        allowed_values = ["mean", "peak"]  # noqa: E501
        if compression_type not in allowed_values:
            raise ValueError(
                "Invalid value for `compression_type` ({0}), must be one of {1}"  # noqa: E501
                .format(compression_type, allowed_values)
            )

        self._compression_type = compression_type

    @property
    def expansion_type(self):
        """Gets the expansion_type of this EchogramSettings.  # noqa: E501


        :return: The expansion_type of this EchogramSettings.  # noqa: E501
        :rtype: str
        """
        return self._expansion_type

    @expansion_type.setter
    def expansion_type(self, expansion_type):
        """Sets the expansion_type of this EchogramSettings.


        :param expansion_type: The expansion_type of this EchogramSettings.  # noqa: E501
        :type: str
        """
        allowed_values = ["interpolate", "copy"]  # noqa: E501
        if expansion_type not in allowed_values:
            raise ValueError(
                "Invalid value for `expansion_type` ({0}), must be one of {1}"  # noqa: E501
                .format(expansion_type, allowed_values)
            )

        self._expansion_type = expansion_type

    @property
    def echogram_heave(self):
        """Gets the echogram_heave of this EchogramSettings.  # noqa: E501


        :return: The echogram_heave of this EchogramSettings.  # noqa: E501
        :rtype: int
        """
        return self._echogram_heave

    @echogram_heave.setter
    def echogram_heave(self, echogram_heave):
        """Sets the echogram_heave of this EchogramSettings.


        :param echogram_heave: The echogram_heave of this EchogramSettings.  # noqa: E501
        :type: int
        """
        if echogram_heave is not None and echogram_heave > 1:  # noqa: E501
            raise ValueError("Invalid value for `echogram_heave`, must be a value less than or equal to `1`")  # noqa: E501
        if echogram_heave is not None and echogram_heave < 0:  # noqa: E501
            raise ValueError("Invalid value for `echogram_heave`, must be a value greater than or equal to `0`")  # noqa: E501

        self._echogram_heave = echogram_heave

    @property
    def echogram_ping_filter_state(self):
        """Gets the echogram_ping_filter_state of this EchogramSettings.  # noqa: E501


        :return: The echogram_ping_filter_state of this EchogramSettings.  # noqa: E501
        :rtype: int
        """
        return self._echogram_ping_filter_state

    @echogram_ping_filter_state.setter
    def echogram_ping_filter_state(self, echogram_ping_filter_state):
        """Sets the echogram_ping_filter_state of this EchogramSettings.


        :param echogram_ping_filter_state: The echogram_ping_filter_state of this EchogramSettings.  # noqa: E501
        :type: int
        """
        if echogram_ping_filter_state is not None and echogram_ping_filter_state > 3:  # noqa: E501
            raise ValueError("Invalid value for `echogram_ping_filter_state`, must be a value less than or equal to `3`")  # noqa: E501
        if echogram_ping_filter_state is not None and echogram_ping_filter_state < 0:  # noqa: E501
            raise ValueError("Invalid value for `echogram_ping_filter_state`, must be a value greater than or equal to `0`")  # noqa: E501

        self._echogram_ping_filter_state = echogram_ping_filter_state

    @property
    def echogram_min_pixel_value(self):
        """Gets the echogram_min_pixel_value of this EchogramSettings.  # noqa: E501


        :return: The echogram_min_pixel_value of this EchogramSettings.  # noqa: E501
        :rtype: float
        """
        return self._echogram_min_pixel_value

    @echogram_min_pixel_value.setter
    def echogram_min_pixel_value(self, echogram_min_pixel_value):
        """Sets the echogram_min_pixel_value of this EchogramSettings.


        :param echogram_min_pixel_value: The echogram_min_pixel_value of this EchogramSettings.  # noqa: E501
        :type: float
        """
        if echogram_min_pixel_value is not None and echogram_min_pixel_value > 100:  # noqa: E501
            raise ValueError("Invalid value for `echogram_min_pixel_value`, must be a value less than or equal to `100`")  # noqa: E501
        if echogram_min_pixel_value is not None and echogram_min_pixel_value < -200:  # noqa: E501
            raise ValueError("Invalid value for `echogram_min_pixel_value`, must be a value greater than or equal to `-200`")  # noqa: E501

        self._echogram_min_pixel_value = echogram_min_pixel_value

    @property
    def echogram_transducer_depth(self):
        """Gets the echogram_transducer_depth of this EchogramSettings.  # noqa: E501


        :return: The echogram_transducer_depth of this EchogramSettings.  # noqa: E501
        :rtype: int
        """
        return self._echogram_transducer_depth

    @echogram_transducer_depth.setter
    def echogram_transducer_depth(self, echogram_transducer_depth):
        """Sets the echogram_transducer_depth of this EchogramSettings.


        :param echogram_transducer_depth: The echogram_transducer_depth of this EchogramSettings.  # noqa: E501
        :type: int
        """
        if echogram_transducer_depth is not None and echogram_transducer_depth > 1:  # noqa: E501
            raise ValueError("Invalid value for `echogram_transducer_depth`, must be a value less than or equal to `1`")  # noqa: E501
        if echogram_transducer_depth is not None and echogram_transducer_depth < 0:  # noqa: E501
            raise ValueError("Invalid value for `echogram_transducer_depth`, must be a value greater than or equal to `0`")  # noqa: E501

        self._echogram_transducer_depth = echogram_transducer_depth

    @property
    def echogram_delay(self):
        """Gets the echogram_delay of this EchogramSettings.  # noqa: E501


        :return: The echogram_delay of this EchogramSettings.  # noqa: E501
        :rtype: int
        """
        return self._echogram_delay

    @echogram_delay.setter
    def echogram_delay(self, echogram_delay):
        """Sets the echogram_delay of this EchogramSettings.


        :param echogram_delay: The echogram_delay of this EchogramSettings.  # noqa: E501
        :type: int
        """
        if echogram_delay is not None and echogram_delay > 1:  # noqa: E501
            raise ValueError("Invalid value for `echogram_delay`, must be a value less than or equal to `1`")  # noqa: E501
        if echogram_delay is not None and echogram_delay < 0:  # noqa: E501
            raise ValueError("Invalid value for `echogram_delay`, must be a value greater than or equal to `0`")  # noqa: E501

        self._echogram_delay = echogram_delay

    @property
    def echogram_temporal_average(self):
        """Gets the echogram_temporal_average of this EchogramSettings.  # noqa: E501


        :return: The echogram_temporal_average of this EchogramSettings.  # noqa: E501
        :rtype: float
        """
        return self._echogram_temporal_average

    @echogram_temporal_average.setter
    def echogram_temporal_average(self, echogram_temporal_average):
        """Sets the echogram_temporal_average of this EchogramSettings.


        :param echogram_temporal_average: The echogram_temporal_average of this EchogramSettings.  # noqa: E501
        :type: float
        """
        if echogram_temporal_average is not None and echogram_temporal_average > 20:  # noqa: E501
            raise ValueError("Invalid value for `echogram_temporal_average`, must be a value less than or equal to `20`")  # noqa: E501
        if echogram_temporal_average is not None and echogram_temporal_average < -2:  # noqa: E501
            raise ValueError("Invalid value for `echogram_temporal_average`, must be a value greater than or equal to `-2`")  # noqa: E501

        self._echogram_temporal_average = echogram_temporal_average

    @property
    def echogram_stop_at_bottom(self):
        """Gets the echogram_stop_at_bottom of this EchogramSettings.  # noqa: E501


        :return: The echogram_stop_at_bottom of this EchogramSettings.  # noqa: E501
        :rtype: bool
        """
        return self._echogram_stop_at_bottom

    @echogram_stop_at_bottom.setter
    def echogram_stop_at_bottom(self, echogram_stop_at_bottom):
        """Sets the echogram_stop_at_bottom of this EchogramSettings.


        :param echogram_stop_at_bottom: The echogram_stop_at_bottom of this EchogramSettings.  # noqa: E501
        :type: bool
        """

        self._echogram_stop_at_bottom = echogram_stop_at_bottom

    @property
    def echogram_bottom_margin(self):
        """Gets the echogram_bottom_margin of this EchogramSettings.  # noqa: E501


        :return: The echogram_bottom_margin of this EchogramSettings.  # noqa: E501
        :rtype: float
        """
        return self._echogram_bottom_margin

    @echogram_bottom_margin.setter
    def echogram_bottom_margin(self, echogram_bottom_margin):
        """Sets the echogram_bottom_margin of this EchogramSettings.


        :param echogram_bottom_margin: The echogram_bottom_margin of this EchogramSettings.  # noqa: E501
        :type: float
        """
        if echogram_bottom_margin is not None and echogram_bottom_margin > 20:  # noqa: E501
            raise ValueError("Invalid value for `echogram_bottom_margin`, must be a value less than or equal to `20`")  # noqa: E501
        if echogram_bottom_margin is not None and echogram_bottom_margin < -10:  # noqa: E501
            raise ValueError("Invalid value for `echogram_bottom_margin`, must be a value greater than or equal to `-10`")  # noqa: E501

        self._echogram_bottom_margin = echogram_bottom_margin

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
        if issubclass(EchogramSettings, dict):
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
        if not isinstance(other, EchogramSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
