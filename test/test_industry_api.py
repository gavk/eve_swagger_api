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
from eve_swagger_api.api.industry_api import IndustryApi  # noqa: E501
from eve_swagger_api.rest import ApiException


class TestIndustryApi(unittest.TestCase):
    """IndustryApi unit test stubs"""

    def setUp(self):
        self.api = eve_swagger_api.api.industry_api.IndustryApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_characters_character_id_industry_jobs(self):
        """Test case for get_characters_character_id_industry_jobs

        List character industry jobs  # noqa: E501
        """
        pass

    def test_get_characters_character_id_mining(self):
        """Test case for get_characters_character_id_mining

        Character mining ledger  # noqa: E501
        """
        pass

    def test_get_corporation_corporation_id_mining_extractions(self):
        """Test case for get_corporation_corporation_id_mining_extractions

        Moon extraction timers  # noqa: E501
        """
        pass

    def test_get_corporation_corporation_id_mining_observers(self):
        """Test case for get_corporation_corporation_id_mining_observers

        Corporation mining observers  # noqa: E501
        """
        pass

    def test_get_corporation_corporation_id_mining_observers_observer_id(self):
        """Test case for get_corporation_corporation_id_mining_observers_observer_id

        Observed corporation mining  # noqa: E501
        """
        pass

    def test_get_corporations_corporation_id_industry_jobs(self):
        """Test case for get_corporations_corporation_id_industry_jobs

        List corporation industry jobs  # noqa: E501
        """
        pass

    def test_get_industry_facilities(self):
        """Test case for get_industry_facilities

        List industry facilities  # noqa: E501
        """
        pass

    def test_get_industry_systems(self):
        """Test case for get_industry_systems

        List solar system cost indices  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
