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
from ek80_data_client.api.operation_api import OperationApi  # noqa: E501
from ek80_data_client.rest import ApiException


class TestOperationApi(unittest.TestCase):
    """OperationApi unit test stubs"""

    def setUp(self):
        self.api = ek80_data_client.api.operation_api.OperationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_auto_range(self):
        """Test case for get_auto_range

        Get ping auto display range  # noqa: E501
        """
        pass

    def test_get_ext_sync(self):
        """Test case for get_ext_sync

        Get external sync settings  # noqa: E501
        """
        pass

    def test_get_ext_sync_delay(self):
        """Test case for get_ext_sync_delay

        Get synchronization delay  # noqa: E501
        """
        pass

    def test_get_ext_sync_mode(self):
        """Test case for get_ext_sync_mode

        Get synchronization mode  # noqa: E501
        """
        pass

    def test_get_operation_mode(self):
        """Test case for get_operation_mode

        Get operation mode  # noqa: E501
        """
        pass

    def test_get_operational_state(self):
        """Test case for get_operational_state

        Get operation state of the application  # noqa: E501
        """
        pass

    def test_get_ping_interval(self):
        """Test case for get_ping_interval

        Get ping interval  # noqa: E501
        """
        pass

    def test_get_ping_mode(self):
        """Test case for get_ping_mode

        Get ping mode  # noqa: E501
        """
        pass

    def test_get_play_state(self):
        """Test case for get_play_state

        Get play state  # noqa: E501
        """
        pass

    def test_get_range(self):
        """Test case for get_range

        Get ping display range  # noqa: E501
        """
        pass

    def test_put_auto_range(self):
        """Test case for put_auto_range

        Set ping auto display range  # noqa: E501
        """
        pass

    def test_put_ext_sync(self):
        """Test case for put_ext_sync

        Set external sync settings  # noqa: E501
        """
        pass

    def test_put_ext_sync_delay(self):
        """Test case for put_ext_sync_delay

        Set synchronization delay  # noqa: E501
        """
        pass

    def test_put_ext_sync_mode(self):
        """Test case for put_ext_sync_mode

        Set synchronization mode  # noqa: E501
        """
        pass

    def test_put_operation_mode(self):
        """Test case for put_operation_mode

        Set operation mode  # noqa: E501
        """
        pass

    def test_put_ping_interval(self):
        """Test case for put_ping_interval

        Set ping interval  # noqa: E501
        """
        pass

    def test_put_ping_mode(self):
        """Test case for put_ping_mode

        Set ping mode  # noqa: E501
        """
        pass

    def test_put_play_state(self):
        """Test case for put_play_state

        Set play state  # noqa: E501
        """
        pass

    def test_put_range(self):
        """Test case for put_range

        Set ping display range  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()