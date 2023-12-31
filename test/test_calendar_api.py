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
from eve_swagger_api.api.calendar_api import CalendarApi  # noqa: E501
from eve_swagger_api.rest import ApiException


class TestCalendarApi(unittest.TestCase):
    """CalendarApi unit test stubs"""

    def setUp(self):
        self.api = eve_swagger_api.api.calendar_api.CalendarApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_characters_character_id_calendar(self):
        """Test case for get_characters_character_id_calendar

        List calendar event summaries  # noqa: E501
        """
        pass

    def test_get_characters_character_id_calendar_event_id(self):
        """Test case for get_characters_character_id_calendar_event_id

        Get an event  # noqa: E501
        """
        pass

    def test_get_characters_character_id_calendar_event_id_attendees(self):
        """Test case for get_characters_character_id_calendar_event_id_attendees

        Get attendees  # noqa: E501
        """
        pass

    def test_put_characters_character_id_calendar_event_id(self):
        """Test case for put_characters_character_id_calendar_event_id

        Respond to an event  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
