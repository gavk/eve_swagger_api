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


class GetOpportunitiesTasksTaskIdOk(object):
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
        'description': 'str',
        'name': 'str',
        'notification': 'str',
        'task_id': 'int'
    }

    attribute_map = {
        'description': 'description',
        'name': 'name',
        'notification': 'notification',
        'task_id': 'task_id'
    }

    def __init__(self, description=None, name=None, notification=None, task_id=None, _configuration=None):  # noqa: E501
        """GetOpportunitiesTasksTaskIdOk - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._description = None
        self._name = None
        self._notification = None
        self._task_id = None
        self.discriminator = None

        self.description = description
        self.name = name
        self.notification = notification
        self.task_id = task_id

    @property
    def description(self):
        """Gets the description of this GetOpportunitiesTasksTaskIdOk.  # noqa: E501

        description string  # noqa: E501

        :return: The description of this GetOpportunitiesTasksTaskIdOk.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this GetOpportunitiesTasksTaskIdOk.

        description string  # noqa: E501

        :param description: The description of this GetOpportunitiesTasksTaskIdOk.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def name(self):
        """Gets the name of this GetOpportunitiesTasksTaskIdOk.  # noqa: E501

        name string  # noqa: E501

        :return: The name of this GetOpportunitiesTasksTaskIdOk.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetOpportunitiesTasksTaskIdOk.

        name string  # noqa: E501

        :param name: The name of this GetOpportunitiesTasksTaskIdOk.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def notification(self):
        """Gets the notification of this GetOpportunitiesTasksTaskIdOk.  # noqa: E501

        notification string  # noqa: E501

        :return: The notification of this GetOpportunitiesTasksTaskIdOk.  # noqa: E501
        :rtype: str
        """
        return self._notification

    @notification.setter
    def notification(self, notification):
        """Sets the notification of this GetOpportunitiesTasksTaskIdOk.

        notification string  # noqa: E501

        :param notification: The notification of this GetOpportunitiesTasksTaskIdOk.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and notification is None:
            raise ValueError("Invalid value for `notification`, must not be `None`")  # noqa: E501

        self._notification = notification

    @property
    def task_id(self):
        """Gets the task_id of this GetOpportunitiesTasksTaskIdOk.  # noqa: E501

        task_id integer  # noqa: E501

        :return: The task_id of this GetOpportunitiesTasksTaskIdOk.  # noqa: E501
        :rtype: int
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this GetOpportunitiesTasksTaskIdOk.

        task_id integer  # noqa: E501

        :param task_id: The task_id of this GetOpportunitiesTasksTaskIdOk.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and task_id is None:
            raise ValueError("Invalid value for `task_id`, must not be `None`")  # noqa: E501

        self._task_id = task_id

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
        if issubclass(GetOpportunitiesTasksTaskIdOk, dict):
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
        if not isinstance(other, GetOpportunitiesTasksTaskIdOk):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetOpportunitiesTasksTaskIdOk):
            return True

        return self.to_dict() != other.to_dict()
