<a name="__pageTop"></a>
# openapi_client.apis.tags.products_api.ProductsApi

All URIs are relative to *https://services.nvd.nist.gov/rest/json*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_cpe_match**](#get_cpe_match) | **get** /cpematch/2.0/ | Match Criteria API
[**get_cpes**](#get_cpes) | **get** /cpes/2.0/ | CPE API

# **get_cpe_match**
<a name="get_cpe_match"></a>
> CpeMatchOas get_cpe_match()

Match Criteria API

### Example

```python
import openapi_client
from openapi_client.apis.tags import products_api
from openapi_client.model.cpe_match_oas import CpeMatchOas
from pprint import pprint
# Defining the host is optional and defaults to https://services.nvd.nist.gov/rest/json
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://services.nvd.nist.gov/rest/json"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = products_api.ProductsApi(api_client)

    # example passing only optional values
    query_params = {
        'cveId': "CVE-0480-2888001528021798096225500850762068629339333975650685139102691291732729478601482026509127275504175770",
        'lastModStartDate': "1970-01-01T00:00:00.00Z",
        'lastModEndDate': "1970-01-01T00:00:00.00Z",
        'matchCriteriaId': "matchCriteriaId_example",
        'resultsPerPage': 0,
        'startIndex': 0,
    }
    try:
        # Match Criteria API
        api_response = api_instance.get_cpe_match(
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProductsApi->get_cpe_match: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
cveId | CveIdSchema | | optional
lastModStartDate | LastModStartDateSchema | | optional
lastModEndDate | LastModEndDateSchema | | optional
matchCriteriaId | MatchCriteriaIdSchema | | optional
resultsPerPage | ResultsPerPageSchema | | optional
startIndex | StartIndexSchema | | optional


# CveIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LastModStartDateSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# LastModEndDateSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# MatchCriteriaIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

# ResultsPerPageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# StartIndexSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_cpe_match.ApiResponseFor200) | successful operation

#### get_cpe_match.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CpeMatchOas**](../../models/CpeMatchOas.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_cpes**
<a name="get_cpes"></a>
> CpeOas get_cpes()

CPE API

### Example

```python
import openapi_client
from openapi_client.apis.tags import products_api
from openapi_client.model.cpe_oas import CpeOas
from pprint import pprint
# Defining the host is optional and defaults to https://services.nvd.nist.gov/rest/json
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://services.nvd.nist.gov/rest/json"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = products_api.ProductsApi(api_client)

    # example passing only optional values
    query_params = {
        'cpeNameId': "cpeNameId_example",
        'cpeMatchString': "cpeMatchString_example",
        'keywordExactMatch': False,
        'keywordSearch': "keywordSearch_example",
        'lastModStartDate': "1970-01-01T00:00:00.00Z",
        'lastModEndDate': "1970-01-01T00:00:00.00Z",
        'matchCriteriaId': "matchCriteriaId_example",
        'resultsPerPage': 0,
        'startIndex': 0,
    }
    try:
        # CPE API
        api_response = api_instance.get_cpes(
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProductsApi->get_cpes: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
cpeNameId | CpeNameIdSchema | | optional
cpeMatchString | CpeMatchStringSchema | | optional
keywordExactMatch | KeywordExactMatchSchema | | optional
keywordSearch | KeywordSearchSchema | | optional
lastModStartDate | LastModStartDateSchema | | optional
lastModEndDate | LastModEndDateSchema | | optional
matchCriteriaId | MatchCriteriaIdSchema | | optional
resultsPerPage | ResultsPerPageSchema | | optional
startIndex | StartIndexSchema | | optional


# CpeNameIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

# CpeMatchStringSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# KeywordExactMatchSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, bool,  | NoneClass, BoolClass,  |  | if omitted the server will use the default value of False

# KeywordSearchSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LastModStartDateSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# LastModEndDateSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# MatchCriteriaIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

# ResultsPerPageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# StartIndexSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_cpes.ApiResponseFor200) | successful operation

#### get_cpes.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CpeOas**](../../models/CpeOas.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

