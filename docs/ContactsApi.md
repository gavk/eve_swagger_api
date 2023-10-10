# eve_swagger_api.ContactsApi

All URIs are relative to *https://esi.evetech.net/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_characters_character_id_contacts**](ContactsApi.md#delete_characters_character_id_contacts) | **DELETE** /characters/{character_id}/contacts/ | Delete contacts
[**get_alliances_alliance_id_contacts**](ContactsApi.md#get_alliances_alliance_id_contacts) | **GET** /alliances/{alliance_id}/contacts/ | Get alliance contacts
[**get_alliances_alliance_id_contacts_labels**](ContactsApi.md#get_alliances_alliance_id_contacts_labels) | **GET** /alliances/{alliance_id}/contacts/labels/ | Get alliance contact labels
[**get_characters_character_id_contacts**](ContactsApi.md#get_characters_character_id_contacts) | **GET** /characters/{character_id}/contacts/ | Get contacts
[**get_characters_character_id_contacts_labels**](ContactsApi.md#get_characters_character_id_contacts_labels) | **GET** /characters/{character_id}/contacts/labels/ | Get contact labels
[**get_corporations_corporation_id_contacts**](ContactsApi.md#get_corporations_corporation_id_contacts) | **GET** /corporations/{corporation_id}/contacts/ | Get corporation contacts
[**get_corporations_corporation_id_contacts_labels**](ContactsApi.md#get_corporations_corporation_id_contacts_labels) | **GET** /corporations/{corporation_id}/contacts/labels/ | Get corporation contact labels
[**post_characters_character_id_contacts**](ContactsApi.md#post_characters_character_id_contacts) | **POST** /characters/{character_id}/contacts/ | Add contacts
[**put_characters_character_id_contacts**](ContactsApi.md#put_characters_character_id_contacts) | **PUT** /characters/{character_id}/contacts/ | Edit contacts


# **delete_characters_character_id_contacts**
> delete_characters_character_id_contacts(character_id, contact_ids, datasource=datasource, token=token)

Delete contacts

Bulk delete contacts  --- Alternate route: `/dev/characters/{character_id}/contacts/`  Alternate route: `/v2/characters/{character_id}/contacts/` 

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
api_instance = eve_swagger_api.ContactsApi(eve_swagger_api.ApiClient(configuration))
character_id = 56 # int | An EVE character ID
contact_ids = [56] # list[int] | A list of contacts to delete
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
token = 'token_example' # str | Access token to use if unable to set a header (optional)

try:
    # Delete contacts
    api_instance.delete_characters_character_id_contacts(character_id, contact_ids, datasource=datasource, token=token)
except ApiException as e:
    print("Exception when calling ContactsApi->delete_characters_character_id_contacts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| An EVE character ID | 
 **contact_ids** | [**list[int]**](int.md)| A list of contacts to delete | 
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

# **get_alliances_alliance_id_contacts**
> list[GetAlliancesAllianceIdContacts200Ok] get_alliances_alliance_id_contacts(alliance_id, datasource=datasource, if_none_match=if_none_match, page=page, token=token)

Get alliance contacts

Return contacts of an alliance  --- Alternate route: `/dev/alliances/{alliance_id}/contacts/`  Alternate route: `/v2/alliances/{alliance_id}/contacts/`  --- This route is cached for up to 300 seconds

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
api_instance = eve_swagger_api.ContactsApi(eve_swagger_api.ApiClient(configuration))
alliance_id = 56 # int | An EVE alliance ID
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
page = 1 # int | Which page of results to return (optional) (default to 1)
token = 'token_example' # str | Access token to use if unable to set a header (optional)

try:
    # Get alliance contacts
    api_response = api_instance.get_alliances_alliance_id_contacts(alliance_id, datasource=datasource, if_none_match=if_none_match, page=page, token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->get_alliances_alliance_id_contacts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alliance_id** | **int**| An EVE alliance ID | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to tranquility]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **page** | **int**| Which page of results to return | [optional] [default to 1]
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

[**list[GetAlliancesAllianceIdContacts200Ok]**](GetAlliancesAllianceIdContacts200Ok.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alliances_alliance_id_contacts_labels**
> list[GetAlliancesAllianceIdContactsLabels200Ok] get_alliances_alliance_id_contacts_labels(alliance_id, datasource=datasource, if_none_match=if_none_match, token=token)

Get alliance contact labels

Return custom labels for an alliance's contacts  --- Alternate route: `/dev/alliances/{alliance_id}/contacts/labels/`  Alternate route: `/legacy/alliances/{alliance_id}/contacts/labels/`  Alternate route: `/v1/alliances/{alliance_id}/contacts/labels/`  --- This route is cached for up to 300 seconds

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
api_instance = eve_swagger_api.ContactsApi(eve_swagger_api.ApiClient(configuration))
alliance_id = 56 # int | An EVE alliance ID
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
token = 'token_example' # str | Access token to use if unable to set a header (optional)

try:
    # Get alliance contact labels
    api_response = api_instance.get_alliances_alliance_id_contacts_labels(alliance_id, datasource=datasource, if_none_match=if_none_match, token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->get_alliances_alliance_id_contacts_labels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alliance_id** | **int**| An EVE alliance ID | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to tranquility]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

[**list[GetAlliancesAllianceIdContactsLabels200Ok]**](GetAlliancesAllianceIdContactsLabels200Ok.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_characters_character_id_contacts**
> list[GetCharactersCharacterIdContacts200Ok] get_characters_character_id_contacts(character_id, datasource=datasource, if_none_match=if_none_match, page=page, token=token)

Get contacts

Return contacts of a character  --- Alternate route: `/dev/characters/{character_id}/contacts/`  Alternate route: `/v2/characters/{character_id}/contacts/`  --- This route is cached for up to 300 seconds

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
api_instance = eve_swagger_api.ContactsApi(eve_swagger_api.ApiClient(configuration))
character_id = 56 # int | An EVE character ID
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
page = 1 # int | Which page of results to return (optional) (default to 1)
token = 'token_example' # str | Access token to use if unable to set a header (optional)

try:
    # Get contacts
    api_response = api_instance.get_characters_character_id_contacts(character_id, datasource=datasource, if_none_match=if_none_match, page=page, token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->get_characters_character_id_contacts: %s\n" % e)
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

[**list[GetCharactersCharacterIdContacts200Ok]**](GetCharactersCharacterIdContacts200Ok.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_characters_character_id_contacts_labels**
> list[GetCharactersCharacterIdContactsLabels200Ok] get_characters_character_id_contacts_labels(character_id, datasource=datasource, if_none_match=if_none_match, token=token)

Get contact labels

Return custom labels for a character's contacts  --- Alternate route: `/dev/characters/{character_id}/contacts/labels/`  Alternate route: `/legacy/characters/{character_id}/contacts/labels/`  Alternate route: `/v1/characters/{character_id}/contacts/labels/`  --- This route is cached for up to 300 seconds

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
api_instance = eve_swagger_api.ContactsApi(eve_swagger_api.ApiClient(configuration))
character_id = 56 # int | An EVE character ID
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
token = 'token_example' # str | Access token to use if unable to set a header (optional)

try:
    # Get contact labels
    api_response = api_instance.get_characters_character_id_contacts_labels(character_id, datasource=datasource, if_none_match=if_none_match, token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->get_characters_character_id_contacts_labels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| An EVE character ID | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to tranquility]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

[**list[GetCharactersCharacterIdContactsLabels200Ok]**](GetCharactersCharacterIdContactsLabels200Ok.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_corporations_corporation_id_contacts**
> list[GetCorporationsCorporationIdContacts200Ok] get_corporations_corporation_id_contacts(corporation_id, datasource=datasource, if_none_match=if_none_match, page=page, token=token)

Get corporation contacts

Return contacts of a corporation  --- Alternate route: `/dev/corporations/{corporation_id}/contacts/`  Alternate route: `/v2/corporations/{corporation_id}/contacts/`  --- This route is cached for up to 300 seconds

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
api_instance = eve_swagger_api.ContactsApi(eve_swagger_api.ApiClient(configuration))
corporation_id = 56 # int | An EVE corporation ID
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
page = 1 # int | Which page of results to return (optional) (default to 1)
token = 'token_example' # str | Access token to use if unable to set a header (optional)

try:
    # Get corporation contacts
    api_response = api_instance.get_corporations_corporation_id_contacts(corporation_id, datasource=datasource, if_none_match=if_none_match, page=page, token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->get_corporations_corporation_id_contacts: %s\n" % e)
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

[**list[GetCorporationsCorporationIdContacts200Ok]**](GetCorporationsCorporationIdContacts200Ok.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_corporations_corporation_id_contacts_labels**
> list[GetCorporationsCorporationIdContactsLabels200Ok] get_corporations_corporation_id_contacts_labels(corporation_id, datasource=datasource, if_none_match=if_none_match, token=token)

Get corporation contact labels

Return custom labels for a corporation's contacts  --- Alternate route: `/dev/corporations/{corporation_id}/contacts/labels/`  Alternate route: `/legacy/corporations/{corporation_id}/contacts/labels/`  Alternate route: `/v1/corporations/{corporation_id}/contacts/labels/`  --- This route is cached for up to 300 seconds

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
api_instance = eve_swagger_api.ContactsApi(eve_swagger_api.ApiClient(configuration))
corporation_id = 56 # int | An EVE corporation ID
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
token = 'token_example' # str | Access token to use if unable to set a header (optional)

try:
    # Get corporation contact labels
    api_response = api_instance.get_corporations_corporation_id_contacts_labels(corporation_id, datasource=datasource, if_none_match=if_none_match, token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->get_corporations_corporation_id_contacts_labels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corporation_id** | **int**| An EVE corporation ID | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to tranquility]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

[**list[GetCorporationsCorporationIdContactsLabels200Ok]**](GetCorporationsCorporationIdContactsLabels200Ok.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_characters_character_id_contacts**
> list[int] post_characters_character_id_contacts(character_id, contact_ids, standing, datasource=datasource, label_ids=label_ids, token=token, watched=watched)

Add contacts

Bulk add contacts with same settings  --- Alternate route: `/dev/characters/{character_id}/contacts/`  Alternate route: `/v2/characters/{character_id}/contacts/` 

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
api_instance = eve_swagger_api.ContactsApi(eve_swagger_api.ApiClient(configuration))
character_id = 56 # int | An EVE character ID
contact_ids = [eve_swagger_api.list[int]()] # list[int] | A list of contacts
standing = 3.4 # float | Standing for the contact
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
label_ids = [56] # list[int] | Add custom labels to the new contact (optional)
token = 'token_example' # str | Access token to use if unable to set a header (optional)
watched = false # bool | Whether the contact should be watched, note this is only effective on characters (optional) (default to false)

try:
    # Add contacts
    api_response = api_instance.post_characters_character_id_contacts(character_id, contact_ids, standing, datasource=datasource, label_ids=label_ids, token=token, watched=watched)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->post_characters_character_id_contacts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| An EVE character ID | 
 **contact_ids** | **list[int]**| A list of contacts | 
 **standing** | **float**| Standing for the contact | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to tranquility]
 **label_ids** | [**list[int]**](int.md)| Add custom labels to the new contact | [optional] 
 **token** | **str**| Access token to use if unable to set a header | [optional] 
 **watched** | **bool**| Whether the contact should be watched, note this is only effective on characters | [optional] [default to false]

### Return type

**list[int]**

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_characters_character_id_contacts**
> put_characters_character_id_contacts(character_id, contact_ids, standing, datasource=datasource, label_ids=label_ids, token=token, watched=watched)

Edit contacts

Bulk edit contacts with same settings  --- Alternate route: `/dev/characters/{character_id}/contacts/`  Alternate route: `/v2/characters/{character_id}/contacts/` 

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
api_instance = eve_swagger_api.ContactsApi(eve_swagger_api.ApiClient(configuration))
character_id = 56 # int | An EVE character ID
contact_ids = [eve_swagger_api.list[int]()] # list[int] | A list of contacts
standing = 3.4 # float | Standing for the contact
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
label_ids = [56] # list[int] | Add custom labels to the contact (optional)
token = 'token_example' # str | Access token to use if unable to set a header (optional)
watched = false # bool | Whether the contact should be watched, note this is only effective on characters (optional) (default to false)

try:
    # Edit contacts
    api_instance.put_characters_character_id_contacts(character_id, contact_ids, standing, datasource=datasource, label_ids=label_ids, token=token, watched=watched)
except ApiException as e:
    print("Exception when calling ContactsApi->put_characters_character_id_contacts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| An EVE character ID | 
 **contact_ids** | **list[int]**| A list of contacts | 
 **standing** | **float**| Standing for the contact | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to tranquility]
 **label_ids** | [**list[int]**](int.md)| Add custom labels to the contact | [optional] 
 **token** | **str**| Access token to use if unable to set a header | [optional] 
 **watched** | **bool**| Whether the contact should be watched, note this is only effective on characters | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

