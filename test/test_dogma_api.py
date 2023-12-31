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
from eve_swagger_api.api.dogma_api import DogmaApi  # noqa: E501
from eve_swagger_api.rest import ApiException


class TestDogmaApi(unittest.TestCase):
    """DogmaApi unit test stubs"""

    def setUp(self):
        self.api = eve_swagger_api.api.dogma_api.DogmaApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_dogma_attributes(self):
        """Test case for get_dogma_attributes

        Get attributes  # noqa: E501
        """
        pass

    def test_get_dogma_attributes_attribute_id(self):
        """Test case for get_dogma_attributes_attribute_id

        Get attribute information  # noqa: E501
        """
        pass

    def test_get_dogma_dynamic_items_type_id_item_id(self):
        """Test case for get_dogma_dynamic_items_type_id_item_id

        Get dynamic item information  # noqa: E501
        """
        pass

    def test_get_dogma_effects(self):
        """Test case for get_dogma_effects

        Get effects  # noqa: E501
        """
        pass

    def test_get_dogma_effects_effect_id(self):
        """Test case for get_dogma_effects_effect_id

        Get effect information  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
