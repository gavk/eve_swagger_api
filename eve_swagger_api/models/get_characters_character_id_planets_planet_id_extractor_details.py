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


class GetCharactersCharacterIdPlanetsPlanetIdExtractorDetails(object):
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
        'cycle_time': 'int',
        'head_radius': 'float',
        'heads': 'list[GetCharactersCharacterIdPlanetsPlanetIdHead]',
        'product_type_id': 'int',
        'qty_per_cycle': 'int'
    }

    attribute_map = {
        'cycle_time': 'cycle_time',
        'head_radius': 'head_radius',
        'heads': 'heads',
        'product_type_id': 'product_type_id',
        'qty_per_cycle': 'qty_per_cycle'
    }

    def __init__(self, cycle_time=None, head_radius=None, heads=None, product_type_id=None, qty_per_cycle=None, _configuration=None):  # noqa: E501
        """GetCharactersCharacterIdPlanetsPlanetIdExtractorDetails - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._cycle_time = None
        self._head_radius = None
        self._heads = None
        self._product_type_id = None
        self._qty_per_cycle = None
        self.discriminator = None

        if cycle_time is not None:
            self.cycle_time = cycle_time
        if head_radius is not None:
            self.head_radius = head_radius
        self.heads = heads
        if product_type_id is not None:
            self.product_type_id = product_type_id
        if qty_per_cycle is not None:
            self.qty_per_cycle = qty_per_cycle

    @property
    def cycle_time(self):
        """Gets the cycle_time of this GetCharactersCharacterIdPlanetsPlanetIdExtractorDetails.  # noqa: E501

        in seconds  # noqa: E501

        :return: The cycle_time of this GetCharactersCharacterIdPlanetsPlanetIdExtractorDetails.  # noqa: E501
        :rtype: int
        """
        return self._cycle_time

    @cycle_time.setter
    def cycle_time(self, cycle_time):
        """Sets the cycle_time of this GetCharactersCharacterIdPlanetsPlanetIdExtractorDetails.

        in seconds  # noqa: E501

        :param cycle_time: The cycle_time of this GetCharactersCharacterIdPlanetsPlanetIdExtractorDetails.  # noqa: E501
        :type: int
        """

        self._cycle_time = cycle_time

    @property
    def head_radius(self):
        """Gets the head_radius of this GetCharactersCharacterIdPlanetsPlanetIdExtractorDetails.  # noqa: E501

        head_radius number  # noqa: E501

        :return: The head_radius of this GetCharactersCharacterIdPlanetsPlanetIdExtractorDetails.  # noqa: E501
        :rtype: float
        """
        return self._head_radius

    @head_radius.setter
    def head_radius(self, head_radius):
        """Sets the head_radius of this GetCharactersCharacterIdPlanetsPlanetIdExtractorDetails.

        head_radius number  # noqa: E501

        :param head_radius: The head_radius of this GetCharactersCharacterIdPlanetsPlanetIdExtractorDetails.  # noqa: E501
        :type: float
        """

        self._head_radius = head_radius

    @property
    def heads(self):
        """Gets the heads of this GetCharactersCharacterIdPlanetsPlanetIdExtractorDetails.  # noqa: E501

        heads array  # noqa: E501

        :return: The heads of this GetCharactersCharacterIdPlanetsPlanetIdExtractorDetails.  # noqa: E501
        :rtype: list[GetCharactersCharacterIdPlanetsPlanetIdHead]
        """
        return self._heads

    @heads.setter
    def heads(self, heads):
        """Sets the heads of this GetCharactersCharacterIdPlanetsPlanetIdExtractorDetails.

        heads array  # noqa: E501

        :param heads: The heads of this GetCharactersCharacterIdPlanetsPlanetIdExtractorDetails.  # noqa: E501
        :type: list[GetCharactersCharacterIdPlanetsPlanetIdHead]
        """
        if self._configuration.client_side_validation and heads is None:
            raise ValueError("Invalid value for `heads`, must not be `None`")  # noqa: E501

        self._heads = heads

    @property
    def product_type_id(self):
        """Gets the product_type_id of this GetCharactersCharacterIdPlanetsPlanetIdExtractorDetails.  # noqa: E501

        product_type_id integer  # noqa: E501

        :return: The product_type_id of this GetCharactersCharacterIdPlanetsPlanetIdExtractorDetails.  # noqa: E501
        :rtype: int
        """
        return self._product_type_id

    @product_type_id.setter
    def product_type_id(self, product_type_id):
        """Sets the product_type_id of this GetCharactersCharacterIdPlanetsPlanetIdExtractorDetails.

        product_type_id integer  # noqa: E501

        :param product_type_id: The product_type_id of this GetCharactersCharacterIdPlanetsPlanetIdExtractorDetails.  # noqa: E501
        :type: int
        """

        self._product_type_id = product_type_id

    @property
    def qty_per_cycle(self):
        """Gets the qty_per_cycle of this GetCharactersCharacterIdPlanetsPlanetIdExtractorDetails.  # noqa: E501

        qty_per_cycle integer  # noqa: E501

        :return: The qty_per_cycle of this GetCharactersCharacterIdPlanetsPlanetIdExtractorDetails.  # noqa: E501
        :rtype: int
        """
        return self._qty_per_cycle

    @qty_per_cycle.setter
    def qty_per_cycle(self, qty_per_cycle):
        """Sets the qty_per_cycle of this GetCharactersCharacterIdPlanetsPlanetIdExtractorDetails.

        qty_per_cycle integer  # noqa: E501

        :param qty_per_cycle: The qty_per_cycle of this GetCharactersCharacterIdPlanetsPlanetIdExtractorDetails.  # noqa: E501
        :type: int
        """

        self._qty_per_cycle = qty_per_cycle

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
        if issubclass(GetCharactersCharacterIdPlanetsPlanetIdExtractorDetails, dict):
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
        if not isinstance(other, GetCharactersCharacterIdPlanetsPlanetIdExtractorDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetCharactersCharacterIdPlanetsPlanetIdExtractorDetails):
            return True

        return self.to_dict() != other.to_dict()
