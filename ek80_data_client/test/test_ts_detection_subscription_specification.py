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
from ek80_data_client.models.ts_detection_subscription_specification import TsDetectionSubscriptionSpecification  # noqa: E501
from ek80_data_client.rest import ApiException


class TestTsDetectionSubscriptionSpecification(unittest.TestCase):
    """TsDetectionSubscriptionSpecification unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTsDetectionSubscriptionSpecification(self):
        """Test TsDetectionSubscriptionSpecification"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ek80_data_client.models.ts_detection_subscription_specification.TsDetectionSubscriptionSpecification()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
