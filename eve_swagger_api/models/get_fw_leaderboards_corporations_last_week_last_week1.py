# coding: utf-8

"""
    EVE Swagger Interface

    An OpenAPI for EVE Online  # noqa: E501

    OpenAPI spec version: 1.19
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from eve_swagger_api.configuration import Configuration


class GetFwLeaderboardsCorporationsLastWeekLastWeek1(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'amount': 'int',
        'corporation_id': 'int'
    }

    attribute_map = {
        'amount': 'amount',
        'corporation_id': 'corporation_id'
    }

    def __init__(self, amount=None, corporation_id=None, _configuration=None):  # noqa: E501
        """GetFwLeaderboardsCorporationsLastWeekLastWeek1 - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._amount = None
        self._corporation_id = None
        self.discriminator = None

        if amount is not None:
            self.amount = amount
        if corporation_id is not None:
            self.corporation_id = corporation_id

    @property
    def amount(self):
        """Gets the amount of this GetFwLeaderboardsCorporationsLastWeekLastWeek1.  # noqa: E501

        Amount of victory points  # noqa: E501

        :return: The amount of this GetFwLeaderboardsCorporationsLastWeekLastWeek1.  # noqa: E501
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this GetFwLeaderboardsCorporationsLastWeekLastWeek1.

        Amount of victory points  # noqa: E501

        :param amount: The amount of this GetFwLeaderboardsCorporationsLastWeekLastWeek1.  # noqa: E501
        :type: int
        """

        self._amount = amount

    @property
    def corporation_id(self):
        """Gets the corporation_id of this GetFwLeaderboardsCorporationsLastWeekLastWeek1.  # noqa: E501

        corporation_id integer  # noqa: E501

        :return: The corporation_id of this GetFwLeaderboardsCorporationsLastWeekLastWeek1.  # noqa: E501
        :rtype: int
        """
        return self._corporation_id

    @corporation_id.setter
    def corporation_id(self, corporation_id):
        """Sets the corporation_id of this GetFwLeaderboardsCorporationsLastWeekLastWeek1.

        corporation_id integer  # noqa: E501

        :param corporation_id: The corporation_id of this GetFwLeaderboardsCorporationsLastWeekLastWeek1.  # noqa: E501
        :type: int
        """

        self._corporation_id = corporation_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(GetFwLeaderboardsCorporationsLastWeekLastWeek1, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GetFwLeaderboardsCorporationsLastWeekLastWeek1):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetFwLeaderboardsCorporationsLastWeekLastWeek1):
            return True

        return self.to_dict() != other.to_dict()
