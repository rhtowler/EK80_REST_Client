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


class Rotation(object):
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
        'around_x': 'float',
        'around_y': 'float',
        'around_z': 'float'
    }

    attribute_map = {
        'around_x': 'around-x',
        'around_y': 'around-y',
        'around_z': 'around-z'
    }

    def __init__(self, around_x=None, around_y=None, around_z=None):  # noqa: E501
        """Rotation - a model defined in Swagger"""  # noqa: E501

        self._around_x = None
        self._around_y = None
        self._around_z = None
        self.discriminator = None

        if around_x is not None:
            self.around_x = around_x
        if around_y is not None:
            self.around_y = around_y
        if around_z is not None:
            self.around_z = around_z

    @property
    def around_x(self):
        """Gets the around_x of this Rotation.  # noqa: E501


        :return: The around_x of this Rotation.  # noqa: E501
        :rtype: float
        """
        return self._around_x

    @around_x.setter
    def around_x(self, around_x):
        """Sets the around_x of this Rotation.


        :param around_x: The around_x of this Rotation.  # noqa: E501
        :type: float
        """

        self._around_x = around_x

    @property
    def around_y(self):
        """Gets the around_y of this Rotation.  # noqa: E501


        :return: The around_y of this Rotation.  # noqa: E501
        :rtype: float
        """
        return self._around_y

    @around_y.setter
    def around_y(self, around_y):
        """Sets the around_y of this Rotation.


        :param around_y: The around_y of this Rotation.  # noqa: E501
        :type: float
        """

        self._around_y = around_y

    @property
    def around_z(self):
        """Gets the around_z of this Rotation.  # noqa: E501


        :return: The around_z of this Rotation.  # noqa: E501
        :rtype: float
        """
        return self._around_z

    @around_z.setter
    def around_z(self, around_z):
        """Sets the around_z of this Rotation.


        :param around_z: The around_z of this Rotation.  # noqa: E501
        :type: float
        """

        self._around_z = around_z

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
        if issubclass(Rotation, dict):
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
        if not isinstance(other, Rotation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
