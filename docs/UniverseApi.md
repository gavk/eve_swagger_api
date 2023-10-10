# eve_swagger_api.UniverseApi

All URIs are relative to *https://esi.evetech.net/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_universe_ancestries**](UniverseApi.md#get_universe_ancestries) | **GET** /universe/ancestries/ | Get ancestries
[**get_universe_asteroid_belts_asteroid_belt_id**](UniverseApi.md#get_universe_asteroid_belts_asteroid_belt_id) | **GET** /universe/asteroid_belts/{asteroid_belt_id}/ | Get asteroid belt information
[**get_universe_bloodlines**](UniverseApi.md#get_universe_bloodlines) | **GET** /universe/bloodlines/ | Get bloodlines
[**get_universe_categories**](UniverseApi.md#get_universe_categories) | **GET** /universe/categories/ | Get item categories
[**get_universe_categories_category_id**](UniverseApi.md#get_universe_categories_category_id) | **GET** /universe/categories/{category_id}/ | Get item category information
[**get_universe_constellations**](UniverseApi.md#get_universe_constellations) | **GET** /universe/constellations/ | Get constellations
[**get_universe_constellations_constellation_id**](UniverseApi.md#get_universe_constellations_constellation_id) | **GET** /universe/constellations/{constellation_id}/ | Get constellation information
[**get_universe_factions**](UniverseApi.md#get_universe_factions) | **GET** /universe/factions/ | Get factions
[**get_universe_graphics**](UniverseApi.md#get_universe_graphics) | **GET** /universe/graphics/ | Get graphics
[**get_universe_graphics_graphic_id**](UniverseApi.md#get_universe_graphics_graphic_id) | **GET** /universe/graphics/{graphic_id}/ | Get graphic information
[**get_universe_groups**](UniverseApi.md#get_universe_groups) | **GET** /universe/groups/ | Get item groups
[**get_universe_groups_group_id**](UniverseApi.md#get_universe_groups_group_id) | **GET** /universe/groups/{group_id}/ | Get item group information
[**get_universe_moons_moon_id**](UniverseApi.md#get_universe_moons_moon_id) | **GET** /universe/moons/{moon_id}/ | Get moon information
[**get_universe_planets_planet_id**](UniverseApi.md#get_universe_planets_planet_id) | **GET** /universe/planets/{planet_id}/ | Get planet information
[**get_universe_races**](UniverseApi.md#get_universe_races) | **GET** /universe/races/ | Get character races
[**get_universe_regions**](UniverseApi.md#get_universe_regions) | **GET** /universe/regions/ | Get regions
[**get_universe_regions_region_id**](UniverseApi.md#get_universe_regions_region_id) | **GET** /universe/regions/{region_id}/ | Get region information
[**get_universe_stargates_stargate_id**](UniverseApi.md#get_universe_stargates_stargate_id) | **GET** /universe/stargates/{stargate_id}/ | Get stargate information
[**get_universe_stars_star_id**](UniverseApi.md#get_universe_stars_star_id) | **GET** /universe/stars/{star_id}/ | Get star information
[**get_universe_stations_station_id**](UniverseApi.md#get_universe_stations_station_id) | **GET** /universe/stations/{station_id}/ | Get station information
[**get_universe_structures**](UniverseApi.md#get_universe_structures) | **GET** /universe/structures/ | List all public structures
[**get_universe_structures_structure_id**](UniverseApi.md#get_universe_structures_structure_id) | **GET** /universe/structures/{structure_id}/ | Get structure information
[**get_universe_system_jumps**](UniverseApi.md#get_universe_system_jumps) | **GET** /universe/system_jumps/ | Get system jumps
[**get_universe_system_kills**](UniverseApi.md#get_universe_system_kills) | **GET** /universe/system_kills/ | Get system kills
[**get_universe_systems**](UniverseApi.md#get_universe_systems) | **GET** /universe/systems/ | Get solar systems
[**get_universe_systems_system_id**](UniverseApi.md#get_universe_systems_system_id) | **GET** /universe/systems/{system_id}/ | Get solar system information
[**get_universe_types**](UniverseApi.md#get_universe_types) | **GET** /universe/types/ | Get types
[**get_universe_types_type_id**](UniverseApi.md#get_universe_types_type_id) | **GET** /universe/types/{type_id}/ | Get type information
[**post_universe_ids**](UniverseApi.md#post_universe_ids) | **POST** /universe/ids/ | Bulk names to IDs
[**post_universe_names**](UniverseApi.md#post_universe_names) | **POST** /universe/names/ | Get names and categories for a set of IDs


# **get_universe_ancestries**
> list[GetUniverseAncestries200Ok] get_universe_ancestries(accept_language=accept_language, datasource=datasource, if_none_match=if_none_match, language=language)

Get ancestries

Get all character ancestries  --- Alternate route: `/legacy/universe/ancestries/`  Alternate route: `/v1/universe/ancestries/`  --- This route expires daily at 11:05

### Example
```python
from __future__ import print_function
import time
import eve_swagger_api
from eve_swagger_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = eve_swagger_api.UniverseApi()
accept_language = 'en' # str | Language to use in the response (optional) (default to en)
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
language = 'en' # str | Language to use in the response, takes precedence over Accept-Language (optional) (default to en)

try:
    # Get ancestries
    api_response = api_instance.get_universe_ancestries(accept_language=accept_language, datasource=datasource, if_none_match=if_none_match, language=language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UniverseApi->get_universe_ancestries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language to use in the response | [optional] [default to en]
 **datasource** | **str**| The server name you would like data from | [optional] [default to tranquility]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **language** | **str**| Language to use in the response, takes precedence over Accept-Language | [optional] [default to en]

### Return type

[**list[GetUniverseAncestries200Ok]**](GetUniverseAncestries200Ok.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_universe_asteroid_belts_asteroid_belt_id**
> GetUniverseAsteroidBeltsAsteroidBeltIdOk get_universe_asteroid_belts_asteroid_belt_id(asteroid_belt_id, datasource=datasource, if_none_match=if_none_match)

Get asteroid belt information

Get information on an asteroid belt  --- Alternate route: `/legacy/universe/asteroid_belts/{asteroid_belt_id}/`  Alternate route: `/v1/universe/asteroid_belts/{asteroid_belt_id}/`  --- This route expires daily at 11:05

### Example
```python
from __future__ import print_function
import time
import eve_swagger_api
from eve_swagger_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = eve_swagger_api.UniverseApi()
asteroid_belt_id = 56 # int | asteroid_belt_id integer
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)

try:
    # Get asteroid belt information
    api_response = api_instance.get_universe_asteroid_belts_asteroid_belt_id(asteroid_belt_id, datasource=datasource, if_none_match=if_none_match)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UniverseApi->get_universe_asteroid_belts_asteroid_belt_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asteroid_belt_id** | **int**| asteroid_belt_id integer | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to tranquility]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 

### Return type

[**GetUniverseAsteroidBeltsAsteroidBeltIdOk**](GetUniverseAsteroidBeltsAsteroidBeltIdOk.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_universe_bloodlines**
> list[GetUniverseBloodlines200Ok] get_universe_bloodlines(accept_language=accept_language, datasource=datasource, if_none_match=if_none_match, language=language)

Get bloodlines

Get a list of bloodlines  --- Alternate route: `/legacy/universe/bloodlines/`  Alternate route: `/v1/universe/bloodlines/`  --- This route expires daily at 11:05

### Example
```python
from __future__ import print_function
import time
import eve_swagger_api
from eve_swagger_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = eve_swagger_api.UniverseApi()
accept_language = 'en' # str | Language to use in the response (optional) (default to en)
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
language = 'en' # str | Language to use in the response, takes precedence over Accept-Language (optional) (default to en)

try:
    # Get bloodlines
    api_response = api_instance.get_universe_bloodlines(accept_language=accept_language, datasource=datasource, if_none_match=if_none_match, language=language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UniverseApi->get_universe_bloodlines: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language to use in the response | [optional] [default to en]
 **datasource** | **str**| The server name you would like data from | [optional] [default to tranquility]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **language** | **str**| Language to use in the response, takes precedence over Accept-Language | [optional] [default to en]

### Return type

[**list[GetUniverseBloodlines200Ok]**](GetUniverseBloodlines200Ok.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_universe_categories**
> list[int] get_universe_categories(datasource=datasource, if_none_match=if_none_match)

Get item categories

Get a list of item categories  --- Alternate route: `/legacy/universe/categories/`  Alternate route: `/v1/universe/categories/`  --- This route expires daily at 11:05

### Example
```python
from __future__ import print_function
import time
import eve_swagger_api
from eve_swagger_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = eve_swagger_api.UniverseApi()
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)

try:
    # Get item categories
    api_response = api_instance.get_universe_categories(datasource=datasource, if_none_match=if_none_match)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UniverseApi->get_universe_categories: %s\n" % e)
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

# **get_universe_categories_category_id**
> GetUniverseCategoriesCategoryIdOk get_universe_categories_category_id(category_id, accept_language=accept_language, datasource=datasource, if_none_match=if_none_match, language=language)

Get item category information

Get information of an item category  --- Alternate route: `/legacy/universe/categories/{category_id}/`  Alternate route: `/v1/universe/categories/{category_id}/`  --- This route expires daily at 11:05

### Example
```python
from __future__ import print_function
import time
import eve_swagger_api
from eve_swagger_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = eve_swagger_api.UniverseApi()
category_id = 56 # int | An Eve item category ID
accept_language = 'en' # str | Language to use in the response (optional) (default to en)
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
language = 'en' # str | Language to use in the response, takes precedence over Accept-Language (optional) (default to en)

try:
    # Get item category information
    api_response = api_instance.get_universe_categories_category_id(category_id, accept_language=accept_language, datasource=datasource, if_none_match=if_none_match, language=language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UniverseApi->get_universe_categories_category_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **int**| An Eve item category ID | 
 **accept_language** | **str**| Language to use in the response | [optional] [default to en]
 **datasource** | **str**| The server name you would like data from | [optional] [default to tranquility]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **language** | **str**| Language to use in the response, takes precedence over Accept-Language | [optional] [default to en]

### Return type

[**GetUniverseCategoriesCategoryIdOk**](GetUniverseCategoriesCategoryIdOk.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_universe_constellations**
> list[int] get_universe_constellations(datasource=datasource, if_none_match=if_none_match)

Get constellations

Get a list of constellations  --- Alternate route: `/legacy/universe/constellations/`  Alternate route: `/v1/universe/constellations/`  --- This route expires daily at 11:05

### Example
```python
from __future__ import print_function
import time
import eve_swagger_api
from eve_swagger_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = eve_swagger_api.UniverseApi()
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)

try:
    # Get constellations
    api_response = api_instance.get_universe_constellations(datasource=datasource, if_none_match=if_none_match)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UniverseApi->get_universe_constellations: %s\n" % e)
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

# **get_universe_constellations_constellation_id**
> GetUniverseConstellationsConstellationIdOk get_universe_constellations_constellation_id(constellation_id, accept_language=accept_language, datasource=datasource, if_none_match=if_none_match, language=language)

Get constellation information

Get information on a constellation  --- Alternate route: `/legacy/universe/constellations/{constellation_id}/`  Alternate route: `/v1/universe/constellations/{constellation_id}/`  --- This route expires daily at 11:05

### Example
```python
from __future__ import print_function
import time
import eve_swagger_api
from eve_swagger_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = eve_swagger_api.UniverseApi()
constellation_id = 56 # int | constellation_id integer
accept_language = 'en' # str | Language to use in the response (optional) (default to en)
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
language = 'en' # str | Language to use in the response, takes precedence over Accept-Language (optional) (default to en)

try:
    # Get constellation information
    api_response = api_instance.get_universe_constellations_constellation_id(constellation_id, accept_language=accept_language, datasource=datasource, if_none_match=if_none_match, language=language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UniverseApi->get_universe_constellations_constellation_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **constellation_id** | **int**| constellation_id integer | 
 **accept_language** | **str**| Language to use in the response | [optional] [default to en]
 **datasource** | **str**| The server name you would like data from | [optional] [default to tranquility]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **language** | **str**| Language to use in the response, takes precedence over Accept-Language | [optional] [default to en]

### Return type

[**GetUniverseConstellationsConstellationIdOk**](GetUniverseConstellationsConstellationIdOk.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_universe_factions**
> list[GetUniverseFactions200Ok] get_universe_factions(accept_language=accept_language, datasource=datasource, if_none_match=if_none_match, language=language)

Get factions

Get a list of factions  --- Alternate route: `/dev/universe/factions/`  Alternate route: `/v2/universe/factions/`  --- This route expires daily at 11:05

### Example
```python
from __future__ import print_function
import time
import eve_swagger_api
from eve_swagger_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = eve_swagger_api.UniverseApi()
accept_language = 'en' # str | Language to use in the response (optional) (default to en)
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
language = 'en' # str | Language to use in the response, takes precedence over Accept-Language (optional) (default to en)

try:
    # Get factions
    api_response = api_instance.get_universe_factions(accept_language=accept_language, datasource=datasource, if_none_match=if_none_match, language=language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UniverseApi->get_universe_factions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language to use in the response | [optional] [default to en]
 **datasource** | **str**| The server name you would like data from | [optional] [default to tranquility]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **language** | **str**| Language to use in the response, takes precedence over Accept-Language | [optional] [default to en]

### Return type

[**list[GetUniverseFactions200Ok]**](GetUniverseFactions200Ok.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_universe_graphics**
> list[int] get_universe_graphics(datasource=datasource, if_none_match=if_none_match)

Get graphics

Get a list of graphics  --- Alternate route: `/legacy/universe/graphics/`  Alternate route: `/v1/universe/graphics/`  --- This route expires daily at 11:05

### Example
```python
from __future__ import print_function
import time
import eve_swagger_api
from eve_swagger_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = eve_swagger_api.UniverseApi()
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)

try:
    # Get graphics
    api_response = api_instance.get_universe_graphics(datasource=datasource, if_none_match=if_none_match)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UniverseApi->get_universe_graphics: %s\n" % e)
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

# **get_universe_graphics_graphic_id**
> GetUniverseGraphicsGraphicIdOk get_universe_graphics_graphic_id(graphic_id, datasource=datasource, if_none_match=if_none_match)

Get graphic information

Get information on a graphic  --- Alternate route: `/dev/universe/graphics/{graphic_id}/`  Alternate route: `/legacy/universe/graphics/{graphic_id}/`  Alternate route: `/v1/universe/graphics/{graphic_id}/`  --- This route expires daily at 11:05

### Example
```python
from __future__ import print_function
import time
import eve_swagger_api
from eve_swagger_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = eve_swagger_api.UniverseApi()
graphic_id = 56 # int | graphic_id integer
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)

try:
    # Get graphic information
    api_response = api_instance.get_universe_graphics_graphic_id(graphic_id, datasource=datasource, if_none_match=if_none_match)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UniverseApi->get_universe_graphics_graphic_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **graphic_id** | **int**| graphic_id integer | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to tranquility]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 

### Return type

[**GetUniverseGraphicsGraphicIdOk**](GetUniverseGraphicsGraphicIdOk.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_universe_groups**
> list[int] get_universe_groups(datasource=datasource, if_none_match=if_none_match, page=page)

Get item groups

Get a list of item groups  --- Alternate route: `/legacy/universe/groups/`  Alternate route: `/v1/universe/groups/`  --- This route expires daily at 11:05

### Example
```python
from __future__ import print_function
import time
import eve_swagger_api
from eve_swagger_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = eve_swagger_api.UniverseApi()
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
page = 1 # int | Which page of results to return (optional) (default to 1)

try:
    # Get item groups
    api_response = api_instance.get_universe_groups(datasource=datasource, if_none_match=if_none_match, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UniverseApi->get_universe_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datasource** | **str**| The server name you would like data from | [optional] [default to tranquility]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **page** | **int**| Which page of results to return | [optional] [default to 1]

### Return type

**list[int]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_universe_groups_group_id**
> GetUniverseGroupsGroupIdOk get_universe_groups_group_id(group_id, accept_language=accept_language, datasource=datasource, if_none_match=if_none_match, language=language)

Get item group information

Get information on an item group  --- Alternate route: `/dev/universe/groups/{group_id}/`  Alternate route: `/legacy/universe/groups/{group_id}/`  Alternate route: `/v1/universe/groups/{group_id}/`  --- This route expires daily at 11:05

### Example
```python
from __future__ import print_function
import time
import eve_swagger_api
from eve_swagger_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = eve_swagger_api.UniverseApi()
group_id = 56 # int | An Eve item group ID
accept_language = 'en' # str | Language to use in the response (optional) (default to en)
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
language = 'en' # str | Language to use in the response, takes precedence over Accept-Language (optional) (default to en)

try:
    # Get item group information
    api_response = api_instance.get_universe_groups_group_id(group_id, accept_language=accept_language, datasource=datasource, if_none_match=if_none_match, language=language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UniverseApi->get_universe_groups_group_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| An Eve item group ID | 
 **accept_language** | **str**| Language to use in the response | [optional] [default to en]
 **datasource** | **str**| The server name you would like data from | [optional] [default to tranquility]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **language** | **str**| Language to use in the response, takes precedence over Accept-Language | [optional] [default to en]

### Return type

[**GetUniverseGroupsGroupIdOk**](GetUniverseGroupsGroupIdOk.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_universe_moons_moon_id**
> GetUniverseMoonsMoonIdOk get_universe_moons_moon_id(moon_id, datasource=datasource, if_none_match=if_none_match)

Get moon information

Get information on a moon  --- Alternate route: `/legacy/universe/moons/{moon_id}/`  Alternate route: `/v1/universe/moons/{moon_id}/`  --- This route expires daily at 11:05

### Example
```python
from __future__ import print_function
import time
import eve_swagger_api
from eve_swagger_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = eve_swagger_api.UniverseApi()
moon_id = 56 # int | moon_id integer
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)

try:
    # Get moon information
    api_response = api_instance.get_universe_moons_moon_id(moon_id, datasource=datasource, if_none_match=if_none_match)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UniverseApi->get_universe_moons_moon_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moon_id** | **int**| moon_id integer | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to tranquility]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 

### Return type

[**GetUniverseMoonsMoonIdOk**](GetUniverseMoonsMoonIdOk.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_universe_planets_planet_id**
> GetUniversePlanetsPlanetIdOk get_universe_planets_planet_id(planet_id, datasource=datasource, if_none_match=if_none_match)

Get planet information

Get information on a planet  --- Alternate route: `/legacy/universe/planets/{planet_id}/`  Alternate route: `/v1/universe/planets/{planet_id}/`  --- This route expires daily at 11:05

### Example
```python
from __future__ import print_function
import time
import eve_swagger_api
from eve_swagger_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = eve_swagger_api.UniverseApi()
planet_id = 56 # int | planet_id integer
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)

try:
    # Get planet information
    api_response = api_instance.get_universe_planets_planet_id(planet_id, datasource=datasource, if_none_match=if_none_match)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UniverseApi->get_universe_planets_planet_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **planet_id** | **int**| planet_id integer | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to tranquility]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 

### Return type

[**GetUniversePlanetsPlanetIdOk**](GetUniversePlanetsPlanetIdOk.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_universe_races**
> list[GetUniverseRaces200Ok] get_universe_races(accept_language=accept_language, datasource=datasource, if_none_match=if_none_match, language=language)

Get character races

Get a list of character races  --- Alternate route: `/dev/universe/races/`  Alternate route: `/legacy/universe/races/`  Alternate route: `/v1/universe/races/`  --- This route expires daily at 11:05

### Example
```python
from __future__ import print_function
import time
import eve_swagger_api
from eve_swagger_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = eve_swagger_api.UniverseApi()
accept_language = 'en' # str | Language to use in the response (optional) (default to en)
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
language = 'en' # str | Language to use in the response, takes precedence over Accept-Language (optional) (default to en)

try:
    # Get character races
    api_response = api_instance.get_universe_races(accept_language=accept_language, datasource=datasource, if_none_match=if_none_match, language=language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UniverseApi->get_universe_races: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language to use in the response | [optional] [default to en]
 **datasource** | **str**| The server name you would like data from | [optional] [default to tranquility]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **language** | **str**| Language to use in the response, takes precedence over Accept-Language | [optional] [default to en]

### Return type

[**list[GetUniverseRaces200Ok]**](GetUniverseRaces200Ok.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_universe_regions**
> list[int] get_universe_regions(datasource=datasource, if_none_match=if_none_match)

Get regions

Get a list of regions  --- Alternate route: `/legacy/universe/regions/`  Alternate route: `/v1/universe/regions/`  --- This route expires daily at 11:05

### Example
```python
from __future__ import print_function
import time
import eve_swagger_api
from eve_swagger_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = eve_swagger_api.UniverseApi()
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)

try:
    # Get regions
    api_response = api_instance.get_universe_regions(datasource=datasource, if_none_match=if_none_match)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UniverseApi->get_universe_regions: %s\n" % e)
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

# **get_universe_regions_region_id**
> GetUniverseRegionsRegionIdOk get_universe_regions_region_id(region_id, accept_language=accept_language, datasource=datasource, if_none_match=if_none_match, language=language)

Get region information

Get information on a region  --- Alternate route: `/legacy/universe/regions/{region_id}/`  Alternate route: `/v1/universe/regions/{region_id}/`  --- This route expires daily at 11:05

### Example
```python
from __future__ import print_function
import time
import eve_swagger_api
from eve_swagger_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = eve_swagger_api.UniverseApi()
region_id = 56 # int | region_id integer
accept_language = 'en' # str | Language to use in the response (optional) (default to en)
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
language = 'en' # str | Language to use in the response, takes precedence over Accept-Language (optional) (default to en)

try:
    # Get region information
    api_response = api_instance.get_universe_regions_region_id(region_id, accept_language=accept_language, datasource=datasource, if_none_match=if_none_match, language=language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UniverseApi->get_universe_regions_region_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **int**| region_id integer | 
 **accept_language** | **str**| Language to use in the response | [optional] [default to en]
 **datasource** | **str**| The server name you would like data from | [optional] [default to tranquility]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **language** | **str**| Language to use in the response, takes precedence over Accept-Language | [optional] [default to en]

### Return type

[**GetUniverseRegionsRegionIdOk**](GetUniverseRegionsRegionIdOk.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_universe_stargates_stargate_id**
> GetUniverseStargatesStargateIdOk get_universe_stargates_stargate_id(stargate_id, datasource=datasource, if_none_match=if_none_match)

Get stargate information

Get information on a stargate  --- Alternate route: `/legacy/universe/stargates/{stargate_id}/`  Alternate route: `/v1/universe/stargates/{stargate_id}/`  --- This route expires daily at 11:05

### Example
```python
from __future__ import print_function
import time
import eve_swagger_api
from eve_swagger_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = eve_swagger_api.UniverseApi()
stargate_id = 56 # int | stargate_id integer
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)

try:
    # Get stargate information
    api_response = api_instance.get_universe_stargates_stargate_id(stargate_id, datasource=datasource, if_none_match=if_none_match)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UniverseApi->get_universe_stargates_stargate_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stargate_id** | **int**| stargate_id integer | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to tranquility]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 

### Return type

[**GetUniverseStargatesStargateIdOk**](GetUniverseStargatesStargateIdOk.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_universe_stars_star_id**
> GetUniverseStarsStarIdOk get_universe_stars_star_id(star_id, datasource=datasource, if_none_match=if_none_match)

Get star information

Get information on a star  --- Alternate route: `/legacy/universe/stars/{star_id}/`  Alternate route: `/v1/universe/stars/{star_id}/`  --- This route expires daily at 11:05

### Example
```python
from __future__ import print_function
import time
import eve_swagger_api
from eve_swagger_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = eve_swagger_api.UniverseApi()
star_id = 56 # int | star_id integer
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)

try:
    # Get star information
    api_response = api_instance.get_universe_stars_star_id(star_id, datasource=datasource, if_none_match=if_none_match)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UniverseApi->get_universe_stars_star_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **star_id** | **int**| star_id integer | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to tranquility]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 

### Return type

[**GetUniverseStarsStarIdOk**](GetUniverseStarsStarIdOk.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_universe_stations_station_id**
> GetUniverseStationsStationIdOk get_universe_stations_station_id(station_id, datasource=datasource, if_none_match=if_none_match)

Get station information

Get information on a station  --- Alternate route: `/dev/universe/stations/{station_id}/`  Alternate route: `/v2/universe/stations/{station_id}/`  --- This route expires daily at 11:05

### Example
```python
from __future__ import print_function
import time
import eve_swagger_api
from eve_swagger_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = eve_swagger_api.UniverseApi()
station_id = 56 # int | station_id integer
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)

try:
    # Get station information
    api_response = api_instance.get_universe_stations_station_id(station_id, datasource=datasource, if_none_match=if_none_match)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UniverseApi->get_universe_stations_station_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **station_id** | **int**| station_id integer | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to tranquility]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 

### Return type

[**GetUniverseStationsStationIdOk**](GetUniverseStationsStationIdOk.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_universe_structures**
> list[int] get_universe_structures(datasource=datasource, filter=filter, if_none_match=if_none_match)

List all public structures

List all public structures  --- Alternate route: `/dev/universe/structures/`  Alternate route: `/legacy/universe/structures/`  Alternate route: `/v1/universe/structures/`  --- This route is cached for up to 3600 seconds

### Example
```python
from __future__ import print_function
import time
import eve_swagger_api
from eve_swagger_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = eve_swagger_api.UniverseApi()
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
filter = 'filter_example' # str | Only list public structures that have this service online (optional)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)

try:
    # List all public structures
    api_response = api_instance.get_universe_structures(datasource=datasource, filter=filter, if_none_match=if_none_match)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UniverseApi->get_universe_structures: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datasource** | **str**| The server name you would like data from | [optional] [default to tranquility]
 **filter** | **str**| Only list public structures that have this service online | [optional] 
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 

### Return type

**list[int]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_universe_structures_structure_id**
> GetUniverseStructuresStructureIdOk get_universe_structures_structure_id(structure_id, datasource=datasource, if_none_match=if_none_match, token=token)

Get structure information

Returns information on requested structure if you are on the ACL. Otherwise, returns \"Forbidden\" for all inputs.  --- Alternate route: `/v2/universe/structures/{structure_id}/`  --- This route is cached for up to 3600 seconds

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
api_instance = eve_swagger_api.UniverseApi(eve_swagger_api.ApiClient(configuration))
structure_id = 789 # int | An Eve structure ID
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
token = 'token_example' # str | Access token to use if unable to set a header (optional)

try:
    # Get structure information
    api_response = api_instance.get_universe_structures_structure_id(structure_id, datasource=datasource, if_none_match=if_none_match, token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UniverseApi->get_universe_structures_structure_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **structure_id** | **int**| An Eve structure ID | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to tranquility]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

[**GetUniverseStructuresStructureIdOk**](GetUniverseStructuresStructureIdOk.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_universe_system_jumps**
> list[GetUniverseSystemJumps200Ok] get_universe_system_jumps(datasource=datasource, if_none_match=if_none_match)

Get system jumps

Get the number of jumps in solar systems within the last hour ending at the timestamp of the Last-Modified header, excluding wormhole space. Only systems with jumps will be listed  --- Alternate route: `/legacy/universe/system_jumps/`  Alternate route: `/v1/universe/system_jumps/`  --- This route is cached for up to 3600 seconds

### Example
```python
from __future__ import print_function
import time
import eve_swagger_api
from eve_swagger_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = eve_swagger_api.UniverseApi()
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)

try:
    # Get system jumps
    api_response = api_instance.get_universe_system_jumps(datasource=datasource, if_none_match=if_none_match)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UniverseApi->get_universe_system_jumps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datasource** | **str**| The server name you would like data from | [optional] [default to tranquility]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 

### Return type

[**list[GetUniverseSystemJumps200Ok]**](GetUniverseSystemJumps200Ok.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_universe_system_kills**
> list[GetUniverseSystemKills200Ok] get_universe_system_kills(datasource=datasource, if_none_match=if_none_match)

Get system kills

Get the number of ship, pod and NPC kills per solar system within the last hour ending at the timestamp of the Last-Modified header, excluding wormhole space. Only systems with kills will be listed  --- Alternate route: `/v2/universe/system_kills/`  --- This route is cached for up to 3600 seconds

### Example
```python
from __future__ import print_function
import time
import eve_swagger_api
from eve_swagger_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = eve_swagger_api.UniverseApi()
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)

try:
    # Get system kills
    api_response = api_instance.get_universe_system_kills(datasource=datasource, if_none_match=if_none_match)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UniverseApi->get_universe_system_kills: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datasource** | **str**| The server name you would like data from | [optional] [default to tranquility]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 

### Return type

[**list[GetUniverseSystemKills200Ok]**](GetUniverseSystemKills200Ok.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_universe_systems**
> list[int] get_universe_systems(datasource=datasource, if_none_match=if_none_match)

Get solar systems

Get a list of solar systems  --- Alternate route: `/dev/universe/systems/`  Alternate route: `/legacy/universe/systems/`  Alternate route: `/v1/universe/systems/`  --- This route expires daily at 11:05

### Example
```python
from __future__ import print_function
import time
import eve_swagger_api
from eve_swagger_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = eve_swagger_api.UniverseApi()
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)

try:
    # Get solar systems
    api_response = api_instance.get_universe_systems(datasource=datasource, if_none_match=if_none_match)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UniverseApi->get_universe_systems: %s\n" % e)
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

# **get_universe_systems_system_id**
> GetUniverseSystemsSystemIdOk get_universe_systems_system_id(system_id, accept_language=accept_language, datasource=datasource, if_none_match=if_none_match, language=language)

Get solar system information

Get information on a solar system.  --- Alternate route: `/dev/universe/systems/{system_id}/`  Alternate route: `/v4/universe/systems/{system_id}/`  --- This route expires daily at 11:05

### Example
```python
from __future__ import print_function
import time
import eve_swagger_api
from eve_swagger_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = eve_swagger_api.UniverseApi()
system_id = 56 # int | system_id integer
accept_language = 'en' # str | Language to use in the response (optional) (default to en)
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
language = 'en' # str | Language to use in the response, takes precedence over Accept-Language (optional) (default to en)

try:
    # Get solar system information
    api_response = api_instance.get_universe_systems_system_id(system_id, accept_language=accept_language, datasource=datasource, if_none_match=if_none_match, language=language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UniverseApi->get_universe_systems_system_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **int**| system_id integer | 
 **accept_language** | **str**| Language to use in the response | [optional] [default to en]
 **datasource** | **str**| The server name you would like data from | [optional] [default to tranquility]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **language** | **str**| Language to use in the response, takes precedence over Accept-Language | [optional] [default to en]

### Return type

[**GetUniverseSystemsSystemIdOk**](GetUniverseSystemsSystemIdOk.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_universe_types**
> list[int] get_universe_types(datasource=datasource, if_none_match=if_none_match, page=page)

Get types

Get a list of type ids  --- Alternate route: `/legacy/universe/types/`  Alternate route: `/v1/universe/types/`  --- This route expires daily at 11:05

### Example
```python
from __future__ import print_function
import time
import eve_swagger_api
from eve_swagger_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = eve_swagger_api.UniverseApi()
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
page = 1 # int | Which page of results to return (optional) (default to 1)

try:
    # Get types
    api_response = api_instance.get_universe_types(datasource=datasource, if_none_match=if_none_match, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UniverseApi->get_universe_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datasource** | **str**| The server name you would like data from | [optional] [default to tranquility]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **page** | **int**| Which page of results to return | [optional] [default to 1]

### Return type

**list[int]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_universe_types_type_id**
> GetUniverseTypesTypeIdOk get_universe_types_type_id(type_id, accept_language=accept_language, datasource=datasource, if_none_match=if_none_match, language=language)

Get type information

Get information on a type  --- Alternate route: `/dev/universe/types/{type_id}/`  Alternate route: `/v3/universe/types/{type_id}/`  --- This route expires daily at 11:05

### Example
```python
from __future__ import print_function
import time
import eve_swagger_api
from eve_swagger_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = eve_swagger_api.UniverseApi()
type_id = 56 # int | An Eve item type ID
accept_language = 'en' # str | Language to use in the response (optional) (default to en)
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
language = 'en' # str | Language to use in the response, takes precedence over Accept-Language (optional) (default to en)

try:
    # Get type information
    api_response = api_instance.get_universe_types_type_id(type_id, accept_language=accept_language, datasource=datasource, if_none_match=if_none_match, language=language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UniverseApi->get_universe_types_type_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type_id** | **int**| An Eve item type ID | 
 **accept_language** | **str**| Language to use in the response | [optional] [default to en]
 **datasource** | **str**| The server name you would like data from | [optional] [default to tranquility]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **language** | **str**| Language to use in the response, takes precedence over Accept-Language | [optional] [default to en]

### Return type

[**GetUniverseTypesTypeIdOk**](GetUniverseTypesTypeIdOk.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_universe_ids**
> PostUniverseIdsOk post_universe_ids(names, accept_language=accept_language, datasource=datasource, language=language)

Bulk names to IDs

Resolve a set of names to IDs in the following categories: agents, alliances, characters, constellations, corporations factions, inventory_types, regions, stations, and systems. Only exact matches will be returned. All names searched for are cached for 12 hours  --- Alternate route: `/dev/universe/ids/`  Alternate route: `/legacy/universe/ids/`  Alternate route: `/v1/universe/ids/` 

### Example
```python
from __future__ import print_function
import time
import eve_swagger_api
from eve_swagger_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = eve_swagger_api.UniverseApi()
names = [eve_swagger_api.list[str]()] # list[str] | The names to resolve
accept_language = 'en' # str | Language to use in the response (optional) (default to en)
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
language = 'en' # str | Language to use in the response, takes precedence over Accept-Language (optional) (default to en)

try:
    # Bulk names to IDs
    api_response = api_instance.post_universe_ids(names, accept_language=accept_language, datasource=datasource, language=language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UniverseApi->post_universe_ids: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **names** | **list[str]**| The names to resolve | 
 **accept_language** | **str**| Language to use in the response | [optional] [default to en]
 **datasource** | **str**| The server name you would like data from | [optional] [default to tranquility]
 **language** | **str**| Language to use in the response, takes precedence over Accept-Language | [optional] [default to en]

### Return type

[**PostUniverseIdsOk**](PostUniverseIdsOk.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_universe_names**
> list[PostUniverseNames200Ok] post_universe_names(ids, datasource=datasource)

Get names and categories for a set of IDs

Resolve a set of IDs to names and categories. Supported ID's for resolving are: Characters, Corporations, Alliances, Stations, Solar Systems, Constellations, Regions, Types, Factions  --- Alternate route: `/dev/universe/names/`  Alternate route: `/v3/universe/names/` 

### Example
```python
from __future__ import print_function
import time
import eve_swagger_api
from eve_swagger_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = eve_swagger_api.UniverseApi()
ids = [eve_swagger_api.list[int]()] # list[int] | The ids to resolve
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)

try:
    # Get names and categories for a set of IDs
    api_response = api_instance.post_universe_names(ids, datasource=datasource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UniverseApi->post_universe_names: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **list[int]**| The ids to resolve | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to tranquility]

### Return type

[**list[PostUniverseNames200Ok]**](PostUniverseNames200Ok.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

