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


class IntegrationChirpSettings(object):
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
        'update_type': 'str',
        'integration_state': 'str',
        'margin': 'float',
        'sv_threshold': 'float',
        'sv_bin_overlap': 'float'
    }

    attribute_map = {
        'range': 'range',
        'range_start': 'range-start',
        'layer_type': 'layer-type',
        'update_type': 'update-type',
        'integration_state': 'integration-state',
        'margin': 'margin',
        'sv_threshold': 'sv-threshold',
        'sv_bin_overlap': 'sv-bin-overlap'
    }

    def __init__(self, range=500.0, range_start=10.0, layer_type='surface', update_type='update-ping', integration_state='start', margin=1.0, sv_threshold=-100.0, sv_bin_overlap=50.0):  # noqa: E501
        """IntegrationChirpSettings - a model defined in Swagger"""  # noqa: E501

        self._range = None
        self._range_start = None
        self._layer_type = None
        self._update_type = None
        self._integration_state = None
        self._margin = None
        self._sv_threshold = None
        self._sv_bin_overlap = None
        self.discriminator = None

        self.range = range
        self.range_start = range_start
        if layer_type is not None:
            self.layer_type = layer_type
        self.update_type = update_type
        self.integration_state = integration_state
        if margin is not None:
            self.margin = margin
        if sv_threshold is not None:
            self.sv_threshold = sv_threshold
        if sv_bin_overlap is not None:
            self.sv_bin_overlap = sv_bin_overlap

    @property
    def range(self):
        """Gets the range of this IntegrationChirpSettings.  # noqa: E501


        :return: The range of this IntegrationChirpSettings.  # noqa: E501
        :rtype: float
        """
        return self._range

    @range.setter
    def range(self, range):
        """Sets the range of this IntegrationChirpSettings.


        :param range: The range of this IntegrationChirpSettings.  # noqa: E501
        :type: float
        """
        if range is None:
            raise ValueError("Invalid value for `range`, must not be `None`")  # noqa: E501

        self._range = range

    @property
    def range_start(self):
        """Gets the range_start of this IntegrationChirpSettings.  # noqa: E501


        :return: The range_start of this IntegrationChirpSettings.  # noqa: E501
        :rtype: float
        """
        return self._range_start

    @range_start.setter
    def range_start(self, range_start):
        """Sets the range_start of this IntegrationChirpSettings.


        :param range_start: The range_start of this IntegrationChirpSettings.  # noqa: E501
        :type: float
        """
        if range_start is None:
            raise ValueError("Invalid value for `range_start`, must not be `None`")  # noqa: E501

        self._range_start = range_start

    @property
    def layer_type(self):
        """Gets the layer_type of this IntegrationChirpSettings.  # noqa: E501


        :return: The layer_type of this IntegrationChirpSettings.  # noqa: E501
        :rtype: str
        """
        return self._layer_type

    @layer_type.setter
    def layer_type(self, layer_type):
        """Sets the layer_type of this IntegrationChirpSettings.


        :param layer_type: The layer_type of this IntegrationChirpSettings.  # noqa: E501
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
    def update_type(self):
        """Gets the update_type of this IntegrationChirpSettings.  # noqa: E501


        :return: The update_type of this IntegrationChirpSettings.  # noqa: E501
        :rtype: str
        """
        return self._update_type

    @update_type.setter
    def update_type(self, update_type):
        """Sets the update_type of this IntegrationChirpSettings.


        :param update_type: The update_type of this IntegrationChirpSettings.  # noqa: E501
        :type: str
        """
        if update_type is None:
            raise ValueError("Invalid value for `update_type`, must not be `None`")  # noqa: E501
        allowed_values = ["update-ping", "update-accumulate"]  # noqa: E501
        if update_type not in allowed_values:
            raise ValueError(
                "Invalid value for `update_type` ({0}), must be one of {1}"  # noqa: E501
                .format(update_type, allowed_values)
            )

        self._update_type = update_type

    @property
    def integration_state(self):
        """Gets the integration_state of this IntegrationChirpSettings.  # noqa: E501


        :return: The integration_state of this IntegrationChirpSettings.  # noqa: E501
        :rtype: str
        """
        return self._integration_state

    @integration_state.setter
    def integration_state(self, integration_state):
        """Sets the integration_state of this IntegrationChirpSettings.


        :param integration_state: The integration_state of this IntegrationChirpSettings.  # noqa: E501
        :type: str
        """
        if integration_state is None:
            raise ValueError("Invalid value for `integration_state`, must not be `None`")  # noqa: E501
        allowed_values = ["start", "stop"]  # noqa: E501
        if integration_state not in allowed_values:
            raise ValueError(
                "Invalid value for `integration_state` ({0}), must be one of {1}"  # noqa: E501
                .format(integration_state, allowed_values)
            )

        self._integration_state = integration_state

    @property
    def margin(self):
        """Gets the margin of this IntegrationChirpSettings.  # noqa: E501


        :return: The margin of this IntegrationChirpSettings.  # noqa: E501
        :rtype: float
        """
        return self._margin

    @margin.setter
    def margin(self, margin):
        """Sets the margin of this IntegrationChirpSettings.


        :param margin: The margin of this IntegrationChirpSettings.  # noqa: E501
        :type: float
        """

        self._margin = margin

    @property
    def sv_threshold(self):
        """Gets the sv_threshold of this IntegrationChirpSettings.  # noqa: E501


        :return: The sv_threshold of this IntegrationChirpSettings.  # noqa: E501
        :rtype: float
        """
        return self._sv_threshold

    @sv_threshold.setter
    def sv_threshold(self, sv_threshold):
        """Sets the sv_threshold of this IntegrationChirpSettings.


        :param sv_threshold: The sv_threshold of this IntegrationChirpSettings.  # noqa: E501
        :type: float
        """

        self._sv_threshold = sv_threshold

    @property
    def sv_bin_overlap(self):
        """Gets the sv_bin_overlap of this IntegrationChirpSettings.  # noqa: E501


        :return: The sv_bin_overlap of this IntegrationChirpSettings.  # noqa: E501
        :rtype: float
        """
        return self._sv_bin_overlap

    @sv_bin_overlap.setter
    def sv_bin_overlap(self, sv_bin_overlap):
        """Sets the sv_bin_overlap of this IntegrationChirpSettings.


        :param sv_bin_overlap: The sv_bin_overlap of this IntegrationChirpSettings.  # noqa: E501
        :type: float
        """

        self._sv_bin_overlap = sv_bin_overlap

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
        if issubclass(IntegrationChirpSettings, dict):
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
        if not isinstance(other, IntegrationChirpSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
