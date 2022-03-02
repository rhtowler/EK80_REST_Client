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
from ek80_data_client.api.bottom_detection_subscriptions_api import BottomDetectionSubscriptionsApi  # noqa: E501
from ek80_data_client.rest import ApiException


class TestBottomDetectionSubscriptionsApi(unittest.TestCase):
    """BottomDetectionSubscriptionsApi unit test stubs"""

    def setUp(self):
        self.api = ek80_data_client.api.bottom_detection_subscriptions_api.BottomDetectionSubscriptionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_bottom_detection_subscription(self):
        """Test case for create_bottom_detection_subscription

        Create a bottom detection data subscription  # noqa: E501
        """
        pass

    def test_delete_bottom_detection_subscription(self):
        """Test case for delete_bottom_detection_subscription

        Delete a bottom detection data subscription  # noqa: E501
        """
        pass

    def test_get_bottom_detection_subscription(self):
        """Test case for get_bottom_detection_subscription

        Get a bottom detection subscription specification  # noqa: E501
        """
        pass

    def test_get_bottom_detection_subscriptions(self):
        """Test case for get_bottom_detection_subscriptions

        Get all bottom detection data subscriptions  # noqa: E501
        """
        pass

    def test_update_bottom_detection_subscription(self):
        """Test case for update_bottom_detection_subscription

        Update an bottom detection subscription  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
