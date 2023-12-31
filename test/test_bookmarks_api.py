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
from eve_swagger_api.api.bookmarks_api import BookmarksApi  # noqa: E501
from eve_swagger_api.rest import ApiException


class TestBookmarksApi(unittest.TestCase):
    """BookmarksApi unit test stubs"""

    def setUp(self):
        self.api = eve_swagger_api.api.bookmarks_api.BookmarksApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_characters_character_id_bookmarks(self):
        """Test case for get_characters_character_id_bookmarks

        List bookmarks  # noqa: E501
        """
        pass

    def test_get_characters_character_id_bookmarks_folders(self):
        """Test case for get_characters_character_id_bookmarks_folders

        List bookmark folders  # noqa: E501
        """
        pass

    def test_get_corporations_corporation_id_bookmarks(self):
        """Test case for get_corporations_corporation_id_bookmarks

        List corporation bookmarks  # noqa: E501
        """
        pass

    def test_get_corporations_corporation_id_bookmarks_folders(self):
        """Test case for get_corporations_corporation_id_bookmarks_folders

        List corporation bookmark folders  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
