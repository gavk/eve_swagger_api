# eve_swagger_api.CorporationApi

All URIs are relative to *https://esi.evetech.net/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_corporations_corporation_id**](CorporationApi.md#get_corporations_corporation_id) | **GET** /corporations/{corporation_id}/ | Get corporation information
[**get_corporations_corporation_id_alliancehistory**](CorporationApi.md#get_corporations_corporation_id_alliancehistory) | **GET** /corporations/{corporation_id}/alliancehistory/ | Get alliance history
[**get_corporations_corporation_id_blueprints**](CorporationApi.md#get_corporations_corporation_id_blueprints) | **GET** /corporations/{corporation_id}/blueprints/ | Get corporation blueprints
[**get_corporations_corporation_id_containers_logs**](CorporationApi.md#get_corporations_corporation_id_containers_logs) | **GET** /corporations/{corporation_id}/containers/logs/ | Get all corporation ALSC logs
[**get_corporations_corporation_id_divisions**](CorporationApi.md#get_corporations_corporation_id_divisions) | **GET** /corporations/{corporation_id}/divisions/ | Get corporation divisions
[**get_corporations_corporation_id_facilities**](CorporationApi.md#get_corporations_corporation_id_facilities) | **GET** /corporations/{corporation_id}/facilities/ | Get corporation facilities
[**get_corporations_corporation_id_icons**](CorporationApi.md#get_corporations_corporation_id_icons) | **GET** /corporations/{corporation_id}/icons/ | Get corporation icon
[**get_corporations_corporation_id_medals**](CorporationApi.md#get_corporations_corporation_id_medals) | **GET** /corporations/{corporation_id}/medals/ | Get corporation medals
[**get_corporations_corporation_id_medals_issued**](CorporationApi.md#get_corporations_corporation_id_medals_issued) | **GET** /corporations/{corporation_id}/medals/issued/ | Get corporation issued medals
[**get_corporations_corporation_id_members**](CorporationApi.md#get_corporations_corporation_id_members) | **GET** /corporations/{corporation_id}/members/ | Get corporation members
[**get_corporations_corporation_id_members_limit**](CorporationApi.md#get_corporations_corporation_id_members_limit) | **GET** /corporations/{corporation_id}/members/limit/ | Get corporation member limit
[**get_corporations_corporation_id_members_titles**](CorporationApi.md#get_corporations_corporation_id_members_titles) | **GET** /corporations/{corporation_id}/members/titles/ | Get corporation&#39;s members&#39; titles
[**get_corporations_corporation_id_membertracking**](CorporationApi.md#get_corporations_corporation_id_membertracking) | **GET** /corporations/{corporation_id}/membertracking/ | Track corporation members
[**get_corporations_corporation_id_roles**](CorporationApi.md#get_corporations_corporation_id_roles) | **GET** /corporations/{corporation_id}/roles/ | Get corporation member roles
[**get_corporations_corporation_id_roles_history**](CorporationApi.md#get_corporations_corporation_id_roles_history) | **GET** /corporations/{corporation_id}/roles/history/ | Get corporation member roles history
[**get_corporations_corporation_id_shareholders**](CorporationApi.md#get_corporations_corporation_id_shareholders) | **GET** /corporations/{corporation_id}/shareholders/ | Get corporation shareholders
[**get_corporations_corporation_id_standings**](CorporationApi.md#get_corporations_corporation_id_standings) | **GET** /corporations/{corporation_id}/standings/ | Get corporation standings
[**get_corporations_corporation_id_starbases**](CorporationApi.md#get_corporations_corporation_id_starbases) | **GET** /corporations/{corporation_id}/starbases/ | Get corporation starbases (POSes)
[**get_corporations_corporation_id_starbases_starbase_id**](CorporationApi.md#get_corporations_corporation_id_starbases_starbase_id) | **GET** /corporations/{corporation_id}/starbases/{starbase_id}/ | Get starbase (POS) detail
[**get_corporations_corporation_id_structures**](CorporationApi.md#get_corporations_corporation_id_structures) | **GET** /corporations/{corporation_id}/structures/ | Get corporation structures
[**get_corporations_corporation_id_titles**](CorporationApi.md#get_corporations_corporation_id_titles) | **GET** /corporations/{corporation_id}/titles/ | Get corporation titles
[**get_corporations_npccorps**](CorporationApi.md#get_corporations_npccorps) | **GET** /corporations/npccorps/ | Get npc corporations


# **get_corporations_corporation_id**
> GetCorporationsCorporationIdOk get_corporations_corporation_id(corporation_id, datasource=datasource, if_none_match=if_none_match)

Get corporation information

Public information about a corporation  --- Alternate route: `/dev/corporations/{corporation_id}/`  Alternate route: `/v5/corporations/{corporation_id}/`  --- This route is cached for up to 3600 seconds

### Example
```python
from __future__ import print_function
import time
import eve_swagger_api
from eve_swagger_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = eve_swagger_api.CorporationApi()
corporation_id = 56 # int | An EVE corporation ID
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)

try:
    # Get corporation information
    api_response = api_instance.get_corporations_corporation_id(corporation_id, datasource=datasource, if_none_match=if_none_match)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CorporationApi->get_corporations_corporation_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corporation_id** | **int**| An EVE corporation ID | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to tranquility]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 

### Return type

[**GetCorporationsCorporationIdOk**](GetCorporationsCorporationIdOk.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_corporations_corporation_id_alliancehistory**
> list[GetCorporationsCorporationIdAlliancehistory200Ok] get_corporations_corporation_id_alliancehistory(corporation_id, datasource=datasource, if_none_match=if_none_match)

Get alliance history

Get a list of all the alliances a corporation has been a member of  --- Alternate route: `/dev/corporations/{corporation_id}/alliancehistory/`  Alternate route: `/v3/corporations/{corporation_id}/alliancehistory/`  --- This route is cached for up to 3600 seconds

### Example
```python
from __future__ import print_function
import time
import eve_swagger_api
from eve_swagger_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = eve_swagger_api.CorporationApi()
corporation_id = 56 # int | An EVE corporation ID
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)

try:
    # Get alliance history
    api_response = api_instance.get_corporations_corporation_id_alliancehistory(corporation_id, datasource=datasource, if_none_match=if_none_match)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CorporationApi->get_corporations_corporation_id_alliancehistory: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corporation_id** | **int**| An EVE corporation ID | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to tranquility]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 

### Return type

[**list[GetCorporationsCorporationIdAlliancehistory200Ok]**](GetCorporationsCorporationIdAlliancehistory200Ok.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_corporations_corporation_id_blueprints**
> list[GetCorporationsCorporationIdBlueprints200Ok] get_corporations_corporation_id_blueprints(corporation_id, datasource=datasource, if_none_match=if_none_match, page=page, token=token)

Get corporation blueprints

Returns a list of blueprints the corporation owns  --- Alternate route: `/dev/corporations/{corporation_id}/blueprints/`  Alternate route: `/v3/corporations/{corporation_id}/blueprints/`  --- This route is cached for up to 3600 seconds  --- Requires one of the following EVE corporation role(s): Director 

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
api_instance = eve_swagger_api.CorporationApi(eve_swagger_api.ApiClient(configuration))
corporation_id = 56 # int | An EVE corporation ID
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
page = 1 # int | Which page of results to return (optional) (default to 1)
token = 'token_example' # str | Access token to use if unable to set a header (optional)

try:
    # Get corporation blueprints
    api_response = api_instance.get_corporations_corporation_id_blueprints(corporation_id, datasource=datasource, if_none_match=if_none_match, page=page, token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CorporationApi->get_corporations_corporation_id_blueprints: %s\n" % e)
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

[**list[GetCorporationsCorporationIdBlueprints200Ok]**](GetCorporationsCorporationIdBlueprints200Ok.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_corporations_corporation_id_containers_logs**
> list[GetCorporationsCorporationIdContainersLogs200Ok] get_corporations_corporation_id_containers_logs(corporation_id, datasource=datasource, if_none_match=if_none_match, page=page, token=token)

Get all corporation ALSC logs

Returns logs recorded in the past seven days from all audit log secure containers (ALSC) owned by a given corporation  --- Alternate route: `/dev/corporations/{corporation_id}/containers/logs/`  Alternate route: `/v3/corporations/{corporation_id}/containers/logs/`  --- This route is cached for up to 600 seconds  --- Requires one of the following EVE corporation role(s): Director 

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
api_instance = eve_swagger_api.CorporationApi(eve_swagger_api.ApiClient(configuration))
corporation_id = 56 # int | An EVE corporation ID
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
page = 1 # int | Which page of results to return (optional) (default to 1)
token = 'token_example' # str | Access token to use if unable to set a header (optional)

try:
    # Get all corporation ALSC logs
    api_response = api_instance.get_corporations_corporation_id_containers_logs(corporation_id, datasource=datasource, if_none_match=if_none_match, page=page, token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CorporationApi->get_corporations_corporation_id_containers_logs: %s\n" % e)
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

[**list[GetCorporationsCorporationIdContainersLogs200Ok]**](GetCorporationsCorporationIdContainersLogs200Ok.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_corporations_corporation_id_divisions**
> GetCorporationsCorporationIdDivisionsOk get_corporations_corporation_id_divisions(corporation_id, datasource=datasource, if_none_match=if_none_match, token=token)

Get corporation divisions

Return corporation hangar and wallet division names, only show if a division is not using the default name  --- Alternate route: `/dev/corporations/{corporation_id}/divisions/`  Alternate route: `/v2/corporations/{corporation_id}/divisions/`  --- This route is cached for up to 3600 seconds  --- Requires one of the following EVE corporation role(s): Director 

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
api_instance = eve_swagger_api.CorporationApi(eve_swagger_api.ApiClient(configuration))
corporation_id = 56 # int | An EVE corporation ID
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
token = 'token_example' # str | Access token to use if unable to set a header (optional)

try:
    # Get corporation divisions
    api_response = api_instance.get_corporations_corporation_id_divisions(corporation_id, datasource=datasource, if_none_match=if_none_match, token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CorporationApi->get_corporations_corporation_id_divisions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corporation_id** | **int**| An EVE corporation ID | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to tranquility]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

[**GetCorporationsCorporationIdDivisionsOk**](GetCorporationsCorporationIdDivisionsOk.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_corporations_corporation_id_facilities**
> list[GetCorporationsCorporationIdFacilities200Ok] get_corporations_corporation_id_facilities(corporation_id, datasource=datasource, if_none_match=if_none_match, token=token)

Get corporation facilities

Return a corporation's facilities  --- Alternate route: `/dev/corporations/{corporation_id}/facilities/`  Alternate route: `/v2/corporations/{corporation_id}/facilities/`  --- This route is cached for up to 3600 seconds  --- Requires one of the following EVE corporation role(s): Factory_Manager 

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
api_instance = eve_swagger_api.CorporationApi(eve_swagger_api.ApiClient(configuration))
corporation_id = 56 # int | An EVE corporation ID
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
token = 'token_example' # str | Access token to use if unable to set a header (optional)

try:
    # Get corporation facilities
    api_response = api_instance.get_corporations_corporation_id_facilities(corporation_id, datasource=datasource, if_none_match=if_none_match, token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CorporationApi->get_corporations_corporation_id_facilities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corporation_id** | **int**| An EVE corporation ID | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to tranquility]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

[**list[GetCorporationsCorporationIdFacilities200Ok]**](GetCorporationsCorporationIdFacilities200Ok.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_corporations_corporation_id_icons**
> GetCorporationsCorporationIdIconsOk get_corporations_corporation_id_icons(corporation_id, datasource=datasource, if_none_match=if_none_match)

Get corporation icon

Get the icon urls for a corporation  --- Alternate route: `/dev/corporations/{corporation_id}/icons/`  Alternate route: `/v2/corporations/{corporation_id}/icons/`  --- This route is cached for up to 3600 seconds

### Example
```python
from __future__ import print_function
import time
import eve_swagger_api
from eve_swagger_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = eve_swagger_api.CorporationApi()
corporation_id = 56 # int | An EVE corporation ID
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)

try:
    # Get corporation icon
    api_response = api_instance.get_corporations_corporation_id_icons(corporation_id, datasource=datasource, if_none_match=if_none_match)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CorporationApi->get_corporations_corporation_id_icons: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corporation_id** | **int**| An EVE corporation ID | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to tranquility]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 

### Return type

[**GetCorporationsCorporationIdIconsOk**](GetCorporationsCorporationIdIconsOk.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_corporations_corporation_id_medals**
> list[GetCorporationsCorporationIdMedals200Ok] get_corporations_corporation_id_medals(corporation_id, datasource=datasource, if_none_match=if_none_match, page=page, token=token)

Get corporation medals

Returns a corporation's medals  --- Alternate route: `/dev/corporations/{corporation_id}/medals/`  Alternate route: `/v2/corporations/{corporation_id}/medals/`  --- This route is cached for up to 3600 seconds

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
api_instance = eve_swagger_api.CorporationApi(eve_swagger_api.ApiClient(configuration))
corporation_id = 56 # int | An EVE corporation ID
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
page = 1 # int | Which page of results to return (optional) (default to 1)
token = 'token_example' # str | Access token to use if unable to set a header (optional)

try:
    # Get corporation medals
    api_response = api_instance.get_corporations_corporation_id_medals(corporation_id, datasource=datasource, if_none_match=if_none_match, page=page, token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CorporationApi->get_corporations_corporation_id_medals: %s\n" % e)
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

[**list[GetCorporationsCorporationIdMedals200Ok]**](GetCorporationsCorporationIdMedals200Ok.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_corporations_corporation_id_medals_issued**
> list[GetCorporationsCorporationIdMedalsIssued200Ok] get_corporations_corporation_id_medals_issued(corporation_id, datasource=datasource, if_none_match=if_none_match, page=page, token=token)

Get corporation issued medals

Returns medals issued by a corporation  --- Alternate route: `/dev/corporations/{corporation_id}/medals/issued/`  Alternate route: `/v2/corporations/{corporation_id}/medals/issued/`  --- This route is cached for up to 3600 seconds  --- Requires one of the following EVE corporation role(s): Director 

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
api_instance = eve_swagger_api.CorporationApi(eve_swagger_api.ApiClient(configuration))
corporation_id = 56 # int | An EVE corporation ID
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
page = 1 # int | Which page of results to return (optional) (default to 1)
token = 'token_example' # str | Access token to use if unable to set a header (optional)

try:
    # Get corporation issued medals
    api_response = api_instance.get_corporations_corporation_id_medals_issued(corporation_id, datasource=datasource, if_none_match=if_none_match, page=page, token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CorporationApi->get_corporations_corporation_id_medals_issued: %s\n" % e)
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

[**list[GetCorporationsCorporationIdMedalsIssued200Ok]**](GetCorporationsCorporationIdMedalsIssued200Ok.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_corporations_corporation_id_members**
> list[int] get_corporations_corporation_id_members(corporation_id, datasource=datasource, if_none_match=if_none_match, token=token)

Get corporation members

Return the current member list of a corporation, the token's character need to be a member of the corporation.  --- Alternate route: `/dev/corporations/{corporation_id}/members/`  Alternate route: `/v4/corporations/{corporation_id}/members/`  --- This route is cached for up to 3600 seconds

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
api_instance = eve_swagger_api.CorporationApi(eve_swagger_api.ApiClient(configuration))
corporation_id = 56 # int | An EVE corporation ID
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
token = 'token_example' # str | Access token to use if unable to set a header (optional)

try:
    # Get corporation members
    api_response = api_instance.get_corporations_corporation_id_members(corporation_id, datasource=datasource, if_none_match=if_none_match, token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CorporationApi->get_corporations_corporation_id_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corporation_id** | **int**| An EVE corporation ID | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to tranquility]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

**list[int]**

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_corporations_corporation_id_members_limit**
> int get_corporations_corporation_id_members_limit(corporation_id, datasource=datasource, if_none_match=if_none_match, token=token)

Get corporation member limit

Return a corporation's member limit, not including CEO himself  --- Alternate route: `/dev/corporations/{corporation_id}/members/limit/`  Alternate route: `/v2/corporations/{corporation_id}/members/limit/`  --- This route is cached for up to 3600 seconds  --- Requires one of the following EVE corporation role(s): Director 

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
api_instance = eve_swagger_api.CorporationApi(eve_swagger_api.ApiClient(configuration))
corporation_id = 56 # int | An EVE corporation ID
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
token = 'token_example' # str | Access token to use if unable to set a header (optional)

try:
    # Get corporation member limit
    api_response = api_instance.get_corporations_corporation_id_members_limit(corporation_id, datasource=datasource, if_none_match=if_none_match, token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CorporationApi->get_corporations_corporation_id_members_limit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corporation_id** | **int**| An EVE corporation ID | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to tranquility]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

**int**

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_corporations_corporation_id_members_titles**
> list[GetCorporationsCorporationIdMembersTitles200Ok] get_corporations_corporation_id_members_titles(corporation_id, datasource=datasource, if_none_match=if_none_match, token=token)

Get corporation's members' titles

Returns a corporation's members' titles  --- Alternate route: `/dev/corporations/{corporation_id}/members/titles/`  Alternate route: `/v2/corporations/{corporation_id}/members/titles/`  --- This route is cached for up to 3600 seconds  --- Requires one of the following EVE corporation role(s): Director 

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
api_instance = eve_swagger_api.CorporationApi(eve_swagger_api.ApiClient(configuration))
corporation_id = 56 # int | An EVE corporation ID
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
token = 'token_example' # str | Access token to use if unable to set a header (optional)

try:
    # Get corporation's members' titles
    api_response = api_instance.get_corporations_corporation_id_members_titles(corporation_id, datasource=datasource, if_none_match=if_none_match, token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CorporationApi->get_corporations_corporation_id_members_titles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corporation_id** | **int**| An EVE corporation ID | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to tranquility]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

[**list[GetCorporationsCorporationIdMembersTitles200Ok]**](GetCorporationsCorporationIdMembersTitles200Ok.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_corporations_corporation_id_membertracking**
> list[GetCorporationsCorporationIdMembertracking200Ok] get_corporations_corporation_id_membertracking(corporation_id, datasource=datasource, if_none_match=if_none_match, token=token)

Track corporation members

Returns additional information about a corporation's members which helps tracking their activities  --- Alternate route: `/dev/corporations/{corporation_id}/membertracking/`  Alternate route: `/v2/corporations/{corporation_id}/membertracking/`  --- This route is cached for up to 3600 seconds  --- Requires one of the following EVE corporation role(s): Director 

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
api_instance = eve_swagger_api.CorporationApi(eve_swagger_api.ApiClient(configuration))
corporation_id = 56 # int | An EVE corporation ID
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
token = 'token_example' # str | Access token to use if unable to set a header (optional)

try:
    # Track corporation members
    api_response = api_instance.get_corporations_corporation_id_membertracking(corporation_id, datasource=datasource, if_none_match=if_none_match, token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CorporationApi->get_corporations_corporation_id_membertracking: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corporation_id** | **int**| An EVE corporation ID | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to tranquility]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

[**list[GetCorporationsCorporationIdMembertracking200Ok]**](GetCorporationsCorporationIdMembertracking200Ok.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_corporations_corporation_id_roles**
> list[GetCorporationsCorporationIdRoles200Ok] get_corporations_corporation_id_roles(corporation_id, datasource=datasource, if_none_match=if_none_match, token=token)

Get corporation member roles

Return the roles of all members if the character has the personnel manager role or any grantable role.  --- Alternate route: `/dev/corporations/{corporation_id}/roles/`  Alternate route: `/v2/corporations/{corporation_id}/roles/`  --- This route is cached for up to 3600 seconds

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
api_instance = eve_swagger_api.CorporationApi(eve_swagger_api.ApiClient(configuration))
corporation_id = 56 # int | An EVE corporation ID
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
token = 'token_example' # str | Access token to use if unable to set a header (optional)

try:
    # Get corporation member roles
    api_response = api_instance.get_corporations_corporation_id_roles(corporation_id, datasource=datasource, if_none_match=if_none_match, token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CorporationApi->get_corporations_corporation_id_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corporation_id** | **int**| An EVE corporation ID | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to tranquility]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

[**list[GetCorporationsCorporationIdRoles200Ok]**](GetCorporationsCorporationIdRoles200Ok.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_corporations_corporation_id_roles_history**
> list[GetCorporationsCorporationIdRolesHistory200Ok] get_corporations_corporation_id_roles_history(corporation_id, datasource=datasource, if_none_match=if_none_match, page=page, token=token)

Get corporation member roles history

Return how roles have changed for a coporation's members, up to a month  --- Alternate route: `/dev/corporations/{corporation_id}/roles/history/`  Alternate route: `/v2/corporations/{corporation_id}/roles/history/`  --- This route is cached for up to 3600 seconds  --- Requires one of the following EVE corporation role(s): Director 

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
api_instance = eve_swagger_api.CorporationApi(eve_swagger_api.ApiClient(configuration))
corporation_id = 56 # int | An EVE corporation ID
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
page = 1 # int | Which page of results to return (optional) (default to 1)
token = 'token_example' # str | Access token to use if unable to set a header (optional)

try:
    # Get corporation member roles history
    api_response = api_instance.get_corporations_corporation_id_roles_history(corporation_id, datasource=datasource, if_none_match=if_none_match, page=page, token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CorporationApi->get_corporations_corporation_id_roles_history: %s\n" % e)
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

[**list[GetCorporationsCorporationIdRolesHistory200Ok]**](GetCorporationsCorporationIdRolesHistory200Ok.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_corporations_corporation_id_shareholders**
> list[GetCorporationsCorporationIdShareholders200Ok] get_corporations_corporation_id_shareholders(corporation_id, datasource=datasource, if_none_match=if_none_match, page=page, token=token)

Get corporation shareholders

Return the current shareholders of a corporation.  --- Alternate route: `/dev/corporations/{corporation_id}/shareholders/`  Alternate route: `/legacy/corporations/{corporation_id}/shareholders/`  Alternate route: `/v1/corporations/{corporation_id}/shareholders/`  --- This route is cached for up to 3600 seconds  --- Requires one of the following EVE corporation role(s): Director 

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
api_instance = eve_swagger_api.CorporationApi(eve_swagger_api.ApiClient(configuration))
corporation_id = 56 # int | An EVE corporation ID
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
page = 1 # int | Which page of results to return (optional) (default to 1)
token = 'token_example' # str | Access token to use if unable to set a header (optional)

try:
    # Get corporation shareholders
    api_response = api_instance.get_corporations_corporation_id_shareholders(corporation_id, datasource=datasource, if_none_match=if_none_match, page=page, token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CorporationApi->get_corporations_corporation_id_shareholders: %s\n" % e)
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

[**list[GetCorporationsCorporationIdShareholders200Ok]**](GetCorporationsCorporationIdShareholders200Ok.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_corporations_corporation_id_standings**
> list[GetCorporationsCorporationIdStandings200Ok] get_corporations_corporation_id_standings(corporation_id, datasource=datasource, if_none_match=if_none_match, page=page, token=token)

Get corporation standings

Return corporation standings from agents, NPC corporations, and factions  --- Alternate route: `/dev/corporations/{corporation_id}/standings/`  Alternate route: `/v2/corporations/{corporation_id}/standings/`  --- This route is cached for up to 3600 seconds

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
api_instance = eve_swagger_api.CorporationApi(eve_swagger_api.ApiClient(configuration))
corporation_id = 56 # int | An EVE corporation ID
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
page = 1 # int | Which page of results to return (optional) (default to 1)
token = 'token_example' # str | Access token to use if unable to set a header (optional)

try:
    # Get corporation standings
    api_response = api_instance.get_corporations_corporation_id_standings(corporation_id, datasource=datasource, if_none_match=if_none_match, page=page, token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CorporationApi->get_corporations_corporation_id_standings: %s\n" % e)
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

[**list[GetCorporationsCorporationIdStandings200Ok]**](GetCorporationsCorporationIdStandings200Ok.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_corporations_corporation_id_starbases**
> list[GetCorporationsCorporationIdStarbases200Ok] get_corporations_corporation_id_starbases(corporation_id, datasource=datasource, if_none_match=if_none_match, page=page, token=token)

Get corporation starbases (POSes)

Returns list of corporation starbases (POSes)  --- Alternate route: `/dev/corporations/{corporation_id}/starbases/`  Alternate route: `/v2/corporations/{corporation_id}/starbases/`  --- This route is cached for up to 3600 seconds  --- Requires one of the following EVE corporation role(s): Director 

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
api_instance = eve_swagger_api.CorporationApi(eve_swagger_api.ApiClient(configuration))
corporation_id = 56 # int | An EVE corporation ID
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
page = 1 # int | Which page of results to return (optional) (default to 1)
token = 'token_example' # str | Access token to use if unable to set a header (optional)

try:
    # Get corporation starbases (POSes)
    api_response = api_instance.get_corporations_corporation_id_starbases(corporation_id, datasource=datasource, if_none_match=if_none_match, page=page, token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CorporationApi->get_corporations_corporation_id_starbases: %s\n" % e)
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

[**list[GetCorporationsCorporationIdStarbases200Ok]**](GetCorporationsCorporationIdStarbases200Ok.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_corporations_corporation_id_starbases_starbase_id**
> GetCorporationsCorporationIdStarbasesStarbaseIdOk get_corporations_corporation_id_starbases_starbase_id(corporation_id, starbase_id, system_id, datasource=datasource, if_none_match=if_none_match, token=token)

Get starbase (POS) detail

Returns various settings and fuels of a starbase (POS)  --- Alternate route: `/dev/corporations/{corporation_id}/starbases/{starbase_id}/`  Alternate route: `/v2/corporations/{corporation_id}/starbases/{starbase_id}/`  --- This route is cached for up to 3600 seconds  --- Requires one of the following EVE corporation role(s): Director 

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
api_instance = eve_swagger_api.CorporationApi(eve_swagger_api.ApiClient(configuration))
corporation_id = 56 # int | An EVE corporation ID
starbase_id = 789 # int | An EVE starbase (POS) ID
system_id = 56 # int | The solar system this starbase (POS) is located in,
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
token = 'token_example' # str | Access token to use if unable to set a header (optional)

try:
    # Get starbase (POS) detail
    api_response = api_instance.get_corporations_corporation_id_starbases_starbase_id(corporation_id, starbase_id, system_id, datasource=datasource, if_none_match=if_none_match, token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CorporationApi->get_corporations_corporation_id_starbases_starbase_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corporation_id** | **int**| An EVE corporation ID | 
 **starbase_id** | **int**| An EVE starbase (POS) ID | 
 **system_id** | **int**| The solar system this starbase (POS) is located in, | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to tranquility]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

[**GetCorporationsCorporationIdStarbasesStarbaseIdOk**](GetCorporationsCorporationIdStarbasesStarbaseIdOk.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_corporations_corporation_id_structures**
> list[GetCorporationsCorporationIdStructures200Ok] get_corporations_corporation_id_structures(corporation_id, accept_language=accept_language, datasource=datasource, if_none_match=if_none_match, language=language, page=page, token=token)

Get corporation structures

Get a list of corporation structures. This route's version includes the changes to structures detailed in this blog: https://www.eveonline.com/article/upwell-2.0-structures-changes-coming-on-february-13th  --- Alternate route: `/dev/corporations/{corporation_id}/structures/`  Alternate route: `/v4/corporations/{corporation_id}/structures/`  --- This route is cached for up to 3600 seconds  --- Requires one of the following EVE corporation role(s): Station_Manager 

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
api_instance = eve_swagger_api.CorporationApi(eve_swagger_api.ApiClient(configuration))
corporation_id = 56 # int | An EVE corporation ID
accept_language = 'en' # str | Language to use in the response (optional) (default to en)
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
language = 'en' # str | Language to use in the response, takes precedence over Accept-Language (optional) (default to en)
page = 1 # int | Which page of results to return (optional) (default to 1)
token = 'token_example' # str | Access token to use if unable to set a header (optional)

try:
    # Get corporation structures
    api_response = api_instance.get_corporations_corporation_id_structures(corporation_id, accept_language=accept_language, datasource=datasource, if_none_match=if_none_match, language=language, page=page, token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CorporationApi->get_corporations_corporation_id_structures: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corporation_id** | **int**| An EVE corporation ID | 
 **accept_language** | **str**| Language to use in the response | [optional] [default to en]
 **datasource** | **str**| The server name you would like data from | [optional] [default to tranquility]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **language** | **str**| Language to use in the response, takes precedence over Accept-Language | [optional] [default to en]
 **page** | **int**| Which page of results to return | [optional] [default to 1]
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

[**list[GetCorporationsCorporationIdStructures200Ok]**](GetCorporationsCorporationIdStructures200Ok.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_corporations_corporation_id_titles**
> list[GetCorporationsCorporationIdTitles200Ok] get_corporations_corporation_id_titles(corporation_id, datasource=datasource, if_none_match=if_none_match, token=token)

Get corporation titles

Returns a corporation's titles  --- Alternate route: `/dev/corporations/{corporation_id}/titles/`  Alternate route: `/v2/corporations/{corporation_id}/titles/`  --- This route is cached for up to 3600 seconds  --- Requires one of the following EVE corporation role(s): Director 

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
api_instance = eve_swagger_api.CorporationApi(eve_swagger_api.ApiClient(configuration))
corporation_id = 56 # int | An EVE corporation ID
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
token = 'token_example' # str | Access token to use if unable to set a header (optional)

try:
    # Get corporation titles
    api_response = api_instance.get_corporations_corporation_id_titles(corporation_id, datasource=datasource, if_none_match=if_none_match, token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CorporationApi->get_corporations_corporation_id_titles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corporation_id** | **int**| An EVE corporation ID | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to tranquility]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

[**list[GetCorporationsCorporationIdTitles200Ok]**](GetCorporationsCorporationIdTitles200Ok.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_corporations_npccorps**
> list[int] get_corporations_npccorps(datasource=datasource, if_none_match=if_none_match)

Get npc corporations

Get a list of npc corporations  --- Alternate route: `/dev/corporations/npccorps/`  Alternate route: `/v2/corporations/npccorps/`  --- This route expires daily at 11:05

### Example
```python
from __future__ import print_function
import time
import eve_swagger_api
from eve_swagger_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = eve_swagger_api.CorporationApi()
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)

try:
    # Get npc corporations
    api_response = api_instance.get_corporations_npccorps(datasource=datasource, if_none_match=if_none_match)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CorporationApi->get_corporations_npccorps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datasource** | **str**| The server name you would like data from | [optional] [default to tranquility]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 

### Return type

**list[int]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

