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


class ApplicationDetails(object):
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
        'application_name': 'str',
        'application_type': 'str',
        'version': 'str'
    }

    attribute_map = {
        'application_name': 'application-name',
        'application_type': 'application-type',
        'version': 'version'
    }

    def __init__(self, application_name=None, application_type=None, version=None):  # noqa: E501
        """ApplicationDetails - a model defined in Swagger"""  # noqa: E501

        self._application_name = None
        self._application_type = None
        self._version = None
        self.discriminator = None

        if application_name is not None:
            self.application_name = application_name
        if application_type is not None:
            self.application_type = application_type
        if version is not None:
            self.version = version

    @property
    def application_name(self):
        """Gets the application_name of this ApplicationDetails.  # noqa: E501


        :return: The application_name of this ApplicationDetails.  # noqa: E501
        :rtype: str
        """
        return self._application_name

    @application_name.setter
    def application_name(self, application_name):
        """Sets the application_name of this ApplicationDetails.


        :param application_name: The application_name of this ApplicationDetails.  # noqa: E501
        :type: str
        """

        self._application_name = application_name

    @property
    def application_type(self):
        """Gets the application_type of this ApplicationDetails.  # noqa: E501


        :return: The application_type of this ApplicationDetails.  # noqa: E501
        :rtype: str
        """
        return self._application_type

    @application_type.setter
    def application_type(self, application_type):
        """Sets the application_type of this ApplicationDetails.


        :param application_type: The application_type of this ApplicationDetails.  # noqa: E501
        :type: str
        """

        self._application_type = application_type

    @property
    def version(self):
        """Gets the version of this ApplicationDetails.  # noqa: E501


        :return: The version of this ApplicationDetails.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ApplicationDetails.


        :param version: The version of this ApplicationDetails.  # noqa: E501
        :type: str
        """

        self._version = version

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
        if issubclass(ApplicationDetails, dict):
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
        if not isinstance(other, ApplicationDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
