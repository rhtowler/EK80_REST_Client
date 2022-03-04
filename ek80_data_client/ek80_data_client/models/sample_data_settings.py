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


class SampleDataSettings(object):
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
        'sample_data_type': 'str',
        'range': 'float',
        'range_start': 'float',
        'auto_range': 'bool',
        'sample_data_heave': 'int',
        'sample_transducer_depth': 'int',
        'sample_data_delay': 'int',
        'adcp_sub_feature': 'str',
        'function': 'str'
    }

    attribute_map = {
        'sample_data_type': 'sample-data-type',
        'range': 'range',
        'range_start': 'range-start',
        'auto_range': 'auto-range',
        'sample_data_heave': 'sample-data-heave',
        'sample_transducer_depth': 'sample-transducer-depth',
        'sample_data_delay': 'sample-data-delay',
        'adcp_sub_feature': 'adcp-sub-feature',
        'function': 'function'
    }

    def __init__(self, sample_data_type=None, range=500.0, range_start=10.0, auto_range=False, sample_data_heave=1, sample_transducer_depth=1, sample_data_delay=1, adcp_sub_feature=None, function=None):  # noqa: E501
        """SampleDataSettings - a model defined in Swagger"""  # noqa: E501

        self._sample_data_type = None
        self._range = None
        self._range_start = None
        self._auto_range = None
        self._sample_data_heave = None
        self._sample_transducer_depth = None
        self._sample_data_delay = None
        self._adcp_sub_feature = None
        self._function = None
        self.discriminator = None

        self.sample_data_type = sample_data_type
        self.range = range
        if range_start is not None:
            self.range_start = range_start
        if auto_range is not None:
            self.auto_range = auto_range
        if sample_data_heave is not None:
            self.sample_data_heave = sample_data_heave
        if sample_transducer_depth is not None:
            self.sample_transducer_depth = sample_transducer_depth
        if sample_data_delay is not None:
            self.sample_data_delay = sample_data_delay
        if adcp_sub_feature is not None:
            self.adcp_sub_feature = adcp_sub_feature
        if function is not None:
            self.function = function

    @property
    def sample_data_type(self):
        """Gets the sample_data_type of this SampleDataSettings.  # noqa: E501


        :return: The sample_data_type of this SampleDataSettings.  # noqa: E501
        :rtype: str
        """
        return self._sample_data_type

    @sample_data_type.setter
    def sample_data_type(self, sample_data_type):
        """Sets the sample_data_type of this SampleDataSettings.


        :param sample_data_type: The sample_data_type of this SampleDataSettings.  # noqa: E501
        :type: str
        """
        if sample_data_type is None:
            raise ValueError("Invalid value for `sample_data_type`, must not be `None`")  # noqa: E501
        allowed_values = ["power", "angle", "sv", "sp", "ss", "tvg-20", "tvg-40", "power-angle", "complex4-float32", "complex-voltage", "proc-chain", "ss-bottom"]  # noqa: E501
        if sample_data_type not in allowed_values:
            raise ValueError(
                "Invalid value for `sample_data_type` ({0}), must be one of {1}"  # noqa: E501
                .format(sample_data_type, allowed_values)
            )

        self._sample_data_type = sample_data_type

    @property
    def range(self):
        """Gets the range of this SampleDataSettings.  # noqa: E501


        :return: The range of this SampleDataSettings.  # noqa: E501
        :rtype: float
        """
        return self._range

    @range.setter
    def range(self, range):
        """Sets the range of this SampleDataSettings.


        :param range: The range of this SampleDataSettings.  # noqa: E501
        :type: float
        """
        if range is None:
            raise ValueError("Invalid value for `range`, must not be `None`")  # noqa: E501
        if range is not None and range > 20000:  # noqa: E501
            raise ValueError("Invalid value for `range`, must be a value less than or equal to `20000`")  # noqa: E501

        self._range = range

    @property
    def range_start(self):
        """Gets the range_start of this SampleDataSettings.  # noqa: E501


        :return: The range_start of this SampleDataSettings.  # noqa: E501
        :rtype: float
        """
        return self._range_start

    @range_start.setter
    def range_start(self, range_start):
        """Sets the range_start of this SampleDataSettings.


        :param range_start: The range_start of this SampleDataSettings.  # noqa: E501
        :type: float
        """
        if range_start is not None and range_start > 20000:  # noqa: E501
            raise ValueError("Invalid value for `range_start`, must be a value less than or equal to `20000`")  # noqa: E501
        if range_start is not None and range_start < 0:  # noqa: E501
            raise ValueError("Invalid value for `range_start`, must be a value greater than or equal to `0`")  # noqa: E501

        self._range_start = range_start

    @property
    def auto_range(self):
        """Gets the auto_range of this SampleDataSettings.  # noqa: E501


        :return: The auto_range of this SampleDataSettings.  # noqa: E501
        :rtype: bool
        """
        return self._auto_range

    @auto_range.setter
    def auto_range(self, auto_range):
        """Sets the auto_range of this SampleDataSettings.


        :param auto_range: The auto_range of this SampleDataSettings.  # noqa: E501
        :type: bool
        """

        self._auto_range = auto_range

    @property
    def sample_data_heave(self):
        """Gets the sample_data_heave of this SampleDataSettings.  # noqa: E501


        :return: The sample_data_heave of this SampleDataSettings.  # noqa: E501
        :rtype: int
        """
        return self._sample_data_heave

    @sample_data_heave.setter
    def sample_data_heave(self, sample_data_heave):
        """Sets the sample_data_heave of this SampleDataSettings.


        :param sample_data_heave: The sample_data_heave of this SampleDataSettings.  # noqa: E501
        :type: int
        """
        if sample_data_heave is not None and sample_data_heave > 1:  # noqa: E501
            raise ValueError("Invalid value for `sample_data_heave`, must be a value less than or equal to `1`")  # noqa: E501
        if sample_data_heave is not None and sample_data_heave < 0:  # noqa: E501
            raise ValueError("Invalid value for `sample_data_heave`, must be a value greater than or equal to `0`")  # noqa: E501

        self._sample_data_heave = sample_data_heave

    @property
    def sample_transducer_depth(self):
        """Gets the sample_transducer_depth of this SampleDataSettings.  # noqa: E501


        :return: The sample_transducer_depth of this SampleDataSettings.  # noqa: E501
        :rtype: int
        """
        return self._sample_transducer_depth

    @sample_transducer_depth.setter
    def sample_transducer_depth(self, sample_transducer_depth):
        """Sets the sample_transducer_depth of this SampleDataSettings.


        :param sample_transducer_depth: The sample_transducer_depth of this SampleDataSettings.  # noqa: E501
        :type: int
        """
        if sample_transducer_depth is not None and sample_transducer_depth > 1:  # noqa: E501
            raise ValueError("Invalid value for `sample_transducer_depth`, must be a value less than or equal to `1`")  # noqa: E501
        if sample_transducer_depth is not None and sample_transducer_depth < 0:  # noqa: E501
            raise ValueError("Invalid value for `sample_transducer_depth`, must be a value greater than or equal to `0`")  # noqa: E501

        self._sample_transducer_depth = sample_transducer_depth

    @property
    def sample_data_delay(self):
        """Gets the sample_data_delay of this SampleDataSettings.  # noqa: E501


        :return: The sample_data_delay of this SampleDataSettings.  # noqa: E501
        :rtype: int
        """
        return self._sample_data_delay

    @sample_data_delay.setter
    def sample_data_delay(self, sample_data_delay):
        """Sets the sample_data_delay of this SampleDataSettings.


        :param sample_data_delay: The sample_data_delay of this SampleDataSettings.  # noqa: E501
        :type: int
        """
        if sample_data_delay is not None and sample_data_delay > 1:  # noqa: E501
            raise ValueError("Invalid value for `sample_data_delay`, must be a value less than or equal to `1`")  # noqa: E501
        if sample_data_delay is not None and sample_data_delay < 0:  # noqa: E501
            raise ValueError("Invalid value for `sample_data_delay`, must be a value greater than or equal to `0`")  # noqa: E501

        self._sample_data_delay = sample_data_delay

    @property
    def adcp_sub_feature(self):
        """Gets the adcp_sub_feature of this SampleDataSettings.  # noqa: E501


        :return: The adcp_sub_feature of this SampleDataSettings.  # noqa: E501
        :rtype: str
        """
        return self._adcp_sub_feature

    @adcp_sub_feature.setter
    def adcp_sub_feature(self, adcp_sub_feature):
        """Sets the adcp_sub_feature of this SampleDataSettings.


        :param adcp_sub_feature: The adcp_sub_feature of this SampleDataSettings.  # noqa: E501
        :type: str
        """
        allowed_values = ["fore", "aft", "starboard", "port"]  # noqa: E501
        if adcp_sub_feature not in allowed_values:
            raise ValueError(
                "Invalid value for `adcp_sub_feature` ({0}), must be one of {1}"  # noqa: E501
                .format(adcp_sub_feature, allowed_values)
            )

        self._adcp_sub_feature = adcp_sub_feature

    @property
    def function(self):
        """Gets the function of this SampleDataSettings.  # noqa: E501


        :return: The function of this SampleDataSettings.  # noqa: E501
        :rtype: str
        """
        return self._function

    @function.setter
    def function(self, function):
        """Sets the function of this SampleDataSettings.


        :param function: The function of this SampleDataSettings.  # noqa: E501
        :type: str
        """
        allowed_values = ["real-part", "amplitude"]  # noqa: E501
        if function not in allowed_values:
            raise ValueError(
                "Invalid value for `function` ({0}), must be one of {1}"  # noqa: E501
                .format(function, allowed_values)
            )

        self._function = function

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
        if issubclass(SampleDataSettings, dict):
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
        if not isinstance(other, SampleDataSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other