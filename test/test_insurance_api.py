# coding: utf-8

"""
    EVE Swagger Interface

    An OpenAPI for EVE Online  # noqa: E501

    OpenAPI spec version: 1.19
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import eve_swagger_api
from eve_swagger_api.api.insurance_api import InsuranceApi  # noqa: E501
from eve_swagger_api.rest import ApiException


class TestInsuranceApi(unittest.TestCase):
    """InsuranceApi unit test stubs"""

    def setUp(self):
        self.api = eve_swagger_api.api.insurance_api.InsuranceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_insurance_prices(self):
        """Test case for get_insurance_prices

        List insurance levels  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
