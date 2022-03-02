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


class Installation(object):
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
        'offset': 'Offset',
        'rotation': 'Rotation',
        'mounting': 'str',
        'orientation': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'rotation': 'rotation',
        'mounting': 'mounting',
        'orientation': 'orientation'
    }

    def __init__(self, offset=None, rotation=None, mounting=None, orientation=None):  # noqa: E501
        """Installation - a model defined in Swagger"""  # noqa: E501

        self._offset = None
        self._rotation = None
        self._mounting = None
        self._orientation = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if rotation is not None:
            self.rotation = rotation
        if mounting is not None:
            self.mounting = mounting
        if orientation is not None:
            self.orientation = orientation

    @property
    def offset(self):
        """Gets the offset of this Installation.  # noqa: E501


        :return: The offset of this Installation.  # noqa: E501
        :rtype: Offset
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this Installation.


        :param offset: The offset of this Installation.  # noqa: E501
        :type: Offset
        """

        self._offset = offset

    @property
    def rotation(self):
        """Gets the rotation of this Installation.  # noqa: E501


        :return: The rotation of this Installation.  # noqa: E501
        :rtype: Rotation
        """
        return self._rotation

    @rotation.setter
    def rotation(self, rotation):
        """Sets the rotation of this Installation.


        :param rotation: The rotation of this Installation.  # noqa: E501
        :type: Rotation
        """

        self._rotation = rotation

    @property
    def mounting(self):
        """Gets the mounting of this Installation.  # noqa: E501


        :return: The mounting of this Installation.  # noqa: E501
        :rtype: str
        """
        return self._mounting

    @mounting.setter
    def mounting(self, mounting):
        """Sets the mounting of this Installation.


        :param mounting: The mounting of this Installation.  # noqa: E501
        :type: str
        """
        allowed_values = ["hull-mounted", "drop-keel", "towed"]  # noqa: E501
        if mounting not in allowed_values:
            raise ValueError(
                "Invalid value for `mounting` ({0}), must be one of {1}"  # noqa: E501
                .format(mounting, allowed_values)
            )

        self._mounting = mounting

    @property
    def orientation(self):
        """Gets the orientation of this Installation.  # noqa: E501


        :return: The orientation of this Installation.  # noqa: E501
        :rtype: str
        """
        return self._orientation

    @orientation.setter
    def orientation(self, orientation):
        """Sets the orientation of this Installation.


        :param orientation: The orientation of this Installation.  # noqa: E501
        :type: str
        """
        allowed_values = ["horizontal", "vertical"]  # noqa: E501
        if orientation not in allowed_values:
            raise ValueError(
                "Invalid value for `orientation` ({0}), must be one of {1}"  # noqa: E501
                .format(orientation, allowed_values)
            )

        self._orientation = orientation

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
        if issubclass(Installation, dict):
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
        if not isinstance(other, Installation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
