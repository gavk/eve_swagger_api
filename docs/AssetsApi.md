# eve_swagger_api.AssetsApi

All URIs are relative to *https://esi.evetech.net/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_characters_character_id_assets**](AssetsApi.md#get_characters_character_id_assets) | **GET** /characters/{character_id}/assets/ | Get character assets
[**get_corporations_corporation_id_assets**](AssetsApi.md#get_corporations_corporation_id_assets) | **GET** /corporations/{corporation_id}/assets/ | Get corporation assets
[**post_characters_character_id_assets_locations**](AssetsApi.md#post_characters_character_id_assets_locations) | **POST** /characters/{character_id}/assets/locations/ | Get character asset locations
[**post_characters_character_id_assets_names**](AssetsApi.md#post_characters_character_id_assets_names) | **POST** /characters/{character_id}/assets/names/ | Get character asset names
[**post_corporations_corporation_id_assets_locations**](AssetsApi.md#post_corporations_corporation_id_assets_locations) | **POST** /corporations/{corporation_id}/assets/locations/ | Get corporation asset locations
[**post_corporations_corporation_id_assets_names**](AssetsApi.md#post_corporations_corporation_id_assets_names) | **POST** /corporations/{corporation_id}/assets/names/ | Get corporation asset names


# **get_characters_character_id_assets**
> list[GetCharactersCharacterIdAssets200Ok] get_characters_character_id_assets(character_id, datasource=datasource, if_none_match=if_none_match, page=page, token=token)

Get character assets

Return a list of the characters assets  --- Alternate route: `/dev/characters/{character_id}/assets/`  Alternate route: `/v5/characters/{character_id}/assets/`  --- This route is cached for up to 3600 seconds

### Example
```python
from __future__ import print_function
import time
import eve_swagger_api
from eve_swagger_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: evesso
configuration = eve_swagger_api.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = eve_swagger_api.AssetsApi(eve_swagger_api.ApiClient(configuration))
character_id = 56 # int | An EVE character ID
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
page = 1 # int | Which page of results to return (optional) (default to 1)
token = 'token_example' # str | Access token to use if unable to set a header (optional)

try:
    # Get character assets
    api_response = api_instance.get_characters_character_id_assets(character_id, datasource=datasource, if_none_match=if_none_match, page=page, token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsApi->get_characters_character_id_assets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| An EVE character ID | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to tranquility]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **page** | **int**| Which page of results to return | [optional] [default to 1]
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

[**list[GetCharactersCharacterIdAssets200Ok]**](GetCharactersCharacterIdAssets200Ok.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_corporations_corporation_id_assets**
> list[GetCorporationsCorporationIdAssets200Ok] get_corporations_corporation_id_assets(corporation_id, datasource=datasource, if_none_match=if_none_match, page=page, token=token)

Get corporation assets

Return a list of the corporation assets  --- Alternate route: `/dev/corporations/{corporation_id}/assets/`  Alternate route: `/v5/corporations/{corporation_id}/assets/`  --- This route is cached for up to 3600 seconds  --- Requires one of the following EVE corporation role(s): Director 

### Example
```python
from __future__ import print_function
import time
import eve_swagger_api
from eve_swagger_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: evesso
configuration = eve_swagger_api.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = eve_swagger_api.AssetsApi(eve_swagger_api.ApiClient(configuration))
corporation_id = 56 # int | An EVE corporation ID
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
page = 1 # int | Which page of results to return (optional) (default to 1)
token = 'token_example' # str | Access token to use if unable to set a header (optional)

try:
    # Get corporation assets
    api_response = api_instance.get_corporations_corporation_id_assets(corporation_id, datasource=datasource, if_none_match=if_none_match, page=page, token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsApi->get_corporations_corporation_id_assets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corporation_id** | **int**| An EVE corporation ID | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to tranquility]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **page** | **int**| Which page of results to return | [optional] [default to 1]
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

[**list[GetCorporationsCorporationIdAssets200Ok]**](GetCorporationsCorporationIdAssets200Ok.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_characters_character_id_assets_locations**
> list[PostCharactersCharacterIdAssetsLocations200Ok] post_characters_character_id_assets_locations(character_id, item_ids, datasource=datasource, token=token)

Get character asset locations

Return locations for a set of item ids, which you can get from character assets endpoint. Coordinates for items in hangars or stations are set to (0,0,0)  --- Alternate route: `/dev/characters/{character_id}/assets/locations/`  Alternate route: `/v2/characters/{character_id}/assets/locations/` 

### Example
```python
from __future__ import print_function
import time
import eve_swagger_api
from eve_swagger_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: evesso
configuration = eve_swagger_api.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = eve_swagger_api.AssetsApi(eve_swagger_api.ApiClient(configuration))
character_id = 56 # int | An EVE character ID
item_ids = [eve_swagger_api.list[int]()] # list[int] | A list of item ids
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
token = 'token_example' # str | Access token to use if unable to set a header (optional)

try:
    # Get character asset locations
    api_response = api_instance.post_characters_character_id_assets_locations(character_id, item_ids, datasource=datasource, token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsApi->post_characters_character_id_assets_locations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| An EVE character ID | 
 **item_ids** | **list[int]**| A list of item ids | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to tranquility]
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

[**list[PostCharactersCharacterIdAssetsLocations200Ok]**](PostCharactersCharacterIdAssetsLocations200Ok.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_characters_character_id_assets_names**
> list[PostCharactersCharacterIdAssetsNames200Ok] post_characters_character_id_assets_names(character_id, item_ids, datasource=datasource, token=token)

Get character asset names

Return names for a set of item ids, which you can get from character assets endpoint. Typically used for items that can customize names, like containers or ships.  --- Alternate route: `/dev/characters/{character_id}/assets/names/`  Alternate route: `/legacy/characters/{character_id}/assets/names/`  Alternate route: `/v1/characters/{character_id}/assets/names/` 

### Example
```python
from __future__ import print_function
import time
import eve_swagger_api
from eve_swagger_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: evesso
configuration = eve_swagger_api.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = eve_swagger_api.AssetsApi(eve_swagger_api.ApiClient(configuration))
character_id = 56 # int | An EVE character ID
item_ids = [eve_swagger_api.list[int]()] # list[int] | A list of item ids
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
token = 'token_example' # str | Access token to use if unable to set a header (optional)

try:
    # Get character asset names
    api_response = api_instance.post_characters_character_id_assets_names(character_id, item_ids, datasource=datasource, token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsApi->post_characters_character_id_assets_names: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| An EVE character ID | 
 **item_ids** | **list[int]**| A list of item ids | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to tranquility]
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

[**list[PostCharactersCharacterIdAssetsNames200Ok]**](PostCharactersCharacterIdAssetsNames200Ok.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_corporations_corporation_id_assets_locations**
> list[PostCorporationsCorporationIdAssetsLocations200Ok] post_corporations_corporation_id_assets_locations(corporation_id, item_ids, datasource=datasource, token=token)

Get corporation asset locations

Return locations for a set of item ids, which you can get from corporation assets endpoint. Coordinates for items in hangars or stations are set to (0,0,0)  --- Alternate route: `/dev/corporations/{corporation_id}/assets/locations/`  Alternate route: `/v2/corporations/{corporation_id}/assets/locations/`   --- Requires one of the following EVE corporation role(s): Director 

### Example
```python
from __future__ import print_function
import time
import eve_swagger_api
from eve_swagger_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: evesso
configuration = eve_swagger_api.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = eve_swagger_api.AssetsApi(eve_swagger_api.ApiClient(configuration))
corporation_id = 56 # int | An EVE corporation ID
item_ids = [eve_swagger_api.list[int]()] # list[int] | A list of item ids
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
token = 'token_example' # str | Access token to use if unable to set a header (optional)

try:
    # Get corporation asset locations
    api_response = api_instance.post_corporations_corporation_id_assets_locations(corporation_id, item_ids, datasource=datasource, token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsApi->post_corporations_corporation_id_assets_locations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corporation_id** | **int**| An EVE corporation ID | 
 **item_ids** | **list[int]**| A list of item ids | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to tranquility]
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

[**list[PostCorporationsCorporationIdAssetsLocations200Ok]**](PostCorporationsCorporationIdAssetsLocations200Ok.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_corporations_corporation_id_assets_names**
> list[PostCorporationsCorporationIdAssetsNames200Ok] post_corporations_corporation_id_assets_names(corporation_id, item_ids, datasource=datasource, token=token)

Get corporation asset names

Return names for a set of item ids, which you can get from corporation assets endpoint. Only valid for items that can customize names, like containers or ships  --- Alternate route: `/dev/corporations/{corporation_id}/assets/names/`  Alternate route: `/legacy/corporations/{corporation_id}/assets/names/`  Alternate route: `/v1/corporations/{corporation_id}/assets/names/`   --- Requires one of the following EVE corporation role(s): Director 

### Example
```python
from __future__ import print_function
import time
import eve_swagger_api
from eve_swagger_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: evesso
configuration = eve_swagger_api.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = eve_swagger_api.AssetsApi(eve_swagger_api.ApiClient(configuration))
corporation_id = 56 # int | An EVE corporation ID
item_ids = [eve_swagger_api.list[int]()] # list[int] | A list of item ids
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
token = 'token_example' # str | Access token to use if unable to set a header (optional)

try:
    # Get corporation asset names
    api_response = api_instance.post_corporations_corporation_id_assets_names(corporation_id, item_ids, datasource=datasource, token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsApi->post_corporations_corporation_id_assets_names: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corporation_id** | **int**| An EVE corporation ID | 
 **item_ids** | **list[int]**| A list of item ids | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to tranquility]
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

[**list[PostCorporationsCorporationIdAssetsNames200Ok]**](PostCorporationsCorporationIdAssetsNames200Ok.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

