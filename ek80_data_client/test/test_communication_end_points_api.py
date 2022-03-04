# coding: utf-8

"""
    REST API for setting up data subscriptions on the EK80 Echo Sounder

    The API, and the documentation of it, is currently under construction and is subject to change without further notice  # How to start data output  1. Create a subscription  2. Create a communication end point  3. Add the subscription to the communication end point    A link example, [kongsberg.com](http://www.kongsberg.com).  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import ek80_data_client
from ek80_data_client.api.communication_end_points_api import CommunicationEndPointsApi  # noqa: E501
from ek80_data_client.rest import ApiException


class TestCommunicationEndPointsApi(unittest.TestCase):
    """CommunicationEndPointsApi unit test stubs"""

    def setUp(self):
        self.api = ek80_data_client.api.communication_end_points_api.CommunicationEndPointsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_subscription_to_end_point(self):
        """Test case for add_subscription_to_end_point

        Add a subscription to the communication end point  # noqa: E501
        """
        pass

    def test_create_communication_end_point(self):
        """Test case for create_communication_end_point

        Create a new communication end point  # noqa: E501
        """
        pass

    def test_delete_communication_end_point(self):
        """Test case for delete_communication_end_point

        Delete a communication end point  # noqa: E501
        """
        pass

    def test_get_active_communication_end_points(self):
        """Test case for get_active_communication_end_points

        Get information about the active communication end points  # noqa: E501
        """
        pass

    def test_get_subscriptions_by_end_point(self):
        """Test case for get_subscriptions_by_end_point

        Get the active data subscriptions for the end point  # noqa: E501
        """
        pass

    def test_remove_subscription_from_end_point(self):
        """Test case for remove_subscription_from_end_point

        Remove a subscription from the communication end point  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()