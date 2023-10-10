# eve_swagger_api.IndustryApi

All URIs are relative to *https://esi.evetech.net/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_characters_character_id_industry_jobs**](IndustryApi.md#get_characters_character_id_industry_jobs) | **GET** /characters/{character_id}/industry/jobs/ | List character industry jobs
[**get_characters_character_id_mining**](IndustryApi.md#get_characters_character_id_mining) | **GET** /characters/{character_id}/mining/ | Character mining ledger
[**get_corporation_corporation_id_mining_extractions**](IndustryApi.md#get_corporation_corporation_id_mining_extractions) | **GET** /corporation/{corporation_id}/mining/extractions/ | Moon extraction timers
[**get_corporation_corporation_id_mining_observers**](IndustryApi.md#get_corporation_corporation_id_mining_observers) | **GET** /corporation/{corporation_id}/mining/observers/ | Corporation mining observers
[**get_corporation_corporation_id_mining_observers_observer_id**](IndustryApi.md#get_corporation_corporation_id_mining_observers_observer_id) | **GET** /corporation/{corporation_id}/mining/observers/{observer_id}/ | Observed corporation mining
[**get_corporations_corporation_id_industry_jobs**](IndustryApi.md#get_corporations_corporation_id_industry_jobs) | **GET** /corporations/{corporation_id}/industry/jobs/ | List corporation industry jobs
[**get_industry_facilities**](IndustryApi.md#get_industry_facilities) | **GET** /industry/facilities/ | List industry facilities
[**get_industry_systems**](IndustryApi.md#get_industry_systems) | **GET** /industry/systems/ | List solar system cost indices


# **get_characters_character_id_industry_jobs**
> list[GetCharactersCharacterIdIndustryJobs200Ok] get_characters_character_id_industry_jobs(character_id, datasource=datasource, if_none_match=if_none_match, include_completed=include_completed, token=token)

List character industry jobs

List industry jobs placed by a character  --- Alternate route: `/dev/characters/{character_id}/industry/jobs/`  Alternate route: `/legacy/characters/{character_id}/industry/jobs/`  Alternate route: `/v1/characters/{character_id}/industry/jobs/`  --- This route is cached for up to 300 seconds

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
api_instance = eve_swagger_api.IndustryApi(eve_swagger_api.ApiClient(configuration))
character_id = 56 # int | An EVE character ID
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
include_completed = true # bool | Whether to retrieve completed character industry jobs. Only includes jobs from the past 90 days (optional)
token = 'token_example' # str | Access token to use if unable to set a header (optional)

try:
    # List character industry jobs
    api_response = api_instance.get_characters_character_id_industry_jobs(character_id, datasource=datasource, if_none_match=if_none_match, include_completed=include_completed, token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndustryApi->get_characters_character_id_industry_jobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| An EVE character ID | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to tranquility]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **include_completed** | **bool**| Whether to retrieve completed character industry jobs. Only includes jobs from the past 90 days | [optional] 
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

[**list[GetCharactersCharacterIdIndustryJobs200Ok]**](GetCharactersCharacterIdIndustryJobs200Ok.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_characters_character_id_mining**
> list[GetCharactersCharacterIdMining200Ok] get_characters_character_id_mining(character_id, datasource=datasource, if_none_match=if_none_match, page=page, token=token)

Character mining ledger

Paginated record of all mining done by a character for the past 30 days   --- Alternate route: `/dev/characters/{character_id}/mining/`  Alternate route: `/legacy/characters/{character_id}/mining/`  Alternate route: `/v1/characters/{character_id}/mining/`  --- This route is cached for up to 600 seconds

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
api_instance = eve_swagger_api.IndustryApi(eve_swagger_api.ApiClient(configuration))
character_id = 56 # int | An EVE character ID
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
page = 1 # int | Which page of results to return (optional) (default to 1)
token = 'token_example' # str | Access token to use if unable to set a header (optional)

try:
    # Character mining ledger
    api_response = api_instance.get_characters_character_id_mining(character_id, datasource=datasource, if_none_match=if_none_match, page=page, token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndustryApi->get_characters_character_id_mining: %s\n" % e)
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

[**list[GetCharactersCharacterIdMining200Ok]**](GetCharactersCharacterIdMining200Ok.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_corporation_corporation_id_mining_extractions**
> list[GetCorporationCorporationIdMiningExtractions200Ok] get_corporation_corporation_id_mining_extractions(corporation_id, datasource=datasource, if_none_match=if_none_match, page=page, token=token)

Moon extraction timers

Extraction timers for all moon chunks being extracted by refineries belonging to a corporation.   --- Alternate route: `/dev/corporation/{corporation_id}/mining/extractions/`  Alternate route: `/legacy/corporation/{corporation_id}/mining/extractions/`  Alternate route: `/v1/corporation/{corporation_id}/mining/extractions/`  --- This route is cached for up to 1800 seconds  --- Requires one of the following EVE corporation role(s): Station_Manager 

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
api_instance = eve_swagger_api.IndustryApi(eve_swagger_api.ApiClient(configuration))
corporation_id = 56 # int | An EVE corporation ID
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
page = 1 # int | Which page of results to return (optional) (default to 1)
token = 'token_example' # str | Access token to use if unable to set a header (optional)

try:
    # Moon extraction timers
    api_response = api_instance.get_corporation_corporation_id_mining_extractions(corporation_id, datasource=datasource, if_none_match=if_none_match, page=page, token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndustryApi->get_corporation_corporation_id_mining_extractions: %s\n" % e)
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

[**list[GetCorporationCorporationIdMiningExtractions200Ok]**](GetCorporationCorporationIdMiningExtractions200Ok.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_corporation_corporation_id_mining_observers**
> list[GetCorporationCorporationIdMiningObservers200Ok] get_corporation_corporation_id_mining_observers(corporation_id, datasource=datasource, if_none_match=if_none_match, page=page, token=token)

Corporation mining observers

Paginated list of all entities capable of observing and recording mining for a corporation   --- Alternate route: `/dev/corporation/{corporation_id}/mining/observers/`  Alternate route: `/legacy/corporation/{corporation_id}/mining/observers/`  Alternate route: `/v1/corporation/{corporation_id}/mining/observers/`  --- This route is cached for up to 3600 seconds  --- Requires one of the following EVE corporation role(s): Accountant 

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
api_instance = eve_swagger_api.IndustryApi(eve_swagger_api.ApiClient(configuration))
corporation_id = 56 # int | An EVE corporation ID
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
page = 1 # int | Which page of results to return (optional) (default to 1)
token = 'token_example' # str | Access token to use if unable to set a header (optional)

try:
    # Corporation mining observers
    api_response = api_instance.get_corporation_corporation_id_mining_observers(corporation_id, datasource=datasource, if_none_match=if_none_match, page=page, token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndustryApi->get_corporation_corporation_id_mining_observers: %s\n" % e)
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

[**list[GetCorporationCorporationIdMiningObservers200Ok]**](GetCorporationCorporationIdMiningObservers200Ok.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_corporation_corporation_id_mining_observers_observer_id**
> list[GetCorporationCorporationIdMiningObserversObserverId200Ok] get_corporation_corporation_id_mining_observers_observer_id(corporation_id, observer_id, datasource=datasource, if_none_match=if_none_match, page=page, token=token)

Observed corporation mining

Paginated record of all mining seen by an observer   --- Alternate route: `/dev/corporation/{corporation_id}/mining/observers/{observer_id}/`  Alternate route: `/legacy/corporation/{corporation_id}/mining/observers/{observer_id}/`  Alternate route: `/v1/corporation/{corporation_id}/mining/observers/{observer_id}/`  --- This route is cached for up to 3600 seconds  --- Requires one of the following EVE corporation role(s): Accountant 

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
api_instance = eve_swagger_api.IndustryApi(eve_swagger_api.ApiClient(configuration))
corporation_id = 56 # int | An EVE corporation ID
observer_id = 789 # int | A mining observer id
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
page = 1 # int | Which page of results to return (optional) (default to 1)
token = 'token_example' # str | Access token to use if unable to set a header (optional)

try:
    # Observed corporation mining
    api_response = api_instance.get_corporation_corporation_id_mining_observers_observer_id(corporation_id, observer_id, datasource=datasource, if_none_match=if_none_match, page=page, token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndustryApi->get_corporation_corporation_id_mining_observers_observer_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corporation_id** | **int**| An EVE corporation ID | 
 **observer_id** | **int**| A mining observer id | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to tranquility]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **page** | **int**| Which page of results to return | [optional] [default to 1]
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

[**list[GetCorporationCorporationIdMiningObserversObserverId200Ok]**](GetCorporationCorporationIdMiningObserversObserverId200Ok.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_corporations_corporation_id_industry_jobs**
> list[GetCorporationsCorporationIdIndustryJobs200Ok] get_corporations_corporation_id_industry_jobs(corporation_id, datasource=datasource, if_none_match=if_none_match, include_completed=include_completed, page=page, token=token)

List corporation industry jobs

List industry jobs run by a corporation  --- Alternate route: `/dev/corporations/{corporation_id}/industry/jobs/`  Alternate route: `/legacy/corporations/{corporation_id}/industry/jobs/`  Alternate route: `/v1/corporations/{corporation_id}/industry/jobs/`  --- This route is cached for up to 300 seconds  --- Requires one of the following EVE corporation role(s): Factory_Manager 

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
api_instance = eve_swagger_api.IndustryApi(eve_swagger_api.ApiClient(configuration))
corporation_id = 56 # int | An EVE corporation ID
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
include_completed = false # bool | Whether to retrieve completed corporation industry jobs. Only includes jobs from the past 90 days (optional) (default to false)
page = 1 # int | Which page of results to return (optional) (default to 1)
token = 'token_example' # str | Access token to use if unable to set a header (optional)

try:
    # List corporation industry jobs
    api_response = api_instance.get_corporations_corporation_id_industry_jobs(corporation_id, datasource=datasource, if_none_match=if_none_match, include_completed=include_completed, page=page, token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndustryApi->get_corporations_corporation_id_industry_jobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corporation_id** | **int**| An EVE corporation ID | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to tranquility]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **include_completed** | **bool**| Whether to retrieve completed corporation industry jobs. Only includes jobs from the past 90 days | [optional] [default to false]
 **page** | **int**| Which page of results to return | [optional] [default to 1]
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

[**list[GetCorporationsCorporationIdIndustryJobs200Ok]**](GetCorporationsCorporationIdIndustryJobs200Ok.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_industry_facilities**
> list[GetIndustryFacilities200Ok] get_industry_facilities(datasource=datasource, if_none_match=if_none_match)

List industry facilities

Return a list of industry facilities  --- Alternate route: `/dev/industry/facilities/`  Alternate route: `/legacy/industry/facilities/`  Alternate route: `/v1/industry/facilities/`  --- This route is cached for up to 3600 seconds

### Example
```python
from __future__ import print_function
import time
import eve_swagger_api
from eve_swagger_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = eve_swagger_api.IndustryApi()
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)

try:
    # List industry facilities
    api_response = api_instance.get_industry_facilities(datasource=datasource, if_none_match=if_none_match)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndustryApi->get_industry_facilities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datasource** | **str**| The server name you would like data from | [optional] [default to tranquility]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 

### Return type

[**list[GetIndustryFacilities200Ok]**](GetIndustryFacilities200Ok.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_industry_systems**
> list[GetIndustrySystems200Ok] get_industry_systems(datasource=datasource, if_none_match=if_none_match)

List solar system cost indices

Return cost indices for solar systems  --- Alternate route: `/dev/industry/systems/`  Alternate route: `/legacy/industry/systems/`  Alternate route: `/v1/industry/systems/`  --- This route is cached for up to 3600 seconds

### Example
```python
from __future__ import print_function
import time
import eve_swagger_api
from eve_swagger_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = eve_swagger_api.IndustryApi()
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)

try:
    # List solar system cost indices
    api_response = api_instance.get_industry_systems(datasource=datasource, if_none_match=if_none_match)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndustryApi->get_industry_systems: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datasource** | **str**| The server name you would like data from | [optional] [default to tranquility]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 

### Return type

[**list[GetIndustrySystems200Ok]**](GetIndustrySystems200Ok.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

