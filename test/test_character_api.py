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
from eve_swagger_api.api.character_api import CharacterApi  # noqa: E501
from eve_swagger_api.rest import ApiException


class TestCharacterApi(unittest.TestCase):
    """CharacterApi unit test stubs"""

    def setUp(self):
        self.api = eve_swagger_api.api.character_api.CharacterApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_characters_character_id(self):
        """Test case for get_characters_character_id

        Get character's public information  # noqa: E501
        """
        pass

    def test_get_characters_character_id_agents_research(self):
        """Test case for get_characters_character_id_agents_research

        Get agents research  # noqa: E501
        """
        pass

    def test_get_characters_character_id_blueprints(self):
        """Test case for get_characters_character_id_blueprints

        Get blueprints  # noqa: E501
        """
        pass

    def test_get_characters_character_id_corporationhistory(self):
        """Test case for get_characters_character_id_corporationhistory

        Get corporation history  # noqa: E501
        """
        pass

    def test_get_characters_character_id_fatigue(self):
        """Test case for get_characters_character_id_fatigue

        Get jump fatigue  # noqa: E501
        """
        pass

    def test_get_characters_character_id_medals(self):
        """Test case for get_characters_character_id_medals

        Get medals  # noqa: E501
        """
        pass

    def test_get_characters_character_id_notifications(self):
        """Test case for get_characters_character_id_notifications

        Get character notifications  # noqa: E501
        """
        pass

    def test_get_characters_character_id_notifications_contacts(self):
        """Test case for get_characters_character_id_notifications_contacts

        Get new contact notifications  # noqa: E501
        """
        pass

    def test_get_characters_character_id_portrait(self):
        """Test case for get_characters_character_id_portrait

        Get character portraits  # noqa: E501
        """
        pass

    def test_get_characters_character_id_roles(self):
        """Test case for get_characters_character_id_roles

        Get character corporation roles  # noqa: E501
        """
        pass

    def test_get_characters_character_id_standings(self):
        """Test case for get_characters_character_id_standings

        Get standings  # noqa: E501
        """
        pass

    def test_get_characters_character_id_titles(self):
        """Test case for get_characters_character_id_titles

        Get character corporation titles  # noqa: E501
        """
        pass

    def test_post_characters_affiliation(self):
        """Test case for post_characters_affiliation

        Character affiliation  # noqa: E501
        """
        pass

    def test_post_characters_character_id_cspa(self):
        """Test case for post_characters_character_id_cspa

        Calculate a CSPA charge cost  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
