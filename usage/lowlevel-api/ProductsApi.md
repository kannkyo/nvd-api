# nvd_api.ProductsApi

All URIs are relative to *https://services.nvd.nist.gov/rest/json*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_cpe_match**](ProductsApi.md#get_cpe_match) | **GET** /cpematch/2.0/ | Match Criteria API
[**get_cpes**](ProductsApi.md#get_cpes) | **GET** /cpes/2.0/ | CPE API


# **get_cpe_match**
> CpeMatchOas get_cpe_match()

Match Criteria API

### Example


```python
import time
import nvd_api
from nvd_api.api import products_api
from nvd_api.model.cpe_match_oas import CpeMatchOas
from pprint import pprint
# Defining the host is optional and defaults to https://services.nvd.nist.gov/rest/json
# See configuration.py for a list of all supported configuration parameters.
configuration = nvd_api.Configuration(
    host = "https://services.nvd.nist.gov/rest/json"
)


# Enter a context with an instance of the API client
with nvd_api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = products_api.ProductsApi(api_client)
    cve_id = "CVE-0480-2888001528021798096225500850762068629339333975650685139102691291732729478601482026509127275504175770" # str | CVE ID (optional)
    last_mod_start_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | search by modified date (optional)
    last_mod_end_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | search by modified date (optional)
    match_criteria_id = "matchCriteriaId_example" # str | specific by UUID (optional)
    results_per_page = 0 # int | max number of records (default is 5000) (optional)
    start_index = 0 # int | the index of the first match string (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Match Criteria API
        api_response = api_instance.get_cpe_match(cve_id=cve_id, last_mod_start_date=last_mod_start_date, last_mod_end_date=last_mod_end_date, match_criteria_id=match_criteria_id, results_per_page=results_per_page, start_index=start_index)
        pprint(api_response)
    except nvd_api.ApiException as e:
        print("Exception when calling ProductsApi->get_cpe_match: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cve_id** | **str**| CVE ID | [optional]
 **last_mod_start_date** | **datetime**| search by modified date | [optional]
 **last_mod_end_date** | **datetime**| search by modified date | [optional]
 **match_criteria_id** | **str**| specific by UUID | [optional]
 **results_per_page** | **int**| max number of records (default is 5000) | [optional]
 **start_index** | **int**| the index of the first match string | [optional]

### Return type

[**CpeMatchOas**](CpeMatchOas.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cpes**
> CpeOas get_cpes()

CPE API

### Example


```python
import time
import nvd_api
from nvd_api.api import products_api
from nvd_api.model.cpe_oas import CpeOas
from pprint import pprint
# Defining the host is optional and defaults to https://services.nvd.nist.gov/rest/json
# See configuration.py for a list of all supported configuration parameters.
configuration = nvd_api.Configuration(
    host = "https://services.nvd.nist.gov/rest/json"
)


# Enter a context with an instance of the API client
with nvd_api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = products_api.ProductsApi(api_client)
    cpe_name_id = "cpeNameId_example" # str | specific CPE record UUID (optional)
    cpe_match_string = "cpeMatchString_example" # str | CPE Name (optional)
    keyword_exact_match = "" # str | if CPE exactly match or not (optional) if omitted the server will use the default value of ""
    keyword_search = "keywordSearch_example" # str | a word or phrase is found in the metadata title or reference links (optional)
    last_mod_start_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | search CPE by modified date (optional)
    last_mod_end_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | search CPE by modified date (optional)
    match_criteria_id = "matchCriteriaId_example" # str | search CPE by uuid (optional)
    results_per_page = 0 # int | max number of CPE records (default is 10000) (optional)
    start_index = 0 # int | the index of the first match string (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # CPE API
        api_response = api_instance.get_cpes(cpe_name_id=cpe_name_id, cpe_match_string=cpe_match_string, keyword_exact_match=keyword_exact_match, keyword_search=keyword_search, last_mod_start_date=last_mod_start_date, last_mod_end_date=last_mod_end_date, match_criteria_id=match_criteria_id, results_per_page=results_per_page, start_index=start_index)
        pprint(api_response)
    except nvd_api.ApiException as e:
        print("Exception when calling ProductsApi->get_cpes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cpe_name_id** | **str**| specific CPE record UUID | [optional]
 **cpe_match_string** | **str**| CPE Name | [optional]
 **keyword_exact_match** | **str**| if CPE exactly match or not | [optional] if omitted the server will use the default value of ""
 **keyword_search** | **str**| a word or phrase is found in the metadata title or reference links | [optional]
 **last_mod_start_date** | **datetime**| search CPE by modified date | [optional]
 **last_mod_end_date** | **datetime**| search CPE by modified date | [optional]
 **match_criteria_id** | **str**| search CPE by uuid | [optional]
 **results_per_page** | **int**| max number of CPE records (default is 10000) | [optional]
 **start_index** | **int**| the index of the first match string | [optional]

### Return type

[**CpeOas**](CpeOas.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

