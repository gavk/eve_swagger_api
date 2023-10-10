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


class GetCharactersCharacterIdFwStatsOk(object):
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
        'current_rank': 'int',
        'enlisted_on': 'datetime',
        'faction_id': 'int',
        'highest_rank': 'int',
        'kills': 'GetCharactersCharacterIdFwStatsKills',
        'victory_points': 'GetCharactersCharacterIdFwStatsVictoryPoints'
    }

    attribute_map = {
        'current_rank': 'current_rank',
        'enlisted_on': 'enlisted_on',
        'faction_id': 'faction_id',
        'highest_rank': 'highest_rank',
        'kills': 'kills',
        'victory_points': 'victory_points'
    }

    def __init__(self, current_rank=None, enlisted_on=None, faction_id=None, highest_rank=None, kills=None, victory_points=None, _configuration=None):  # noqa: E501
        """GetCharactersCharacterIdFwStatsOk - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._current_rank = None
        self._enlisted_on = None
        self._faction_id = None
        self._highest_rank = None
        self._kills = None
        self._victory_points = None
        self.discriminator = None

        if current_rank is not None:
            self.current_rank = current_rank
        if enlisted_on is not None:
            self.enlisted_on = enlisted_on
        if faction_id is not None:
            self.faction_id = faction_id
        if highest_rank is not None:
            self.highest_rank = highest_rank
        self.kills = kills
        self.victory_points = victory_points

    @property
    def current_rank(self):
        """Gets the current_rank of this GetCharactersCharacterIdFwStatsOk.  # noqa: E501

        The given character's current faction rank  # noqa: E501

        :return: The current_rank of this GetCharactersCharacterIdFwStatsOk.  # noqa: E501
        :rtype: int
        """
        return self._current_rank

    @current_rank.setter
    def current_rank(self, current_rank):
        """Sets the current_rank of this GetCharactersCharacterIdFwStatsOk.

        The given character's current faction rank  # noqa: E501

        :param current_rank: The current_rank of this GetCharactersCharacterIdFwStatsOk.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                current_rank is not None and current_rank > 9):  # noqa: E501
            raise ValueError("Invalid value for `current_rank`, must be a value less than or equal to `9`")  # noqa: E501
        if (self._configuration.client_side_validation and
                current_rank is not None and current_rank < 0):  # noqa: E501
            raise ValueError("Invalid value for `current_rank`, must be a value greater than or equal to `0`")  # noqa: E501

        self._current_rank = current_rank

    @property
    def enlisted_on(self):
        """Gets the enlisted_on of this GetCharactersCharacterIdFwStatsOk.  # noqa: E501

        The enlistment date of the given character into faction warfare. Will not be included if character is not enlisted in faction warfare  # noqa: E501

        :return: The enlisted_on of this GetCharactersCharacterIdFwStatsOk.  # noqa: E501
        :rtype: datetime
        """
        return self._enlisted_on

    @enlisted_on.setter
    def enlisted_on(self, enlisted_on):
        """Sets the enlisted_on of this GetCharactersCharacterIdFwStatsOk.

        The enlistment date of the given character into faction warfare. Will not be included if character is not enlisted in faction warfare  # noqa: E501

        :param enlisted_on: The enlisted_on of this GetCharactersCharacterIdFwStatsOk.  # noqa: E501
        :type: datetime
        """

        self._enlisted_on = enlisted_on

    @property
    def faction_id(self):
        """Gets the faction_id of this GetCharactersCharacterIdFwStatsOk.  # noqa: E501

        The faction the given character is enlisted to fight for. Will not be included if character is not enlisted in faction warfare  # noqa: E501

        :return: The faction_id of this GetCharactersCharacterIdFwStatsOk.  # noqa: E501
        :rtype: int
        """
        return self._faction_id

    @faction_id.setter
    def faction_id(self, faction_id):
        """Sets the faction_id of this GetCharactersCharacterIdFwStatsOk.

        The faction the given character is enlisted to fight for. Will not be included if character is not enlisted in faction warfare  # noqa: E501

        :param faction_id: The faction_id of this GetCharactersCharacterIdFwStatsOk.  # noqa: E501
        :type: int
        """

        self._faction_id = faction_id

    @property
    def highest_rank(self):
        """Gets the highest_rank of this GetCharactersCharacterIdFwStatsOk.  # noqa: E501

        The given character's highest faction rank achieved  # noqa: E501

        :return: The highest_rank of this GetCharactersCharacterIdFwStatsOk.  # noqa: E501
        :rtype: int
        """
        return self._highest_rank

    @highest_rank.setter
    def highest_rank(self, highest_rank):
        """Sets the highest_rank of this GetCharactersCharacterIdFwStatsOk.

        The given character's highest faction rank achieved  # noqa: E501

        :param highest_rank: The highest_rank of this GetCharactersCharacterIdFwStatsOk.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                highest_rank is not None and highest_rank > 9):  # noqa: E501
            raise ValueError("Invalid value for `highest_rank`, must be a value less than or equal to `9`")  # noqa: E501
        if (self._configuration.client_side_validation and
                highest_rank is not None and highest_rank < 0):  # noqa: E501
            raise ValueError("Invalid value for `highest_rank`, must be a value greater than or equal to `0`")  # noqa: E501

        self._highest_rank = highest_rank

    @property
    def kills(self):
        """Gets the kills of this GetCharactersCharacterIdFwStatsOk.  # noqa: E501


        :return: The kills of this GetCharactersCharacterIdFwStatsOk.  # noqa: E501
        :rtype: GetCharactersCharacterIdFwStatsKills
        """
        return self._kills

    @kills.setter
    def kills(self, kills):
        """Sets the kills of this GetCharactersCharacterIdFwStatsOk.


        :param kills: The kills of this GetCharactersCharacterIdFwStatsOk.  # noqa: E501
        :type: GetCharactersCharacterIdFwStatsKills
        """
        if self._configuration.client_side_validation and kills is None:
            raise ValueError("Invalid value for `kills`, must not be `None`")  # noqa: E501

        self._kills = kills

    @property
    def victory_points(self):
        """Gets the victory_points of this GetCharactersCharacterIdFwStatsOk.  # noqa: E501


        :return: The victory_points of this GetCharactersCharacterIdFwStatsOk.  # noqa: E501
        :rtype: GetCharactersCharacterIdFwStatsVictoryPoints
        """
        return self._victory_points

    @victory_points.setter
    def victory_points(self, victory_points):
        """Sets the victory_points of this GetCharactersCharacterIdFwStatsOk.


        :param victory_points: The victory_points of this GetCharactersCharacterIdFwStatsOk.  # noqa: E501
        :type: GetCharactersCharacterIdFwStatsVictoryPoints
        """
        if self._configuration.client_side_validation and victory_points is None:
            raise ValueError("Invalid value for `victory_points`, must not be `None`")  # noqa: E501

        self._victory_points = victory_points

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
        if issubclass(GetCharactersCharacterIdFwStatsOk, dict):
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
        if not isinstance(other, GetCharactersCharacterIdFwStatsOk):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetCharactersCharacterIdFwStatsOk):
            return True

        return self.to_dict() != other.to_dict()
