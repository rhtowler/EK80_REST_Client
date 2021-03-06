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
from ek80_param_client.api.installed_transceivers_api import InstalledTransceiversApi  # noqa: E501
from ek80_param_client.rest import ApiException


class TestInstalledTransceiversApi(unittest.TestCase):
    """InstalledTransceiversApi unit test stubs"""

    def setUp(self):
        self.api = ek80_param_client.api.installed_transceivers_api.InstalledTransceiversApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_echo_sounder_transducers_get_acoustic_source(self):
        """Test case for echo_sounder_transducers_get_acoustic_source

        Get information about a specific installed transceiver  # noqa: E501
        """
        pass

    def test_echo_sounder_transducers_get_acoustic_source_0(self):
        """Test case for echo_sounder_transducers_get_acoustic_source_0

        Get information about a specific installed transceiver  # noqa: E501
        """
        pass

    def test_echo_sounder_transducers_get_acoustic_sources(self):
        """Test case for echo_sounder_transducers_get_acoustic_sources

        Get information about all installed transceivers  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
