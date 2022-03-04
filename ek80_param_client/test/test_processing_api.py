# coding: utf-8

"""
    REST API for the EK80 Echo Sounder

    This API is for internal Simrad/Kongsberg Maritime use only.  The API, and the documentation of it, is currently under construction and is subject to change without further notice  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import ek80_param_client
from ek80_param_client.api.processing_api import ProcessingApi  # noqa: E501
from ek80_param_client.rest import ApiException


class TestProcessingApi(unittest.TestCase):
    """ProcessingApi unit test stubs"""

    def setUp(self):
        self.api = ek80_param_client.api.processing_api.ProcessingApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_processing_get_adcp_processing_setting(self):
        """Test case for processing_get_adcp_processing_setting

        Get all adcp processing parameters for specific channel  # noqa: E501
        """
        pass

    def test_processing_get_adcp_processing_settings(self):
        """Test case for processing_get_adcp_processing_settings

        """
        pass

    def test_processing_get_bottom_detection_active(self):
        """Test case for processing_get_bottom_detection_active

        Check if bottom detection is on and off  # noqa: E501
        """
        pass

    def test_processing_set_bottom_detection_active(self):
        """Test case for processing_set_bottom_detection_active

        Turn on and off bottom detection  # noqa: E501
        """
        pass

    def test_processing_set_bottom_detection_backstep(self):
        """Test case for processing_set_bottom_detection_backstep

        Set the bottom backstep value for bottom detection  # noqa: E501
        """
        pass

    def test_processing_set_bottom_detection_maximum_depth(self):
        """Test case for processing_set_bottom_detection_maximum_depth

        Set range from where bottom detector should stop searching for bottom  # noqa: E501
        """
        pass

    def test_processing_set_bottom_detection_minimum_depth(self):
        """Test case for processing_set_bottom_detection_minimum_depth

        Set range from where bottom detector should start searching for bottom  # noqa: E501
        """
        pass

    def test_processing_set_correlation_limit_percentage(self):
        """Test case for processing_set_correlation_limit_percentage

        Set correlation percentage limit  # noqa: E501
        """
        pass

    def test_processing_set_error_velocity_limit(self):
        """Test case for processing_set_error_velocity_limit

        Set error velocity limit  # noqa: E501
        """
        pass

    def test_processing_set_error_velocity_limit_0(self):
        """Test case for processing_set_error_velocity_limit_0

        Activate or deactivate error velocity limit  # noqa: E501
        """
        pass

    def test_processing_set_is_correlation_limit_percentage_active(self):
        """Test case for processing_set_is_correlation_limit_percentage_active

        Activate or deactivate correlation percentage limit  # noqa: E501
        """
        pass

    def test_processing_set_is_min_quality_average_data_factor_active(self):
        """Test case for processing_set_is_min_quality_average_data_factor_active

        Activate or deactivate minimum quality average data factor  # noqa: E501
        """
        pass

    def test_processing_set_min_quality_average_data_percentage(self):
        """Test case for processing_set_min_quality_average_data_percentage

        Set minimum quality average data factor  # noqa: E501
        """
        pass

    def test_processing_set_svd_b_high_limit(self):
        """Test case for processing_set_svd_b_high_limit

        Set maximum limit for Sv  # noqa: E501
        """
        pass

    def test_processing_set_svd_b_high_limit_active(self):
        """Test case for processing_set_svd_b_high_limit_active

        Activate or deactivate test on maximum limit for Sv  # noqa: E501
        """
        pass

    def test_processing_set_svd_b_low_limit(self):
        """Test case for processing_set_svd_b_low_limit

        Set minimum limit for Sv  # noqa: E501
        """
        pass

    def test_processing_set_svd_b_low_limit_active(self):
        """Test case for processing_set_svd_b_low_limit_active

        Activate or deactivate test on minimum limit for Sv  # noqa: E501
        """
        pass

    def test_processing_set_use_epoch_time(self):
        """Test case for processing_set_use_epoch_time

        Switch between PC time or epoch time from transceiver  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()