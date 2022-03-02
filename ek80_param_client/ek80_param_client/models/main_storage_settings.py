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


class MainStorageSettings(object):
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
        'file_path': 'str',
        'raw_file_name_prefix': 'str',
        'max_file_size': 'int',
        'min_free_disk_space': 'int',
        'sample_range': 'int',
        'sample_range_auto': 'bool',
        'individual_range_control': 'bool',
        'record_raw_active': 'bool'
    }

    attribute_map = {
        'file_path': 'file-path',
        'raw_file_name_prefix': 'raw-file-name-prefix',
        'max_file_size': 'max-file-size',
        'min_free_disk_space': 'min-free-disk-space',
        'sample_range': 'sample-range',
        'sample_range_auto': 'sample-range-auto',
        'individual_range_control': 'individual-range-control',
        'record_raw_active': 'record-raw-active'
    }

    def __init__(self, file_path=None, raw_file_name_prefix=None, max_file_size=None, min_free_disk_space=None, sample_range=None, sample_range_auto=None, individual_range_control=None, record_raw_active=None):  # noqa: E501
        """MainStorageSettings - a model defined in Swagger"""  # noqa: E501

        self._file_path = None
        self._raw_file_name_prefix = None
        self._max_file_size = None
        self._min_free_disk_space = None
        self._sample_range = None
        self._sample_range_auto = None
        self._individual_range_control = None
        self._record_raw_active = None
        self.discriminator = None

        if file_path is not None:
            self.file_path = file_path
        if raw_file_name_prefix is not None:
            self.raw_file_name_prefix = raw_file_name_prefix
        if max_file_size is not None:
            self.max_file_size = max_file_size
        if min_free_disk_space is not None:
            self.min_free_disk_space = min_free_disk_space
        if sample_range is not None:
            self.sample_range = sample_range
        if sample_range_auto is not None:
            self.sample_range_auto = sample_range_auto
        if individual_range_control is not None:
            self.individual_range_control = individual_range_control
        if record_raw_active is not None:
            self.record_raw_active = record_raw_active

    @property
    def file_path(self):
        """Gets the file_path of this MainStorageSettings.  # noqa: E501


        :return: The file_path of this MainStorageSettings.  # noqa: E501
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        """Sets the file_path of this MainStorageSettings.


        :param file_path: The file_path of this MainStorageSettings.  # noqa: E501
        :type: str
        """

        self._file_path = file_path

    @property
    def raw_file_name_prefix(self):
        """Gets the raw_file_name_prefix of this MainStorageSettings.  # noqa: E501


        :return: The raw_file_name_prefix of this MainStorageSettings.  # noqa: E501
        :rtype: str
        """
        return self._raw_file_name_prefix

    @raw_file_name_prefix.setter
    def raw_file_name_prefix(self, raw_file_name_prefix):
        """Sets the raw_file_name_prefix of this MainStorageSettings.


        :param raw_file_name_prefix: The raw_file_name_prefix of this MainStorageSettings.  # noqa: E501
        :type: str
        """

        self._raw_file_name_prefix = raw_file_name_prefix

    @property
    def max_file_size(self):
        """Gets the max_file_size of this MainStorageSettings.  # noqa: E501


        :return: The max_file_size of this MainStorageSettings.  # noqa: E501
        :rtype: int
        """
        return self._max_file_size

    @max_file_size.setter
    def max_file_size(self, max_file_size):
        """Sets the max_file_size of this MainStorageSettings.


        :param max_file_size: The max_file_size of this MainStorageSettings.  # noqa: E501
        :type: int
        """

        self._max_file_size = max_file_size

    @property
    def min_free_disk_space(self):
        """Gets the min_free_disk_space of this MainStorageSettings.  # noqa: E501


        :return: The min_free_disk_space of this MainStorageSettings.  # noqa: E501
        :rtype: int
        """
        return self._min_free_disk_space

    @min_free_disk_space.setter
    def min_free_disk_space(self, min_free_disk_space):
        """Sets the min_free_disk_space of this MainStorageSettings.


        :param min_free_disk_space: The min_free_disk_space of this MainStorageSettings.  # noqa: E501
        :type: int
        """

        self._min_free_disk_space = min_free_disk_space

    @property
    def sample_range(self):
        """Gets the sample_range of this MainStorageSettings.  # noqa: E501


        :return: The sample_range of this MainStorageSettings.  # noqa: E501
        :rtype: int
        """
        return self._sample_range

    @sample_range.setter
    def sample_range(self, sample_range):
        """Sets the sample_range of this MainStorageSettings.


        :param sample_range: The sample_range of this MainStorageSettings.  # noqa: E501
        :type: int
        """

        self._sample_range = sample_range

    @property
    def sample_range_auto(self):
        """Gets the sample_range_auto of this MainStorageSettings.  # noqa: E501


        :return: The sample_range_auto of this MainStorageSettings.  # noqa: E501
        :rtype: bool
        """
        return self._sample_range_auto

    @sample_range_auto.setter
    def sample_range_auto(self, sample_range_auto):
        """Sets the sample_range_auto of this MainStorageSettings.


        :param sample_range_auto: The sample_range_auto of this MainStorageSettings.  # noqa: E501
        :type: bool
        """

        self._sample_range_auto = sample_range_auto

    @property
    def individual_range_control(self):
        """Gets the individual_range_control of this MainStorageSettings.  # noqa: E501


        :return: The individual_range_control of this MainStorageSettings.  # noqa: E501
        :rtype: bool
        """
        return self._individual_range_control

    @individual_range_control.setter
    def individual_range_control(self, individual_range_control):
        """Sets the individual_range_control of this MainStorageSettings.


        :param individual_range_control: The individual_range_control of this MainStorageSettings.  # noqa: E501
        :type: bool
        """

        self._individual_range_control = individual_range_control

    @property
    def record_raw_active(self):
        """Gets the record_raw_active of this MainStorageSettings.  # noqa: E501


        :return: The record_raw_active of this MainStorageSettings.  # noqa: E501
        :rtype: bool
        """
        return self._record_raw_active

    @record_raw_active.setter
    def record_raw_active(self, record_raw_active):
        """Sets the record_raw_active of this MainStorageSettings.


        :param record_raw_active: The record_raw_active of this MainStorageSettings.  # noqa: E501
        :type: bool
        """

        self._record_raw_active = record_raw_active

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
        if issubclass(MainStorageSettings, dict):
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
        if not isinstance(other, MainStorageSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
