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


class PostUniverseIdsOk(object):
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
        'agents': 'list[PostUniverseIdsAgent]',
        'alliances': 'list[PostUniverseIdsAlliance]',
        'characters': 'list[PostUniverseIdsCharacter]',
        'constellations': 'list[PostUniverseIdsConstellation]',
        'corporations': 'list[PostUniverseIdsCorporation]',
        'factions': 'list[PostUniverseIdsFaction]',
        'inventory_types': 'list[PostUniverseIdsInventoryType]',
        'regions': 'list[PostUniverseIdsRegion]',
        'stations': 'list[PostUniverseIdsStation]',
        'systems': 'list[PostUniverseIdsSystem]'
    }

    attribute_map = {
        'agents': 'agents',
        'alliances': 'alliances',
        'characters': 'characters',
        'constellations': 'constellations',
        'corporations': 'corporations',
        'factions': 'factions',
        'inventory_types': 'inventory_types',
        'regions': 'regions',
        'stations': 'stations',
        'systems': 'systems'
    }

    def __init__(self, agents=None, alliances=None, characters=None, constellations=None, corporations=None, factions=None, inventory_types=None, regions=None, stations=None, systems=None, _configuration=None):  # noqa: E501
        """PostUniverseIdsOk - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._agents = None
        self._alliances = None
        self._characters = None
        self._constellations = None
        self._corporations = None
        self._factions = None
        self._inventory_types = None
        self._regions = None
        self._stations = None
        self._systems = None
        self.discriminator = None

        if agents is not None:
            self.agents = agents
        if alliances is not None:
            self.alliances = alliances
        if characters is not None:
            self.characters = characters
        if constellations is not None:
            self.constellations = constellations
        if corporations is not None:
            self.corporations = corporations
        if factions is not None:
            self.factions = factions
        if inventory_types is not None:
            self.inventory_types = inventory_types
        if regions is not None:
            self.regions = regions
        if stations is not None:
            self.stations = stations
        if systems is not None:
            self.systems = systems

    @property
    def agents(self):
        """Gets the agents of this PostUniverseIdsOk.  # noqa: E501

        agents array  # noqa: E501

        :return: The agents of this PostUniverseIdsOk.  # noqa: E501
        :rtype: list[PostUniverseIdsAgent]
        """
        return self._agents

    @agents.setter
    def agents(self, agents):
        """Sets the agents of this PostUniverseIdsOk.

        agents array  # noqa: E501

        :param agents: The agents of this PostUniverseIdsOk.  # noqa: E501
        :type: list[PostUniverseIdsAgent]
        """

        self._agents = agents

    @property
    def alliances(self):
        """Gets the alliances of this PostUniverseIdsOk.  # noqa: E501

        alliances array  # noqa: E501

        :return: The alliances of this PostUniverseIdsOk.  # noqa: E501
        :rtype: list[PostUniverseIdsAlliance]
        """
        return self._alliances

    @alliances.setter
    def alliances(self, alliances):
        """Sets the alliances of this PostUniverseIdsOk.

        alliances array  # noqa: E501

        :param alliances: The alliances of this PostUniverseIdsOk.  # noqa: E501
        :type: list[PostUniverseIdsAlliance]
        """

        self._alliances = alliances

    @property
    def characters(self):
        """Gets the characters of this PostUniverseIdsOk.  # noqa: E501

        characters array  # noqa: E501

        :return: The characters of this PostUniverseIdsOk.  # noqa: E501
        :rtype: list[PostUniverseIdsCharacter]
        """
        return self._characters

    @characters.setter
    def characters(self, characters):
        """Sets the characters of this PostUniverseIdsOk.

        characters array  # noqa: E501

        :param characters: The characters of this PostUniverseIdsOk.  # noqa: E501
        :type: list[PostUniverseIdsCharacter]
        """

        self._characters = characters

    @property
    def constellations(self):
        """Gets the constellations of this PostUniverseIdsOk.  # noqa: E501

        constellations array  # noqa: E501

        :return: The constellations of this PostUniverseIdsOk.  # noqa: E501
        :rtype: list[PostUniverseIdsConstellation]
        """
        return self._constellations

    @constellations.setter
    def constellations(self, constellations):
        """Sets the constellations of this PostUniverseIdsOk.

        constellations array  # noqa: E501

        :param constellations: The constellations of this PostUniverseIdsOk.  # noqa: E501
        :type: list[PostUniverseIdsConstellation]
        """

        self._constellations = constellations

    @property
    def corporations(self):
        """Gets the corporations of this PostUniverseIdsOk.  # noqa: E501

        corporations array  # noqa: E501

        :return: The corporations of this PostUniverseIdsOk.  # noqa: E501
        :rtype: list[PostUniverseIdsCorporation]
        """
        return self._corporations

    @corporations.setter
    def corporations(self, corporations):
        """Sets the corporations of this PostUniverseIdsOk.

        corporations array  # noqa: E501

        :param corporations: The corporations of this PostUniverseIdsOk.  # noqa: E501
        :type: list[PostUniverseIdsCorporation]
        """

        self._corporations = corporations

    @property
    def factions(self):
        """Gets the factions of this PostUniverseIdsOk.  # noqa: E501

        factions array  # noqa: E501

        :return: The factions of this PostUniverseIdsOk.  # noqa: E501
        :rtype: list[PostUniverseIdsFaction]
        """
        return self._factions

    @factions.setter
    def factions(self, factions):
        """Sets the factions of this PostUniverseIdsOk.

        factions array  # noqa: E501

        :param factions: The factions of this PostUniverseIdsOk.  # noqa: E501
        :type: list[PostUniverseIdsFaction]
        """

        self._factions = factions

    @property
    def inventory_types(self):
        """Gets the inventory_types of this PostUniverseIdsOk.  # noqa: E501

        inventory_types array  # noqa: E501

        :return: The inventory_types of this PostUniverseIdsOk.  # noqa: E501
        :rtype: list[PostUniverseIdsInventoryType]
        """
        return self._inventory_types

    @inventory_types.setter
    def inventory_types(self, inventory_types):
        """Sets the inventory_types of this PostUniverseIdsOk.

        inventory_types array  # noqa: E501

        :param inventory_types: The inventory_types of this PostUniverseIdsOk.  # noqa: E501
        :type: list[PostUniverseIdsInventoryType]
        """

        self._inventory_types = inventory_types

    @property
    def regions(self):
        """Gets the regions of this PostUniverseIdsOk.  # noqa: E501

        regions array  # noqa: E501

        :return: The regions of this PostUniverseIdsOk.  # noqa: E501
        :rtype: list[PostUniverseIdsRegion]
        """
        return self._regions

    @regions.setter
    def regions(self, regions):
        """Sets the regions of this PostUniverseIdsOk.

        regions array  # noqa: E501

        :param regions: The regions of this PostUniverseIdsOk.  # noqa: E501
        :type: list[PostUniverseIdsRegion]
        """

        self._regions = regions

    @property
    def stations(self):
        """Gets the stations of this PostUniverseIdsOk.  # noqa: E501

        stations array  # noqa: E501

        :return: The stations of this PostUniverseIdsOk.  # noqa: E501
        :rtype: list[PostUniverseIdsStation]
        """
        return self._stations

    @stations.setter
    def stations(self, stations):
        """Sets the stations of this PostUniverseIdsOk.

        stations array  # noqa: E501

        :param stations: The stations of this PostUniverseIdsOk.  # noqa: E501
        :type: list[PostUniverseIdsStation]
        """

        self._stations = stations

    @property
    def systems(self):
        """Gets the systems of this PostUniverseIdsOk.  # noqa: E501

        systems array  # noqa: E501

        :return: The systems of this PostUniverseIdsOk.  # noqa: E501
        :rtype: list[PostUniverseIdsSystem]
        """
        return self._systems

    @systems.setter
    def systems(self, systems):
        """Sets the systems of this PostUniverseIdsOk.

        systems array  # noqa: E501

        :param systems: The systems of this PostUniverseIdsOk.  # noqa: E501
        :type: list[PostUniverseIdsSystem]
        """

        self._systems = systems

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
        if issubclass(PostUniverseIdsOk, dict):
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
        if not isinstance(other, PostUniverseIdsOk):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PostUniverseIdsOk):
            return True

        return self.to_dict() != other.to_dict()
