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


class GetInsurancePrices200Ok(object):
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
        'levels': 'list[GetInsurancePricesLevel]',
        'type_id': 'int'
    }

    attribute_map = {
        'levels': 'levels',
        'type_id': 'type_id'
    }

    def __init__(self, levels=None, type_id=None, _configuration=None):  # noqa: E501
        """GetInsurancePrices200Ok - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._levels = None
        self._type_id = None
        self.discriminator = None

        self.levels = levels
        self.type_id = type_id

    @property
    def levels(self):
        """Gets the levels of this GetInsurancePrices200Ok.  # noqa: E501

        A list of a available insurance levels for this ship type  # noqa: E501

        :return: The levels of this GetInsurancePrices200Ok.  # noqa: E501
        :rtype: list[GetInsurancePricesLevel]
        """
        return self._levels

    @levels.setter
    def levels(self, levels):
        """Sets the levels of this GetInsurancePrices200Ok.

        A list of a available insurance levels for this ship type  # noqa: E501

        :param levels: The levels of this GetInsurancePrices200Ok.  # noqa: E501
        :type: list[GetInsurancePricesLevel]
        """
        if self._configuration.client_side_validation and levels is None:
            raise ValueError("Invalid value for `levels`, must not be `None`")  # noqa: E501

        self._levels = levels

    @property
    def type_id(self):
        """Gets the type_id of this GetInsurancePrices200Ok.  # noqa: E501

        type_id integer  # noqa: E501

        :return: The type_id of this GetInsurancePrices200Ok.  # noqa: E501
        :rtype: int
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """Sets the type_id of this GetInsurancePrices200Ok.

        type_id integer  # noqa: E501

        :param type_id: The type_id of this GetInsurancePrices200Ok.  # noqa: E501
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
        if issubclass(GetInsurancePrices200Ok, dict):
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
        if not isinstance(other, GetInsurancePrices200Ok):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetInsurancePrices200Ok):
            return True

        return self.to_dict() != other.to_dict()
