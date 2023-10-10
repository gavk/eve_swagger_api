# eve_swagger_api.UserInterfaceApi

All URIs are relative to *https://esi.evetech.net/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_ui_autopilot_waypoint**](UserInterfaceApi.md#post_ui_autopilot_waypoint) | **POST** /ui/autopilot/waypoint/ | Set Autopilot Waypoint
[**post_ui_openwindow_contract**](UserInterfaceApi.md#post_ui_openwindow_contract) | **POST** /ui/openwindow/contract/ | Open Contract Window
[**post_ui_openwindow_information**](UserInterfaceApi.md#post_ui_openwindow_information) | **POST** /ui/openwindow/information/ | Open Information Window
[**post_ui_openwindow_marketdetails**](UserInterfaceApi.md#post_ui_openwindow_marketdetails) | **POST** /ui/openwindow/marketdetails/ | Open Market Details
[**post_ui_openwindow_newmail**](UserInterfaceApi.md#post_ui_openwindow_newmail) | **POST** /ui/openwindow/newmail/ | Open New Mail Window


# **post_ui_autopilot_waypoint**
> post_ui_autopilot_waypoint(add_to_beginning, clear_other_waypoints, destination_id, datasource=datasource, token=token)

Set Autopilot Waypoint

Set a solar system as autopilot waypoint  --- Alternate route: `/dev/ui/autopilot/waypoint/`  Alternate route: `/legacy/ui/autopilot/waypoint/`  Alternate route: `/v2/ui/autopilot/waypoint/` 

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
api_instance = eve_swagger_api.UserInterfaceApi(eve_swagger_api.ApiClient(configuration))
add_to_beginning = false # bool | Whether this solar system should be added to the beginning of all waypoints (default to false)
clear_other_waypoints = false # bool | Whether clean other waypoints beforing adding this one (default to false)
destination_id = 789 # int | The destination to travel to, can be solar system, station or structure's id
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
token = 'token_example' # str | Access token to use if unable to set a header (optional)

try:
    # Set Autopilot Waypoint
    api_instance.post_ui_autopilot_waypoint(add_to_beginning, clear_other_waypoints, destination_id, datasource=datasource, token=token)
except ApiException as e:
    print("Exception when calling UserInterfaceApi->post_ui_autopilot_waypoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_to_beginning** | **bool**| Whether this solar system should be added to the beginning of all waypoints | [default to false]
 **clear_other_waypoints** | **bool**| Whether clean other waypoints beforing adding this one | [default to false]
 **destination_id** | **int**| The destination to travel to, can be solar system, station or structure&#39;s id | 
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

# **post_ui_openwindow_contract**
> post_ui_openwindow_contract(contract_id, datasource=datasource, token=token)

Open Contract Window

Open the contract window inside the client  --- Alternate route: `/dev/ui/openwindow/contract/`  Alternate route: `/legacy/ui/openwindow/contract/`  Alternate route: `/v1/ui/openwindow/contract/` 

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
api_instance = eve_swagger_api.UserInterfaceApi(eve_swagger_api.ApiClient(configuration))
contract_id = 56 # int | The contract to open
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
token = 'token_example' # str | Access token to use if unable to set a header (optional)

try:
    # Open Contract Window
    api_instance.post_ui_openwindow_contract(contract_id, datasource=datasource, token=token)
except ApiException as e:
    print("Exception when calling UserInterfaceApi->post_ui_openwindow_contract: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **int**| The contract to open | 
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

# **post_ui_openwindow_information**
> post_ui_openwindow_information(target_id, datasource=datasource, token=token)

Open Information Window

Open the information window for a character, corporation or alliance inside the client  --- Alternate route: `/dev/ui/openwindow/information/`  Alternate route: `/legacy/ui/openwindow/information/`  Alternate route: `/v1/ui/openwindow/information/` 

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
api_instance = eve_swagger_api.UserInterfaceApi(eve_swagger_api.ApiClient(configuration))
target_id = 56 # int | The target to open
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
token = 'token_example' # str | Access token to use if unable to set a header (optional)

try:
    # Open Information Window
    api_instance.post_ui_openwindow_information(target_id, datasource=datasource, token=token)
except ApiException as e:
    print("Exception when calling UserInterfaceApi->post_ui_openwindow_information: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_id** | **int**| The target to open | 
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

# **post_ui_openwindow_marketdetails**
> post_ui_openwindow_marketdetails(type_id, datasource=datasource, token=token)

Open Market Details

Open the market details window for a specific typeID inside the client  --- Alternate route: `/dev/ui/openwindow/marketdetails/`  Alternate route: `/legacy/ui/openwindow/marketdetails/`  Alternate route: `/v1/ui/openwindow/marketdetails/` 

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
api_instance = eve_swagger_api.UserInterfaceApi(eve_swagger_api.ApiClient(configuration))
type_id = 56 # int | The item type to open in market window
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
token = 'token_example' # str | Access token to use if unable to set a header (optional)

try:
    # Open Market Details
    api_instance.post_ui_openwindow_marketdetails(type_id, datasource=datasource, token=token)
except ApiException as e:
    print("Exception when calling UserInterfaceApi->post_ui_openwindow_marketdetails: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type_id** | **int**| The item type to open in market window | 
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

# **post_ui_openwindow_newmail**
> post_ui_openwindow_newmail(new_mail, datasource=datasource, token=token)

Open New Mail Window

Open the New Mail window, according to settings from the request if applicable  --- Alternate route: `/dev/ui/openwindow/newmail/`  Alternate route: `/legacy/ui/openwindow/newmail/`  Alternate route: `/v1/ui/openwindow/newmail/` 

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
api_instance = eve_swagger_api.UserInterfaceApi(eve_swagger_api.ApiClient(configuration))
new_mail = eve_swagger_api.PostUiOpenwindowNewmailNewMail() # PostUiOpenwindowNewmailNewMail | The details of mail to create
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
token = 'token_example' # str | Access token to use if unable to set a header (optional)

try:
    # Open New Mail Window
    api_instance.post_ui_openwindow_newmail(new_mail, datasource=datasource, token=token)
except ApiException as e:
    print("Exception when calling UserInterfaceApi->post_ui_openwindow_newmail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_mail** | [**PostUiOpenwindowNewmailNewMail**](PostUiOpenwindowNewmailNewMail.md)| The details of mail to create | 
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

