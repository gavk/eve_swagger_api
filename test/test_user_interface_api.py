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
from eve_swagger_api.api.user_interface_api import UserInterfaceApi  # noqa: E501
from eve_swagger_api.rest import ApiException


class TestUserInterfaceApi(unittest.TestCase):
    """UserInterfaceApi unit test stubs"""

    def setUp(self):
        self.api = eve_swagger_api.api.user_interface_api.UserInterfaceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_post_ui_autopilot_waypoint(self):
        """Test case for post_ui_autopilot_waypoint

        Set Autopilot Waypoint  # noqa: E501
        """
        pass

    def test_post_ui_openwindow_contract(self):
        """Test case for post_ui_openwindow_contract

        Open Contract Window  # noqa: E501
        """
        pass

    def test_post_ui_openwindow_information(self):
        """Test case for post_ui_openwindow_information

        Open Information Window  # noqa: E501
        """
        pass

    def test_post_ui_openwindow_marketdetails(self):
        """Test case for post_ui_openwindow_marketdetails

        Open Market Details  # noqa: E501
        """
        pass

    def test_post_ui_openwindow_newmail(self):
        """Test case for post_ui_openwindow_newmail

        Open New Mail Window  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
