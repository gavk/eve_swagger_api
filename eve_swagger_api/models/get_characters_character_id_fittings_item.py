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


class GetCharactersCharacterIdFittingsItem(object):
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
        'flag': 'str',
        'quantity': 'int',
        'type_id': 'int'
    }

    attribute_map = {
        'flag': 'flag',
        'quantity': 'quantity',
        'type_id': 'type_id'
    }

    def __init__(self, flag=None, quantity=None, type_id=None, _configuration=None):  # noqa: E501
        """GetCharactersCharacterIdFittingsItem - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._flag = None
        self._quantity = None
        self._type_id = None
        self.discriminator = None

        self.flag = flag
        self.quantity = quantity
        self.type_id = type_id

    @property
    def flag(self):
        """Gets the flag of this GetCharactersCharacterIdFittingsItem.  # noqa: E501

        flag string  # noqa: E501

        :return: The flag of this GetCharactersCharacterIdFittingsItem.  # noqa: E501
        :rtype: str
        """
        return self._flag

    @flag.setter
    def flag(self, flag):
        """Sets the flag of this GetCharactersCharacterIdFittingsItem.

        flag string  # noqa: E501

        :param flag: The flag of this GetCharactersCharacterIdFittingsItem.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and flag is None:
            raise ValueError("Invalid value for `flag`, must not be `None`")  # noqa: E501
        allowed_values = ["Cargo", "DroneBay", "FighterBay", "HiSlot0", "HiSlot1", "HiSlot2", "HiSlot3", "HiSlot4", "HiSlot5", "HiSlot6", "HiSlot7", "Invalid", "LoSlot0", "LoSlot1", "LoSlot2", "LoSlot3", "LoSlot4", "LoSlot5", "LoSlot6", "LoSlot7", "MedSlot0", "MedSlot1", "MedSlot2", "MedSlot3", "MedSlot4", "MedSlot5", "MedSlot6", "MedSlot7", "RigSlot0", "RigSlot1", "RigSlot2", "ServiceSlot0", "ServiceSlot1", "ServiceSlot2", "ServiceSlot3", "ServiceSlot4", "ServiceSlot5", "ServiceSlot6", "ServiceSlot7", "SubSystemSlot0", "SubSystemSlot1", "SubSystemSlot2", "SubSystemSlot3"]  # noqa: E501
        if (self._configuration.client_side_validation and
                flag not in allowed_values):
            raise ValueError(
                "Invalid value for `flag` ({0}), must be one of {1}"  # noqa: E501
                .format(flag, allowed_values)
            )

        self._flag = flag

    @property
    def quantity(self):
        """Gets the quantity of this GetCharactersCharacterIdFittingsItem.  # noqa: E501

        quantity integer  # noqa: E501

        :return: The quantity of this GetCharactersCharacterIdFittingsItem.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this GetCharactersCharacterIdFittingsItem.

        quantity integer  # noqa: E501

        :param quantity: The quantity of this GetCharactersCharacterIdFittingsItem.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and quantity is None:
            raise ValueError("Invalid value for `quantity`, must not be `None`")  # noqa: E501

        self._quantity = quantity

    @property
    def type_id(self):
        """Gets the type_id of this GetCharactersCharacterIdFittingsItem.  # noqa: E501

        type_id integer  # noqa: E501

        :return: The type_id of this GetCharactersCharacterIdFittingsItem.  # noqa: E501
        :rtype: int
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """Sets the type_id of this GetCharactersCharacterIdFittingsItem.

        type_id integer  # noqa: E501

        :param type_id: The type_id of this GetCharactersCharacterIdFittingsItem.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and type_id is None:
            raise ValueError("Invalid value for `type_id`, must not be `None`")  # noqa: E501

        self._type_id = type_id

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
        if issubclass(GetCharactersCharacterIdFittingsItem, dict):
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
        if not isinstance(other, GetCharactersCharacterIdFittingsItem):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetCharactersCharacterIdFittingsItem):
            return True

        return self.to_dict() != other.to_dict()
