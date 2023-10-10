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


class PostUiOpenwindowNewmailNewMail(object):
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
        'body': 'str',
        'recipients': 'list[int]',
        'subject': 'str',
        'to_corp_or_alliance_id': 'int',
        'to_mailing_list_id': 'int'
    }

    attribute_map = {
        'body': 'body',
        'recipients': 'recipients',
        'subject': 'subject',
        'to_corp_or_alliance_id': 'to_corp_or_alliance_id',
        'to_mailing_list_id': 'to_mailing_list_id'
    }

    def __init__(self, body=None, recipients=None, subject=None, to_corp_or_alliance_id=None, to_mailing_list_id=None, _configuration=None):  # noqa: E501
        """PostUiOpenwindowNewmailNewMail - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._body = None
        self._recipients = None
        self._subject = None
        self._to_corp_or_alliance_id = None
        self._to_mailing_list_id = None
        self.discriminator = None

        self.body = body
        self.recipients = recipients
        self.subject = subject
        if to_corp_or_alliance_id is not None:
            self.to_corp_or_alliance_id = to_corp_or_alliance_id
        if to_mailing_list_id is not None:
            self.to_mailing_list_id = to_mailing_list_id

    @property
    def body(self):
        """Gets the body of this PostUiOpenwindowNewmailNewMail.  # noqa: E501

        body string  # noqa: E501

        :return: The body of this PostUiOpenwindowNewmailNewMail.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this PostUiOpenwindowNewmailNewMail.

        body string  # noqa: E501

        :param body: The body of this PostUiOpenwindowNewmailNewMail.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and body is None:
            raise ValueError("Invalid value for `body`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                body is not None and len(body) > 10000):
            raise ValueError("Invalid value for `body`, length must be less than or equal to `10000`")  # noqa: E501

        self._body = body

    @property
    def recipients(self):
        """Gets the recipients of this PostUiOpenwindowNewmailNewMail.  # noqa: E501

        recipients array  # noqa: E501

        :return: The recipients of this PostUiOpenwindowNewmailNewMail.  # noqa: E501
        :rtype: list[int]
        """
        return self._recipients

    @recipients.setter
    def recipients(self, recipients):
        """Sets the recipients of this PostUiOpenwindowNewmailNewMail.

        recipients array  # noqa: E501

        :param recipients: The recipients of this PostUiOpenwindowNewmailNewMail.  # noqa: E501
        :type: list[int]
        """
        if self._configuration.client_side_validation and recipients is None:
            raise ValueError("Invalid value for `recipients`, must not be `None`")  # noqa: E501

        self._recipients = recipients

    @property
    def subject(self):
        """Gets the subject of this PostUiOpenwindowNewmailNewMail.  # noqa: E501

        subject string  # noqa: E501

        :return: The subject of this PostUiOpenwindowNewmailNewMail.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this PostUiOpenwindowNewmailNewMail.

        subject string  # noqa: E501

        :param subject: The subject of this PostUiOpenwindowNewmailNewMail.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and subject is None:
            raise ValueError("Invalid value for `subject`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                subject is not None and len(subject) > 1000):
            raise ValueError("Invalid value for `subject`, length must be less than or equal to `1000`")  # noqa: E501

        self._subject = subject

    @property
    def to_corp_or_alliance_id(self):
        """Gets the to_corp_or_alliance_id of this PostUiOpenwindowNewmailNewMail.  # noqa: E501

        to_corp_or_alliance_id integer  # noqa: E501

        :return: The to_corp_or_alliance_id of this PostUiOpenwindowNewmailNewMail.  # noqa: E501
        :rtype: int
        """
        return self._to_corp_or_alliance_id

    @to_corp_or_alliance_id.setter
    def to_corp_or_alliance_id(self, to_corp_or_alliance_id):
        """Sets the to_corp_or_alliance_id of this PostUiOpenwindowNewmailNewMail.

        to_corp_or_alliance_id integer  # noqa: E501

        :param to_corp_or_alliance_id: The to_corp_or_alliance_id of this PostUiOpenwindowNewmailNewMail.  # noqa: E501
        :type: int
        """

        self._to_corp_or_alliance_id = to_corp_or_alliance_id

    @property
    def to_mailing_list_id(self):
        """Gets the to_mailing_list_id of this PostUiOpenwindowNewmailNewMail.  # noqa: E501

        Corporations, alliances and mailing lists are all types of mailing groups. You may only send to one mailing group, at a time, so you may fill out either this field or the to_corp_or_alliance_ids field  # noqa: E501

        :return: The to_mailing_list_id of this PostUiOpenwindowNewmailNewMail.  # noqa: E501
        :rtype: int
        """
        return self._to_mailing_list_id

    @to_mailing_list_id.setter
    def to_mailing_list_id(self, to_mailing_list_id):
        """Sets the to_mailing_list_id of this PostUiOpenwindowNewmailNewMail.

        Corporations, alliances and mailing lists are all types of mailing groups. You may only send to one mailing group, at a time, so you may fill out either this field or the to_corp_or_alliance_ids field  # noqa: E501

        :param to_mailing_list_id: The to_mailing_list_id of this PostUiOpenwindowNewmailNewMail.  # noqa: E501
        :type: int
        """

        self._to_mailing_list_id = to_mailing_list_id

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
        if issubclass(PostUiOpenwindowNewmailNewMail, dict):
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
        if not isinstance(other, PostUiOpenwindowNewmailNewMail):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PostUiOpenwindowNewmailNewMail):
            return True

        return self.to_dict() != other.to_dict()
