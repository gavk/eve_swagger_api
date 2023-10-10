# coding: utf-8

"""
    EVE Swagger Interface

    An OpenAPI for EVE Online  # noqa: E501

    OpenAPI spec version: 1.19
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from eve_swagger_api.api_client import ApiClient


class PlanetaryInteractionApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_characters_character_id_planets(self, character_id, **kwargs):  # noqa: E501
        """Get colonies  # noqa: E501

        Returns a list of all planetary colonies owned by a character.  --- Alternate route: `/dev/characters/{character_id}/planets/`  Alternate route: `/legacy/characters/{character_id}/planets/`  Alternate route: `/v1/characters/{character_id}/planets/`  --- This route is cached for up to 600 seconds  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_characters_character_id_planets(character_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int character_id: An EVE character ID (required)
        :param str datasource: The server name you would like data from
        :param str if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
        :param str token: Access token to use if unable to set a header
        :return: list[GetCharactersCharacterIdPlanets200Ok]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_characters_character_id_planets_with_http_info(character_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_characters_character_id_planets_with_http_info(character_id, **kwargs)  # noqa: E501
            return data

    def get_characters_character_id_planets_with_http_info(self, character_id, **kwargs):  # noqa: E501
        """Get colonies  # noqa: E501

        Returns a list of all planetary colonies owned by a character.  --- Alternate route: `/dev/characters/{character_id}/planets/`  Alternate route: `/legacy/characters/{character_id}/planets/`  Alternate route: `/v1/characters/{character_id}/planets/`  --- This route is cached for up to 600 seconds  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_characters_character_id_planets_with_http_info(character_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int character_id: An EVE character ID (required)
        :param str datasource: The server name you would like data from
        :param str if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
        :param str token: Access token to use if unable to set a header
        :return: list[GetCharactersCharacterIdPlanets200Ok]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['character_id', 'datasource', 'if_none_match', 'token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_characters_character_id_planets" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'character_id' is set
        if self.api_client.client_side_validation and ('character_id' not in params or
                                                       params['character_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `character_id` when calling `get_characters_character_id_planets`")  # noqa: E501

        if self.api_client.client_side_validation and ('character_id' in params and params['character_id'] < 1):  # noqa: E501
            raise ValueError("Invalid value for parameter `character_id` when calling `get_characters_character_id_planets`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'character_id' in params:
            path_params['character_id'] = params['character_id']  # noqa: E501

        query_params = []
        if 'datasource' in params:
            query_params.append(('datasource', params['datasource']))  # noqa: E501
        if 'token' in params:
            query_params.append(('token', params['token']))  # noqa: E501

        header_params = {}
        if 'if_none_match' in params:
            header_params['If-None-Match'] = params['if_none_match']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['evesso']  # noqa: E501

        return self.api_client.call_api(
            '/characters/{character_id}/planets/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GetCharactersCharacterIdPlanets200Ok]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_characters_character_id_planets_planet_id(self, character_id, planet_id, **kwargs):  # noqa: E501
        """Get colony layout  # noqa: E501

        Returns full details on the layout of a single planetary colony, including links, pins and routes. Note: Planetary information is only recalculated when the colony is viewed through the client. Information will not update until this criteria is met.  --- Alternate route: `/dev/characters/{character_id}/planets/{planet_id}/`  Alternate route: `/v3/characters/{character_id}/planets/{planet_id}/`   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_characters_character_id_planets_planet_id(character_id, planet_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int character_id: An EVE character ID (required)
        :param int planet_id: Planet id of the target planet (required)
        :param str datasource: The server name you would like data from
        :param str token: Access token to use if unable to set a header
        :return: GetCharactersCharacterIdPlanetsPlanetIdOk
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_characters_character_id_planets_planet_id_with_http_info(character_id, planet_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_characters_character_id_planets_planet_id_with_http_info(character_id, planet_id, **kwargs)  # noqa: E501
            return data

    def get_characters_character_id_planets_planet_id_with_http_info(self, character_id, planet_id, **kwargs):  # noqa: E501
        """Get colony layout  # noqa: E501

        Returns full details on the layout of a single planetary colony, including links, pins and routes. Note: Planetary information is only recalculated when the colony is viewed through the client. Information will not update until this criteria is met.  --- Alternate route: `/dev/characters/{character_id}/planets/{planet_id}/`  Alternate route: `/v3/characters/{character_id}/planets/{planet_id}/`   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_characters_character_id_planets_planet_id_with_http_info(character_id, planet_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int character_id: An EVE character ID (required)
        :param int planet_id: Planet id of the target planet (required)
        :param str datasource: The server name you would like data from
        :param str token: Access token to use if unable to set a header
        :return: GetCharactersCharacterIdPlanetsPlanetIdOk
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['character_id', 'planet_id', 'datasource', 'token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_characters_character_id_planets_planet_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'character_id' is set
        if self.api_client.client_side_validation and ('character_id' not in params or
                                                       params['character_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `character_id` when calling `get_characters_character_id_planets_planet_id`")  # noqa: E501
        # verify the required parameter 'planet_id' is set
        if self.api_client.client_side_validation and ('planet_id' not in params or
                                                       params['planet_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `planet_id` when calling `get_characters_character_id_planets_planet_id`")  # noqa: E501

        if self.api_client.client_side_validation and ('character_id' in params and params['character_id'] < 1):  # noqa: E501
            raise ValueError("Invalid value for parameter `character_id` when calling `get_characters_character_id_planets_planet_id`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'character_id' in params:
            path_params['character_id'] = params['character_id']  # noqa: E501
        if 'planet_id' in params:
            path_params['planet_id'] = params['planet_id']  # noqa: E501

        query_params = []
        if 'datasource' in params:
            query_params.append(('datasource', params['datasource']))  # noqa: E501
        if 'token' in params:
            query_params.append(('token', params['token']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['evesso']  # noqa: E501

        return self.api_client.call_api(
            '/characters/{character_id}/planets/{planet_id}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetCharactersCharacterIdPlanetsPlanetIdOk',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_corporations_corporation_id_customs_offices(self, corporation_id, **kwargs):  # noqa: E501
        """List corporation customs offices  # noqa: E501

        List customs offices owned by a corporation  --- Alternate route: `/dev/corporations/{corporation_id}/customs_offices/`  Alternate route: `/legacy/corporations/{corporation_id}/customs_offices/`  Alternate route: `/v1/corporations/{corporation_id}/customs_offices/`  --- This route is cached for up to 3600 seconds  --- Requires one of the following EVE corporation role(s): Director   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_corporations_corporation_id_customs_offices(corporation_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int corporation_id: An EVE corporation ID (required)
        :param str datasource: The server name you would like data from
        :param str if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
        :param int page: Which page of results to return
        :param str token: Access token to use if unable to set a header
        :return: list[GetCorporationsCorporationIdCustomsOffices200Ok]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_corporations_corporation_id_customs_offices_with_http_info(corporation_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_corporations_corporation_id_customs_offices_with_http_info(corporation_id, **kwargs)  # noqa: E501
            return data

    def get_corporations_corporation_id_customs_offices_with_http_info(self, corporation_id, **kwargs):  # noqa: E501
        """List corporation customs offices  # noqa: E501

        List customs offices owned by a corporation  --- Alternate route: `/dev/corporations/{corporation_id}/customs_offices/`  Alternate route: `/legacy/corporations/{corporation_id}/customs_offices/`  Alternate route: `/v1/corporations/{corporation_id}/customs_offices/`  --- This route is cached for up to 3600 seconds  --- Requires one of the following EVE corporation role(s): Director   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_corporations_corporation_id_customs_offices_with_http_info(corporation_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int corporation_id: An EVE corporation ID (required)
        :param str datasource: The server name you would like data from
        :param str if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
        :param int page: Which page of results to return
        :param str token: Access token to use if unable to set a header
        :return: list[GetCorporationsCorporationIdCustomsOffices200Ok]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['corporation_id', 'datasource', 'if_none_match', 'page', 'token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_corporations_corporation_id_customs_offices" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'corporation_id' is set
        if self.api_client.client_side_validation and ('corporation_id' not in params or
                                                       params['corporation_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `corporation_id` when calling `get_corporations_corporation_id_customs_offices`")  # noqa: E501

        if self.api_client.client_side_validation and ('corporation_id' in params and params['corporation_id'] < 1):  # noqa: E501
            raise ValueError("Invalid value for parameter `corporation_id` when calling `get_corporations_corporation_id_customs_offices`, must be a value greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and ('page' in params and params['page'] < 1):  # noqa: E501
            raise ValueError("Invalid value for parameter `page` when calling `get_corporations_corporation_id_customs_offices`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'corporation_id' in params:
            path_params['corporation_id'] = params['corporation_id']  # noqa: E501

        query_params = []
        if 'datasource' in params:
            query_params.append(('datasource', params['datasource']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'token' in params:
            query_params.append(('token', params['token']))  # noqa: E501

        header_params = {}
        if 'if_none_match' in params:
            header_params['If-None-Match'] = params['if_none_match']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['evesso']  # noqa: E501

        return self.api_client.call_api(
            '/corporations/{corporation_id}/customs_offices/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GetCorporationsCorporationIdCustomsOffices200Ok]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_universe_schematics_schematic_id(self, schematic_id, **kwargs):  # noqa: E501
        """Get schematic information  # noqa: E501

        Get information on a planetary factory schematic  --- Alternate route: `/dev/universe/schematics/{schematic_id}/`  Alternate route: `/legacy/universe/schematics/{schematic_id}/`  Alternate route: `/v1/universe/schematics/{schematic_id}/`  --- This route is cached for up to 3600 seconds  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_universe_schematics_schematic_id(schematic_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int schematic_id: A PI schematic ID (required)
        :param str datasource: The server name you would like data from
        :param str if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
        :return: GetUniverseSchematicsSchematicIdOk
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_universe_schematics_schematic_id_with_http_info(schematic_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_universe_schematics_schematic_id_with_http_info(schematic_id, **kwargs)  # noqa: E501
            return data

    def get_universe_schematics_schematic_id_with_http_info(self, schematic_id, **kwargs):  # noqa: E501
        """Get schematic information  # noqa: E501

        Get information on a planetary factory schematic  --- Alternate route: `/dev/universe/schematics/{schematic_id}/`  Alternate route: `/legacy/universe/schematics/{schematic_id}/`  Alternate route: `/v1/universe/schematics/{schematic_id}/`  --- This route is cached for up to 3600 seconds  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_universe_schematics_schematic_id_with_http_info(schematic_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int schematic_id: A PI schematic ID (required)
        :param str datasource: The server name you would like data from
        :param str if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
        :return: GetUniverseSchematicsSchematicIdOk
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['schematic_id', 'datasource', 'if_none_match']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_universe_schematics_schematic_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'schematic_id' is set
        if self.api_client.client_side_validation and ('schematic_id' not in params or
                                                       params['schematic_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `schematic_id` when calling `get_universe_schematics_schematic_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'schematic_id' in params:
            path_params['schematic_id'] = params['schematic_id']  # noqa: E501

        query_params = []
        if 'datasource' in params:
            query_params.append(('datasource', params['datasource']))  # noqa: E501

        header_params = {}
        if 'if_none_match' in params:
            header_params['If-None-Match'] = params['if_none_match']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/universe/schematics/{schematic_id}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetUniverseSchematicsSchematicIdOk',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
