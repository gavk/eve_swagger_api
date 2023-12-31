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
from eve_swagger_api.api.killmails_api import KillmailsApi  # noqa: E501
from eve_swagger_api.rest import ApiException


class TestKillmailsApi(unittest.TestCase):
    """KillmailsApi unit test stubs"""

    def setUp(self):
        self.api = eve_swagger_api.api.killmails_api.KillmailsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_characters_character_id_killmails_recent(self):
        """Test case for get_characters_character_id_killmails_recent

        Get a character's recent kills and losses  # noqa: E501
        """
        pass

    def test_get_corporations_corporation_id_killmails_recent(self):
        """Test case for get_corporations_corporation_id_killmails_recent

        Get a corporation's recent kills and losses  # noqa: E501
        """
        pass

    def test_get_killmails_killmail_id_killmail_hash(self):
        """Test case for get_killmails_killmail_id_killmail_hash

        Get a single killmail  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
