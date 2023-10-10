# eve_swagger_api.FittingsApi

All URIs are relative to *https://esi.evetech.net/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_characters_character_id_fittings_fitting_id**](FittingsApi.md#delete_characters_character_id_fittings_fitting_id) | **DELETE** /characters/{character_id}/fittings/{fitting_id}/ | Delete fitting
[**get_characters_character_id_fittings**](FittingsApi.md#get_characters_character_id_fittings) | **GET** /characters/{character_id}/fittings/ | Get fittings
[**post_characters_character_id_fittings**](FittingsApi.md#post_characters_character_id_fittings) | **POST** /characters/{character_id}/fittings/ | Create fitting


# **delete_characters_character_id_fittings_fitting_id**
> delete_characters_character_id_fittings_fitting_id(character_id, fitting_id, datasource=datasource, token=token)

Delete fitting

Delete a fitting from a character  --- Alternate route: `/dev/characters/{character_id}/fittings/{fitting_id}/`  Alternate route: `/legacy/characters/{character_id}/fittings/{fitting_id}/`  Alternate route: `/v1/characters/{character_id}/fittings/{fitting_id}/` 

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
api_instance = eve_swagger_api.FittingsApi(eve_swagger_api.ApiClient(configuration))
character_id = 56 # int | An EVE character ID
fitting_id = 56 # int | ID for a fitting of this character
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
token = 'token_example' # str | Access token to use if unable to set a header (optional)

try:
    # Delete fitting
    api_instance.delete_characters_character_id_fittings_fitting_id(character_id, fitting_id, datasource=datasource, token=token)
except ApiException as e:
    print("Exception when calling FittingsApi->delete_characters_character_id_fittings_fitting_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| An EVE character ID | 
 **fitting_id** | **int**| ID for a fitting of this character | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to tranquility]
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

void (empty response body)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_characters_character_id_fittings**
> list[GetCharactersCharacterIdFittings200Ok] get_characters_character_id_fittings(character_id, datasource=datasource, if_none_match=if_none_match, token=token)

Get fittings

Return fittings of a character  --- Alternate route: `/dev/characters/{character_id}/fittings/`  Alternate route: `/v2/characters/{character_id}/fittings/`  --- This route is cached for up to 300 seconds

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
api_instance = eve_swagger_api.FittingsApi(eve_swagger_api.ApiClient(configuration))
character_id = 56 # int | An EVE character ID
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
token = 'token_example' # str | Access token to use if unable to set a header (optional)

try:
    # Get fittings
    api_response = api_instance.get_characters_character_id_fittings(character_id, datasource=datasource, if_none_match=if_none_match, token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FittingsApi->get_characters_character_id_fittings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| An EVE character ID | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to tranquility]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

[**list[GetCharactersCharacterIdFittings200Ok]**](GetCharactersCharacterIdFittings200Ok.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_characters_character_id_fittings**
> PostCharactersCharacterIdFittingsCreated post_characters_character_id_fittings(character_id, fitting, datasource=datasource, token=token)

Create fitting

Save a new fitting for a character  --- Alternate route: `/dev/characters/{character_id}/fittings/`  Alternate route: `/v2/characters/{character_id}/fittings/` 

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
api_instance = eve_swagger_api.FittingsApi(eve_swagger_api.ApiClient(configuration))
character_id = 56 # int | An EVE character ID
fitting = eve_swagger_api.PostCharactersCharacterIdFittingsFitting() # PostCharactersCharacterIdFittingsFitting | Details about the new fitting
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
token = 'token_example' # str | Access token to use if unable to set a header (optional)

try:
    # Create fitting
    api_response = api_instance.post_characters_character_id_fittings(character_id, fitting, datasource=datasource, token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FittingsApi->post_characters_character_id_fittings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| An EVE character ID | 
 **fitting** | [**PostCharactersCharacterIdFittingsFitting**](PostCharactersCharacterIdFittingsFitting.md)| Details about the new fitting | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to tranquility]
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

[**PostCharactersCharacterIdFittingsCreated**](PostCharactersCharacterIdFittingsCreated.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

