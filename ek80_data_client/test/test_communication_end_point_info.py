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
from ek80_data_client.models.communication_end_point_info import CommunicationEndPointInfo  # noqa: E501
from ek80_data_client.rest import ApiException


class TestCommunicationEndPointInfo(unittest.TestCase):
    """CommunicationEndPointInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCommunicationEndPointInfo(self):
        """Test CommunicationEndPointInfo"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ek80_data_client.models.communication_end_point_info.CommunicationEndPointInfo()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
