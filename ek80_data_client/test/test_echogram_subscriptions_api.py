# coding: utf-8

"""
    REST API for setting up data subscriptions on the EK80 Echo Sounder

    The API, and the documentation of it, is still under construction. Feel free to experiment with it, but Kongsberg is only able to provide very limited support at the moment.  # How to start data output  1. Create a subscription  2. Create a communication end point  3. Add the subscription to the communication end point      # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import ek80_data_client
from ek80_data_client.api.echogram_subscriptions_api import EchogramSubscriptionsApi  # noqa: E501
from ek80_data_client.rest import ApiException


class TestEchogramSubscriptionsApi(unittest.TestCase):
    """EchogramSubscriptionsApi unit test stubs"""

    def setUp(self):
        self.api = ek80_data_client.api.echogram_subscriptions_api.EchogramSubscriptionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_echogram_subscription(self):
        """Test case for create_echogram_subscription

        Create an echogram data subscription  # noqa: E501
        """
        pass

    def test_delete_echogram_subscription(self):
        """Test case for delete_echogram_subscription

        Delete a echogram data subscription  # noqa: E501
        """
        pass

    def test_get_echogram_subscription(self):
        """Test case for get_echogram_subscription

        Get a particular echogram data subscription specification  # noqa: E501
        """
        pass

    def test_get_echogram_subscriptions(self):
        """Test case for get_echogram_subscriptions

        Get all echogram data subscriptions  # noqa: E501
        """
        pass

    def test_update_echogram_subscription(self):
        """Test case for update_echogram_subscription

        Update an echogram data subscription  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
