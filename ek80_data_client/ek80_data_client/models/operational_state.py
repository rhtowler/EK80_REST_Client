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


class OperationalState(object):
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
        'operation_mode': 'str',
        'ping_mode': 'str',
        'play_state': 'str',
        'external_sync': 'ExternalSync',
        'active_user_setting': 'str'
    }

    attribute_map = {
        'operation_mode': 'operation-mode',
        'ping_mode': 'ping-mode',
        'play_state': 'play-state',
        'external_sync': 'external-sync',
        'active_user_setting': 'active-user-setting'
    }

    def __init__(self, operation_mode=None, ping_mode=None, play_state=None, external_sync=None, active_user_setting=None):  # noqa: E501
        """OperationalState - a model defined in Swagger"""  # noqa: E501

        self._operation_mode = None
        self._ping_mode = None
        self._play_state = None
        self._external_sync = None
        self._active_user_setting = None
        self.discriminator = None

        if operation_mode is not None:
            self.operation_mode = operation_mode
        if ping_mode is not None:
            self.ping_mode = ping_mode
        if play_state is not None:
            self.play_state = play_state
        if external_sync is not None:
            self.external_sync = external_sync
        if active_user_setting is not None:
            self.active_user_setting = active_user_setting

    @property
    def operation_mode(self):
        """Gets the operation_mode of this OperationalState.  # noqa: E501


        :return: The operation_mode of this OperationalState.  # noqa: E501
        :rtype: str
        """
        return self._operation_mode

    @operation_mode.setter
    def operation_mode(self, operation_mode):
        """Sets the operation_mode of this OperationalState.


        :param operation_mode: The operation_mode of this OperationalState.  # noqa: E501
        :type: str
        """
        allowed_values = ["inactive", "normal", "replay", "simulation", "mission"]  # noqa: E501
        if operation_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `operation_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(operation_mode, allowed_values)
            )

        self._operation_mode = operation_mode

    @property
    def ping_mode(self):
        """Gets the ping_mode of this OperationalState.  # noqa: E501


        :return: The ping_mode of this OperationalState.  # noqa: E501
        :rtype: str
        """
        return self._ping_mode

    @ping_mode.setter
    def ping_mode(self, ping_mode):
        """Sets the ping_mode of this OperationalState.


        :param ping_mode: The ping_mode of this OperationalState.  # noqa: E501
        :type: str
        """
        allowed_values = ["single", "interval", "maximum"]  # noqa: E501
        if ping_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `ping_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(ping_mode, allowed_values)
            )

        self._ping_mode = ping_mode

    @property
    def play_state(self):
        """Gets the play_state of this OperationalState.  # noqa: E501


        :return: The play_state of this OperationalState.  # noqa: E501
        :rtype: str
        """
        return self._play_state

    @play_state.setter
    def play_state(self, play_state):
        """Sets the play_state of this OperationalState.


        :param play_state: The play_state of this OperationalState.  # noqa: E501
        :type: str
        """
        allowed_values = ["stopped", "running", "paused"]  # noqa: E501
        if play_state not in allowed_values:
            raise ValueError(
                "Invalid value for `play_state` ({0}), must be one of {1}"  # noqa: E501
                .format(play_state, allowed_values)
            )

        self._play_state = play_state

    @property
    def external_sync(self):
        """Gets the external_sync of this OperationalState.  # noqa: E501


        :return: The external_sync of this OperationalState.  # noqa: E501
        :rtype: ExternalSync
        """
        return self._external_sync

    @external_sync.setter
    def external_sync(self, external_sync):
        """Sets the external_sync of this OperationalState.


        :param external_sync: The external_sync of this OperationalState.  # noqa: E501
        :type: ExternalSync
        """

        self._external_sync = external_sync

    @property
    def active_user_setting(self):
        """Gets the active_user_setting of this OperationalState.  # noqa: E501


        :return: The active_user_setting of this OperationalState.  # noqa: E501
        :rtype: str
        """
        return self._active_user_setting

    @active_user_setting.setter
    def active_user_setting(self, active_user_setting):
        """Sets the active_user_setting of this OperationalState.


        :param active_user_setting: The active_user_setting of this OperationalState.  # noqa: E501
        :type: str
        """

        self._active_user_setting = active_user_setting

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
        if issubclass(OperationalState, dict):
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
        if not isinstance(other, OperationalState):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
