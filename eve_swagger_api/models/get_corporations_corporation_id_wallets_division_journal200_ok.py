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


class GetCorporationsCorporationIdWalletsDivisionJournal200Ok(object):
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
        'amount': 'float',
        'balance': 'float',
        'context_id': 'int',
        'context_id_type': 'str',
        '_date': 'datetime',
        'description': 'str',
        'first_party_id': 'int',
        'id': 'int',
        'reason': 'str',
        'ref_type': 'str',
        'second_party_id': 'int',
        'tax': 'float',
        'tax_receiver_id': 'int'
    }

    attribute_map = {
        'amount': 'amount',
        'balance': 'balance',
        'context_id': 'context_id',
        'context_id_type': 'context_id_type',
        '_date': 'date',
        'description': 'description',
        'first_party_id': 'first_party_id',
        'id': 'id',
        'reason': 'reason',
        'ref_type': 'ref_type',
        'second_party_id': 'second_party_id',
        'tax': 'tax',
        'tax_receiver_id': 'tax_receiver_id'
    }

    def __init__(self, amount=None, balance=None, context_id=None, context_id_type=None, _date=None, description=None, first_party_id=None, id=None, reason=None, ref_type=None, second_party_id=None, tax=None, tax_receiver_id=None, _configuration=None):  # noqa: E501
        """GetCorporationsCorporationIdWalletsDivisionJournal200Ok - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._amount = None
        self._balance = None
        self._context_id = None
        self._context_id_type = None
        self.__date = None
        self._description = None
        self._first_party_id = None
        self._id = None
        self._reason = None
        self._ref_type = None
        self._second_party_id = None
        self._tax = None
        self._tax_receiver_id = None
        self.discriminator = None

        if amount is not None:
            self.amount = amount
        if balance is not None:
            self.balance = balance
        if context_id is not None:
            self.context_id = context_id
        if context_id_type is not None:
            self.context_id_type = context_id_type
        self._date = _date
        self.description = description
        if first_party_id is not None:
            self.first_party_id = first_party_id
        self.id = id
        if reason is not None:
            self.reason = reason
        self.ref_type = ref_type
        if second_party_id is not None:
            self.second_party_id = second_party_id
        if tax is not None:
            self.tax = tax
        if tax_receiver_id is not None:
            self.tax_receiver_id = tax_receiver_id

    @property
    def amount(self):
        """Gets the amount of this GetCorporationsCorporationIdWalletsDivisionJournal200Ok.  # noqa: E501

        The amount of ISK given or taken from the wallet as a result of the given transaction. Positive when ISK is deposited into the wallet and negative when ISK is withdrawn  # noqa: E501

        :return: The amount of this GetCorporationsCorporationIdWalletsDivisionJournal200Ok.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this GetCorporationsCorporationIdWalletsDivisionJournal200Ok.

        The amount of ISK given or taken from the wallet as a result of the given transaction. Positive when ISK is deposited into the wallet and negative when ISK is withdrawn  # noqa: E501

        :param amount: The amount of this GetCorporationsCorporationIdWalletsDivisionJournal200Ok.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def balance(self):
        """Gets the balance of this GetCorporationsCorporationIdWalletsDivisionJournal200Ok.  # noqa: E501

        Wallet balance after transaction occurred  # noqa: E501

        :return: The balance of this GetCorporationsCorporationIdWalletsDivisionJournal200Ok.  # noqa: E501
        :rtype: float
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this GetCorporationsCorporationIdWalletsDivisionJournal200Ok.

        Wallet balance after transaction occurred  # noqa: E501

        :param balance: The balance of this GetCorporationsCorporationIdWalletsDivisionJournal200Ok.  # noqa: E501
        :type: float
        """

        self._balance = balance

    @property
    def context_id(self):
        """Gets the context_id of this GetCorporationsCorporationIdWalletsDivisionJournal200Ok.  # noqa: E501

        An ID that gives extra context to the particular transaction. Because of legacy reasons the context is completely different per ref_type and means different things. It is also possible to not have a context_id  # noqa: E501

        :return: The context_id of this GetCorporationsCorporationIdWalletsDivisionJournal200Ok.  # noqa: E501
        :rtype: int
        """
        return self._context_id

    @context_id.setter
    def context_id(self, context_id):
        """Sets the context_id of this GetCorporationsCorporationIdWalletsDivisionJournal200Ok.

        An ID that gives extra context to the particular transaction. Because of legacy reasons the context is completely different per ref_type and means different things. It is also possible to not have a context_id  # noqa: E501

        :param context_id: The context_id of this GetCorporationsCorporationIdWalletsDivisionJournal200Ok.  # noqa: E501
        :type: int
        """

        self._context_id = context_id

    @property
    def context_id_type(self):
        """Gets the context_id_type of this GetCorporationsCorporationIdWalletsDivisionJournal200Ok.  # noqa: E501

        The type of the given context_id if present  # noqa: E501

        :return: The context_id_type of this GetCorporationsCorporationIdWalletsDivisionJournal200Ok.  # noqa: E501
        :rtype: str
        """
        return self._context_id_type

    @context_id_type.setter
    def context_id_type(self, context_id_type):
        """Sets the context_id_type of this GetCorporationsCorporationIdWalletsDivisionJournal200Ok.

        The type of the given context_id if present  # noqa: E501

        :param context_id_type: The context_id_type of this GetCorporationsCorporationIdWalletsDivisionJournal200Ok.  # noqa: E501
        :type: str
        """
        allowed_values = ["structure_id", "station_id", "market_transaction_id", "character_id", "corporation_id", "alliance_id", "eve_system", "industry_job_id", "contract_id", "planet_id", "system_id", "type_id"]  # noqa: E501
        if (self._configuration.client_side_validation and
                context_id_type not in allowed_values):
            raise ValueError(
                "Invalid value for `context_id_type` ({0}), must be one of {1}"  # noqa: E501
                .format(context_id_type, allowed_values)
            )

        self._context_id_type = context_id_type

    @property
    def _date(self):
        """Gets the _date of this GetCorporationsCorporationIdWalletsDivisionJournal200Ok.  # noqa: E501

        Date and time of transaction  # noqa: E501

        :return: The _date of this GetCorporationsCorporationIdWalletsDivisionJournal200Ok.  # noqa: E501
        :rtype: datetime
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this GetCorporationsCorporationIdWalletsDivisionJournal200Ok.

        Date and time of transaction  # noqa: E501

        :param _date: The _date of this GetCorporationsCorporationIdWalletsDivisionJournal200Ok.  # noqa: E501
        :type: datetime
        """
        if self._configuration.client_side_validation and _date is None:
            raise ValueError("Invalid value for `_date`, must not be `None`")  # noqa: E501

        self.__date = _date

    @property
    def description(self):
        """Gets the description of this GetCorporationsCorporationIdWalletsDivisionJournal200Ok.  # noqa: E501

        The reason for the transaction, mirrors what is seen in the client  # noqa: E501

        :return: The description of this GetCorporationsCorporationIdWalletsDivisionJournal200Ok.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this GetCorporationsCorporationIdWalletsDivisionJournal200Ok.

        The reason for the transaction, mirrors what is seen in the client  # noqa: E501

        :param description: The description of this GetCorporationsCorporationIdWalletsDivisionJournal200Ok.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def first_party_id(self):
        """Gets the first_party_id of this GetCorporationsCorporationIdWalletsDivisionJournal200Ok.  # noqa: E501

        The id of the first party involved in the transaction. This attribute has no consistency and is different or non existant for particular ref_types. The description attribute will help make sense of what this attribute means. For more info about the given ID it can be dropped into the /universe/names/ ESI route to determine its type and name  # noqa: E501

        :return: The first_party_id of this GetCorporationsCorporationIdWalletsDivisionJournal200Ok.  # noqa: E501
        :rtype: int
        """
        return self._first_party_id

    @first_party_id.setter
    def first_party_id(self, first_party_id):
        """Sets the first_party_id of this GetCorporationsCorporationIdWalletsDivisionJournal200Ok.

        The id of the first party involved in the transaction. This attribute has no consistency and is different or non existant for particular ref_types. The description attribute will help make sense of what this attribute means. For more info about the given ID it can be dropped into the /universe/names/ ESI route to determine its type and name  # noqa: E501

        :param first_party_id: The first_party_id of this GetCorporationsCorporationIdWalletsDivisionJournal200Ok.  # noqa: E501
        :type: int
        """

        self._first_party_id = first_party_id

    @property
    def id(self):
        """Gets the id of this GetCorporationsCorporationIdWalletsDivisionJournal200Ok.  # noqa: E501

        Unique journal reference ID  # noqa: E501

        :return: The id of this GetCorporationsCorporationIdWalletsDivisionJournal200Ok.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetCorporationsCorporationIdWalletsDivisionJournal200Ok.

        Unique journal reference ID  # noqa: E501

        :param id: The id of this GetCorporationsCorporationIdWalletsDivisionJournal200Ok.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def reason(self):
        """Gets the reason of this GetCorporationsCorporationIdWalletsDivisionJournal200Ok.  # noqa: E501

        The user stated reason for the transaction. Only applies to some ref_types  # noqa: E501

        :return: The reason of this GetCorporationsCorporationIdWalletsDivisionJournal200Ok.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this GetCorporationsCorporationIdWalletsDivisionJournal200Ok.

        The user stated reason for the transaction. Only applies to some ref_types  # noqa: E501

        :param reason: The reason of this GetCorporationsCorporationIdWalletsDivisionJournal200Ok.  # noqa: E501
        :type: str
        """

        self._reason = reason

    @property
    def ref_type(self):
        """Gets the ref_type of this GetCorporationsCorporationIdWalletsDivisionJournal200Ok.  # noqa: E501

        \"The transaction type for the given. transaction. Different transaction types will populate different attributes. Note: If you have an existing XML API application that is using ref_types, you will need to know which string ESI ref_type maps to which integer. You can look at the following file to see string->int mappings: https://github.com/ccpgames/eve-glue/blob/master/eve_glue/wallet_journal_ref.py\"  # noqa: E501

        :return: The ref_type of this GetCorporationsCorporationIdWalletsDivisionJournal200Ok.  # noqa: E501
        :rtype: str
        """
        return self._ref_type

    @ref_type.setter
    def ref_type(self, ref_type):
        """Sets the ref_type of this GetCorporationsCorporationIdWalletsDivisionJournal200Ok.

        \"The transaction type for the given. transaction. Different transaction types will populate different attributes. Note: If you have an existing XML API application that is using ref_types, you will need to know which string ESI ref_type maps to which integer. You can look at the following file to see string->int mappings: https://github.com/ccpgames/eve-glue/blob/master/eve_glue/wallet_journal_ref.py\"  # noqa: E501

        :param ref_type: The ref_type of this GetCorporationsCorporationIdWalletsDivisionJournal200Ok.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and ref_type is None:
            raise ValueError("Invalid value for `ref_type`, must not be `None`")  # noqa: E501
        allowed_values = ["acceleration_gate_fee", "advertisement_listing_fee", "agent_donation", "agent_location_services", "agent_miscellaneous", "agent_mission_collateral_paid", "agent_mission_collateral_refunded", "agent_mission_reward", "agent_mission_reward_corporation_tax", "agent_mission_time_bonus_reward", "agent_mission_time_bonus_reward_corporation_tax", "agent_security_services", "agent_services_rendered", "agents_preward", "alliance_maintainance_fee", "alliance_registration_fee", "asset_safety_recovery_tax", "bounty", "bounty_prize", "bounty_prize_corporation_tax", "bounty_prizes", "bounty_reimbursement", "bounty_surcharge", "brokers_fee", "clone_activation", "clone_transfer", "contraband_fine", "contract_auction_bid", "contract_auction_bid_corp", "contract_auction_bid_refund", "contract_auction_sold", "contract_brokers_fee", "contract_brokers_fee_corp", "contract_collateral", "contract_collateral_deposited_corp", "contract_collateral_payout", "contract_collateral_refund", "contract_deposit", "contract_deposit_corp", "contract_deposit_refund", "contract_deposit_sales_tax", "contract_price", "contract_price_payment_corp", "contract_reversal", "contract_reward", "contract_reward_deposited", "contract_reward_deposited_corp", "contract_reward_refund", "contract_sales_tax", "copying", "corporate_reward_payout", "corporate_reward_tax", "corporation_account_withdrawal", "corporation_bulk_payment", "corporation_dividend_payment", "corporation_liquidation", "corporation_logo_change_cost", "corporation_payment", "corporation_registration_fee", "courier_mission_escrow", "cspa", "cspaofflinerefund", "daily_challenge_reward", "datacore_fee", "dna_modification_fee", "docking_fee", "duel_wager_escrow", "duel_wager_payment", "duel_wager_refund", "ess_escrow_transfer", "external_trade_delivery", "external_trade_freeze", "external_trade_thaw", "factory_slot_rental_fee", "flux_payout", "flux_tax", "flux_ticket_repayment", "flux_ticket_sale", "gm_cash_transfer", "industry_job_tax", "infrastructure_hub_maintenance", "inheritance", "insurance", "item_trader_payment", "jump_clone_activation_fee", "jump_clone_installation_fee", "kill_right_fee", "lp_store", "manufacturing", "market_escrow", "market_fine_paid", "market_provider_tax", "market_transaction", "medal_creation", "medal_issued", "milestone_reward_payment", "mission_completion", "mission_cost", "mission_expiration", "mission_reward", "office_rental_fee", "operation_bonus", "opportunity_reward", "planetary_construction", "planetary_export_tax", "planetary_import_tax", "player_donation", "player_trading", "project_discovery_reward", "project_discovery_tax", "reaction", "redeemed_isk_token", "release_of_impounded_property", "repair_bill", "reprocessing_tax", "researching_material_productivity", "researching_technology", "researching_time_productivity", "resource_wars_reward", "reverse_engineering", "season_challenge_reward", "security_processing_fee", "shares", "skill_purchase", "sovereignity_bill", "store_purchase", "store_purchase_refund", "structure_gate_jump", "transaction_tax", "upkeep_adjustment_fee", "war_ally_contract", "war_fee", "war_fee_surrender"]  # noqa: E501
        if (self._configuration.client_side_validation and
                ref_type not in allowed_values):
            raise ValueError(
                "Invalid value for `ref_type` ({0}), must be one of {1}"  # noqa: E501
                .format(ref_type, allowed_values)
            )

        self._ref_type = ref_type

    @property
    def second_party_id(self):
        """Gets the second_party_id of this GetCorporationsCorporationIdWalletsDivisionJournal200Ok.  # noqa: E501

        The id of the second party involved in the transaction. This attribute has no consistency and is different or non existant for particular ref_types. The description attribute will help make sense of what this attribute means. For more info about the given ID it can be dropped into the /universe/names/ ESI route to determine its type and name  # noqa: E501

        :return: The second_party_id of this GetCorporationsCorporationIdWalletsDivisionJournal200Ok.  # noqa: E501
        :rtype: int
        """
        return self._second_party_id

    @second_party_id.setter
    def second_party_id(self, second_party_id):
        """Sets the second_party_id of this GetCorporationsCorporationIdWalletsDivisionJournal200Ok.

        The id of the second party involved in the transaction. This attribute has no consistency and is different or non existant for particular ref_types. The description attribute will help make sense of what this attribute means. For more info about the given ID it can be dropped into the /universe/names/ ESI route to determine its type and name  # noqa: E501

        :param second_party_id: The second_party_id of this GetCorporationsCorporationIdWalletsDivisionJournal200Ok.  # noqa: E501
        :type: int
        """

        self._second_party_id = second_party_id

    @property
    def tax(self):
        """Gets the tax of this GetCorporationsCorporationIdWalletsDivisionJournal200Ok.  # noqa: E501

        Tax amount received. Only applies to tax related transactions  # noqa: E501

        :return: The tax of this GetCorporationsCorporationIdWalletsDivisionJournal200Ok.  # noqa: E501
        :rtype: float
        """
        return self._tax

    @tax.setter
    def tax(self, tax):
        """Sets the tax of this GetCorporationsCorporationIdWalletsDivisionJournal200Ok.

        Tax amount received. Only applies to tax related transactions  # noqa: E501

        :param tax: The tax of this GetCorporationsCorporationIdWalletsDivisionJournal200Ok.  # noqa: E501
        :type: float
        """

        self._tax = tax

    @property
    def tax_receiver_id(self):
        """Gets the tax_receiver_id of this GetCorporationsCorporationIdWalletsDivisionJournal200Ok.  # noqa: E501

        The corporation ID receiving any tax paid. Only applies to tax related transactions  # noqa: E501

        :return: The tax_receiver_id of this GetCorporationsCorporationIdWalletsDivisionJournal200Ok.  # noqa: E501
        :rtype: int
        """
        return self._tax_receiver_id

    @tax_receiver_id.setter
    def tax_receiver_id(self, tax_receiver_id):
        """Sets the tax_receiver_id of this GetCorporationsCorporationIdWalletsDivisionJournal200Ok.

        The corporation ID receiving any tax paid. Only applies to tax related transactions  # noqa: E501

        :param tax_receiver_id: The tax_receiver_id of this GetCorporationsCorporationIdWalletsDivisionJournal200Ok.  # noqa: E501
        :type: int
        """

        self._tax_receiver_id = tax_receiver_id

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
        if issubclass(GetCorporationsCorporationIdWalletsDivisionJournal200Ok, dict):
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
        if not isinstance(other, GetCorporationsCorporationIdWalletsDivisionJournal200Ok):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetCorporationsCorporationIdWalletsDivisionJournal200Ok):
            return True

        return self.to_dict() != other.to_dict()
