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
from ek80_data_client.api.ts_detection_chirp_subscriptions_api import TsDetectionChirpSubscriptionsApi  # noqa: E501
from ek80_data_client.rest import ApiException


class TestTsDetectionChirpSubscriptionsApi(unittest.TestCase):
    """TsDetectionChirpSubscriptionsApi unit test stubs"""

    def setUp(self):
        self.api = ek80_data_client.api.ts_detection_chirp_subscriptions_api.TsDetectionChirpSubscriptionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_ts_detection_chirp_subscription(self):
        """Test case for create_ts_detection_chirp_subscription

        Create a ts detection chirp data subscription  # noqa: E501
        """
        pass

    def test_delete_ts_detection_chirp_subscription(self):
        """Test case for delete_ts_detection_chirp_subscription

        Delete a ts detection chirp data subscription  # noqa: E501
        """
        pass

    def test_get_ts_detection_chirp_subscription(self):
        """Test case for get_ts_detection_chirp_subscription

        Get a particular ts detection chirp subscription specification  # noqa: E501
        """
        pass

    def test_get_ts_detection_chirp_subscriptions(self):
        """Test case for get_ts_detection_chirp_subscriptions

        Get all ts detection chirp subscriptions  # noqa: E501
        """
        pass

    def test_update_ts_detection_chirp_subscription(self):
        """Test case for update_ts_detection_chirp_subscription

        Update a ts detection chirp data subscription  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()