# eve_swagger_api.InsuranceApi

All URIs are relative to *https://esi.evetech.net/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_insurance_prices**](InsuranceApi.md#get_insurance_prices) | **GET** /insurance/prices/ | List insurance levels


# **get_insurance_prices**
> list[GetInsurancePrices200Ok] get_insurance_prices(accept_language=accept_language, datasource=datasource, if_none_match=if_none_match, language=language)

List insurance levels

Return available insurance levels for all ship types  --- Alternate route: `/dev/insurance/prices/`  Alternate route: `/legacy/insurance/prices/`  Alternate route: `/v1/insurance/prices/`  --- This route is cached for up to 3600 seconds

### Example
```python
from __future__ import print_function
import time
import eve_swagger_api
from eve_swagger_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = eve_swagger_api.InsuranceApi()
accept_language = 'en' # str | Language to use in the response (optional) (default to en)
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
language = 'en' # str | Language to use in the response, takes precedence over Accept-Language (optional) (default to en)

try:
    # List insurance levels
    api_response = api_instance.get_insurance_prices(accept_language=accept_language, datasource=datasource, if_none_match=if_none_match, language=language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InsuranceApi->get_insurance_prices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language to use in the response | [optional] [default to en]
 **datasource** | **str**| The server name you would like data from | [optional] [default to tranquility]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **language** | **str**| Language to use in the response, takes precedence over Accept-Language | [optional] [default to en]

### Return type

[**list[GetInsurancePrices200Ok]**](GetInsurancePrices200Ok.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

