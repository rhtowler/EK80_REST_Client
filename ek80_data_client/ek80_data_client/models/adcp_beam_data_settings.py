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


class AdcpBeamDataSettings(object):
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
        'beam_data_type': 'str',
        'range': 'float',
        'range_start': 'float',
        'use_heave_adjustment': 'bool'
    }

    attribute_map = {
        'beam_data_type': 'beam-data-type',
        'range': 'range',
        'range_start': 'range-start',
        'use_heave_adjustment': 'use-heave-adjustment'
    }

    def __init__(self, beam_data_type=None, range=None, range_start=0.0, use_heave_adjustment=True):  # noqa: E501
        """AdcpBeamDataSettings - a model defined in Swagger"""  # noqa: E501

        self._beam_data_type = None
        self._range = None
        self._range_start = None
        self._use_heave_adjustment = None
        self.discriminator = None

        self.beam_data_type = beam_data_type
        self.range = range
        if range_start is not None:
            self.range_start = range_start
        if use_heave_adjustment is not None:
            self.use_heave_adjustment = use_heave_adjustment

    @property
    def beam_data_type(self):
        """Gets the beam_data_type of this AdcpBeamDataSettings.  # noqa: E501


        :return: The beam_data_type of this AdcpBeamDataSettings.  # noqa: E501
        :rtype: str
        """
        return self._beam_data_type

    @beam_data_type.setter
    def beam_data_type(self, beam_data_type):
        """Sets the beam_data_type of this AdcpBeamDataSettings.


        :param beam_data_type: The beam_data_type of this AdcpBeamDataSettings.  # noqa: E501
        :type: str
        """
        if beam_data_type is None:
            raise ValueError("Invalid value for `beam_data_type`, must not be `None`")  # noqa: E501
        allowed_values = ["beam-velocity-1", "beam-velocity-2", "beam-velocity-3", "beam-velocity-4", "correlation-beam1", "correlation-beam2", "correlation-beam3", "correlation-beam4", "error-factor"]  # noqa: E501
        if beam_data_type not in allowed_values:
            raise ValueError(
                "Invalid value for `beam_data_type` ({0}), must be one of {1}"  # noqa: E501
                .format(beam_data_type, allowed_values)
            )

        self._beam_data_type = beam_data_type

    @property
    def range(self):
        """Gets the range of this AdcpBeamDataSettings.  # noqa: E501


        :return: The range of this AdcpBeamDataSettings.  # noqa: E501
        :rtype: float
        """
        return self._range

    @range.setter
    def range(self, range):
        """Sets the range of this AdcpBeamDataSettings.


        :param range: The range of this AdcpBeamDataSettings.  # noqa: E501
        :type: float
        """
        if range is None:
            raise ValueError("Invalid value for `range`, must not be `None`")  # noqa: E501
        if range is not None and range > 20000:  # noqa: E501
            raise ValueError("Invalid value for `range`, must be a value less than or equal to `20000`")  # noqa: E501

        self._range = range

    @property
    def range_start(self):
        """Gets the range_start of this AdcpBeamDataSettings.  # noqa: E501


        :return: The range_start of this AdcpBeamDataSettings.  # noqa: E501
        :rtype: float
        """
        return self._range_start

    @range_start.setter
    def range_start(self, range_start):
        """Sets the range_start of this AdcpBeamDataSettings.


        :param range_start: The range_start of this AdcpBeamDataSettings.  # noqa: E501
        :type: float
        """
        if range_start is not None and range_start > 20000:  # noqa: E501
            raise ValueError("Invalid value for `range_start`, must be a value less than or equal to `20000`")  # noqa: E501
        if range_start is not None and range_start < -20000:  # noqa: E501
            raise ValueError("Invalid value for `range_start`, must be a value greater than or equal to `-20000`")  # noqa: E501

        self._range_start = range_start

    @property
    def use_heave_adjustment(self):
        """Gets the use_heave_adjustment of this AdcpBeamDataSettings.  # noqa: E501


        :return: The use_heave_adjustment of this AdcpBeamDataSettings.  # noqa: E501
        :rtype: bool
        """
        return self._use_heave_adjustment

    @use_heave_adjustment.setter
    def use_heave_adjustment(self, use_heave_adjustment):
        """Sets the use_heave_adjustment of this AdcpBeamDataSettings.


        :param use_heave_adjustment: The use_heave_adjustment of this AdcpBeamDataSettings.  # noqa: E501
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
        if issubclass(AdcpBeamDataSettings, dict):
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
        if not isinstance(other, AdcpBeamDataSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
