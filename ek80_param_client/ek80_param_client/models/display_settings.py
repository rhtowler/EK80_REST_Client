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


class DisplaySettings(object):
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
        'display_palette': 'str',
        'echo_colours': 'str',
        'brightness': 'int',
        'full_screen': 'bool'
    }

    attribute_map = {
        'display_palette': 'display-palette',
        'echo_colours': 'echo-colours',
        'brightness': 'brightness',
        'full_screen': 'full-screen'
    }

    def __init__(self, display_palette=None, echo_colours=None, brightness=None, full_screen=None):  # noqa: E501
        """DisplaySettings - a model defined in Swagger"""  # noqa: E501

        self._display_palette = None
        self._echo_colours = None
        self._brightness = None
        self._full_screen = None
        self.discriminator = None

        if display_palette is not None:
            self.display_palette = display_palette
        if echo_colours is not None:
            self.echo_colours = echo_colours
        if brightness is not None:
            self.brightness = brightness
        if full_screen is not None:
            self.full_screen = full_screen

    @property
    def display_palette(self):
        """Gets the display_palette of this DisplaySettings.  # noqa: E501


        :return: The display_palette of this DisplaySettings.  # noqa: E501
        :rtype: str
        """
        return self._display_palette

    @display_palette.setter
    def display_palette(self, display_palette):
        """Sets the display_palette of this DisplaySettings.


        :param display_palette: The display_palette of this DisplaySettings.  # noqa: E501
        :type: str
        """
        allowed_values = ["day-black", "day-white", "night"]  # noqa: E501
        if display_palette not in allowed_values:
            raise ValueError(
                "Invalid value for `display_palette` ({0}), must be one of {1}"  # noqa: E501
                .format(display_palette, allowed_values)
            )

        self._display_palette = display_palette

    @property
    def echo_colours(self):
        """Gets the echo_colours of this DisplaySettings.  # noqa: E501


        :return: The echo_colours of this DisplaySettings.  # noqa: E501
        :rtype: str
        """
        return self._echo_colours

    @echo_colours.setter
    def echo_colours(self, echo_colours):
        """Sets the echo_colours of this DisplaySettings.


        :param echo_colours: The echo_colours of this DisplaySettings.  # noqa: E501
        :type: str
        """
        allowed_values = ["colours-12", "colours-64-sonar", "colours-64-smooth-echo-sounder", "colours-64-gray-scale", "colours-64-bi500"]  # noqa: E501
        if echo_colours not in allowed_values:
            raise ValueError(
                "Invalid value for `echo_colours` ({0}), must be one of {1}"  # noqa: E501
                .format(echo_colours, allowed_values)
            )

        self._echo_colours = echo_colours

    @property
    def brightness(self):
        """Gets the brightness of this DisplaySettings.  # noqa: E501


        :return: The brightness of this DisplaySettings.  # noqa: E501
        :rtype: int
        """
        return self._brightness

    @brightness.setter
    def brightness(self, brightness):
        """Sets the brightness of this DisplaySettings.


        :param brightness: The brightness of this DisplaySettings.  # noqa: E501
        :type: int
        """

        self._brightness = brightness

    @property
    def full_screen(self):
        """Gets the full_screen of this DisplaySettings.  # noqa: E501


        :return: The full_screen of this DisplaySettings.  # noqa: E501
        :rtype: bool
        """
        return self._full_screen

    @full_screen.setter
    def full_screen(self, full_screen):
        """Sets the full_screen of this DisplaySettings.


        :param full_screen: The full_screen of this DisplaySettings.  # noqa: E501
        :type: bool
        """

        self._full_screen = full_screen

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
        if issubclass(DisplaySettings, dict):
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
        if not isinstance(other, DisplaySettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
