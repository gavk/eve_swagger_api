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


class GetIndustrySystems200Ok(object):
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
        'cost_indices': 'list[GetIndustrySystemsCostIndice]',
        'solar_system_id': 'int'
    }

    attribute_map = {
        'cost_indices': 'cost_indices',
        'solar_system_id': 'solar_system_id'
    }

    def __init__(self, cost_indices=None, solar_system_id=None, _configuration=None):  # noqa: E501
        """GetIndustrySystems200Ok - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._cost_indices = None
        self._solar_system_id = None
        self.discriminator = None

        self.cost_indices = cost_indices
        self.solar_system_id = solar_system_id

    @property
    def cost_indices(self):
        """Gets the cost_indices of this GetIndustrySystems200Ok.  # noqa: E501

        cost_indices array  # noqa: E501

        :return: The cost_indices of this GetIndustrySystems200Ok.  # noqa: E501
        :rtype: list[GetIndustrySystemsCostIndice]
        """
        return self._cost_indices

    @cost_indices.setter
    def cost_indices(self, cost_indices):
        """Sets the cost_indices of this GetIndustrySystems200Ok.

        cost_indices array  # noqa: E501

        :param cost_indices: The cost_indices of this GetIndustrySystems200Ok.  # noqa: E501
        :type: list[GetIndustrySystemsCostIndice]
        """
        if self._configuration.client_side_validation and cost_indices is None:
            raise ValueError("Invalid value for `cost_indices`, must not be `None`")  # noqa: E501

        self._cost_indices = cost_indices

    @property
    def solar_system_id(self):
        """Gets the solar_system_id of this GetIndustrySystems200Ok.  # noqa: E501

        solar_system_id integer  # noqa: E501

        :return: The solar_system_id of this GetIndustrySystems200Ok.  # noqa: E501
        :rtype: int
        """
        return self._solar_system_id

    @solar_system_id.setter
    def solar_system_id(self, solar_system_id):
        """Sets the solar_system_id of this GetIndustrySystems200Ok.

        solar_system_id integer  # noqa: E501

        :param solar_system_id: The solar_system_id of this GetIndustrySystems200Ok.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and solar_system_id is None:
            raise ValueError("Invalid value for `solar_system_id`, must not be `None`")  # noqa: E501

        self._solar_system_id = solar_system_id

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
        if issubclass(GetIndustrySystems200Ok, dict):
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
        if not isinstance(other, GetIndustrySystems200Ok):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetIndustrySystems200Ok):
            return True

        return self.to_dict() != other.to_dict()
