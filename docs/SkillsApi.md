# eve_swagger_api.SkillsApi

All URIs are relative to *https://esi.evetech.net/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_characters_character_id_attributes**](SkillsApi.md#get_characters_character_id_attributes) | **GET** /characters/{character_id}/attributes/ | Get character attributes
[**get_characters_character_id_skillqueue**](SkillsApi.md#get_characters_character_id_skillqueue) | **GET** /characters/{character_id}/skillqueue/ | Get character&#39;s skill queue
[**get_characters_character_id_skills**](SkillsApi.md#get_characters_character_id_skills) | **GET** /characters/{character_id}/skills/ | Get character skills


# **get_characters_character_id_attributes**
> GetCharactersCharacterIdAttributesOk get_characters_character_id_attributes(character_id, datasource=datasource, if_none_match=if_none_match, token=token)

Get character attributes

Return attributes of a character  --- Alternate route: `/dev/characters/{character_id}/attributes/`  Alternate route: `/legacy/characters/{character_id}/attributes/`  Alternate route: `/v1/characters/{character_id}/attributes/`  --- This route is cached for up to 120 seconds

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
api_instance = eve_swagger_api.SkillsApi(eve_swagger_api.ApiClient(configuration))
character_id = 56 # int | An EVE character ID
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
token = 'token_example' # str | Access token to use if unable to set a header (optional)

try:
    # Get character attributes
    api_response = api_instance.get_characters_character_id_attributes(character_id, datasource=datasource, if_none_match=if_none_match, token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SkillsApi->get_characters_character_id_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| An EVE character ID | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to tranquility]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

[**GetCharactersCharacterIdAttributesOk**](GetCharactersCharacterIdAttributesOk.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_characters_character_id_skillqueue**
> list[GetCharactersCharacterIdSkillqueue200Ok] get_characters_character_id_skillqueue(character_id, datasource=datasource, if_none_match=if_none_match, token=token)

Get character's skill queue

List the configured skill queue for the given character  --- Alternate route: `/dev/characters/{character_id}/skillqueue/`  Alternate route: `/legacy/characters/{character_id}/skillqueue/`  Alternate route: `/v2/characters/{character_id}/skillqueue/`  --- This route is cached for up to 120 seconds

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
api_instance = eve_swagger_api.SkillsApi(eve_swagger_api.ApiClient(configuration))
character_id = 56 # int | An EVE character ID
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
token = 'token_example' # str | Access token to use if unable to set a header (optional)

try:
    # Get character's skill queue
    api_response = api_instance.get_characters_character_id_skillqueue(character_id, datasource=datasource, if_none_match=if_none_match, token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SkillsApi->get_characters_character_id_skillqueue: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| An EVE character ID | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to tranquility]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

[**list[GetCharactersCharacterIdSkillqueue200Ok]**](GetCharactersCharacterIdSkillqueue200Ok.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_characters_character_id_skills**
> GetCharactersCharacterIdSkillsOk get_characters_character_id_skills(character_id, datasource=datasource, if_none_match=if_none_match, token=token)

Get character skills

List all trained skills for the given character  --- Alternate route: `/dev/characters/{character_id}/skills/`  Alternate route: `/v4/characters/{character_id}/skills/`  --- This route is cached for up to 120 seconds

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
api_instance = eve_swagger_api.SkillsApi(eve_swagger_api.ApiClient(configuration))
character_id = 56 # int | An EVE character ID
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
token = 'token_example' # str | Access token to use if unable to set a header (optional)

try:
    # Get character skills
    api_response = api_instance.get_characters_character_id_skills(character_id, datasource=datasource, if_none_match=if_none_match, token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SkillsApi->get_characters_character_id_skills: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| An EVE character ID | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to tranquility]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

[**GetCharactersCharacterIdSkillsOk**](GetCharactersCharacterIdSkillsOk.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

