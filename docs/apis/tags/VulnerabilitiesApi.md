<a name="__pageTop"></a>
# openapi_client.apis.tags.vulnerabilities_api.VulnerabilitiesApi

All URIs are relative to *https://services.nvd.nist.gov/rest/json*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_cve_history**](#get_cve_history) | **get** /cvehistory/2.0/ | CVE Change History API
[**get_cves**](#get_cves) | **get** /cves/2.0/ | CVE API

# **get_cve_history**
<a name="get_cve_history"></a>
> CveHistoryOas get_cve_history()

CVE Change History API

### Example

```python
import openapi_client
from openapi_client.apis.tags import vulnerabilities_api
from openapi_client.model.cve_history_oas import CveHistoryOas
from pprint import pprint
# Defining the host is optional and defaults to https://services.nvd.nist.gov/rest/json
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://services.nvd.nist.gov/rest/json"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vulnerabilities_api.VulnerabilitiesApi(api_client)

    # example passing only optional values
    query_params = {
        'changeStartDate': "1970-01-01T00:00:00.00Z",
        'changeEndDate': "1970-01-01T00:00:00.00Z",
        'cveId': "CVE-0480-2888001528021798096225500850762068629339333975650685139102691291732729478601482026509127275504175770",
        'eventName': "eventName_example",
        'resultsPerPage': 0,
        'startIndex': 0,
    }
    try:
        # CVE Change History API
        api_response = api_instance.get_cve_history(
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling VulnerabilitiesApi->get_cve_history: %s\n" % e)
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
changeStartDate | ChangeStartDateSchema | | optional
changeEndDate | ChangeEndDateSchema | | optional
cveId | CveIdSchema | | optional
eventName | EventNameSchema | | optional
resultsPerPage | ResultsPerPageSchema | | optional
startIndex | StartIndexSchema | | optional


# ChangeStartDateSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# ChangeEndDateSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# CveIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# EventNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

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
200 | [ApiResponseFor200](#get_cve_history.ApiResponseFor200) | successful operation

#### get_cve_history.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CveHistoryOas**](../../models/CveHistoryOas.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_cves**
<a name="get_cves"></a>
> CveOas get_cves()

CVE API

### Example

```python
import openapi_client
from openapi_client.apis.tags import vulnerabilities_api
from openapi_client.model.cve_oas import CveOas
from pprint import pprint
# Defining the host is optional and defaults to https://services.nvd.nist.gov/rest/json
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://services.nvd.nist.gov/rest/json"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vulnerabilities_api.VulnerabilitiesApi(api_client)

    # example passing only optional values
    query_params = {
        'cpeName': "cpeName_example",
        'cveId': "CVE-0480-2888001528021798096225500850762068629339333975650685139102691291732729478601482026509127275504175770",
        'cvssV2Metrics': "cvssV2Metrics_example",
        'cvssV2Severity': "LOW",
        'cvssV3Metrics': "cvssV3Metrics_example",
        'cvssV3Severity': "LOW",
        'cweId': "CWE-4",
        'hasCertAlerts': False,
        'hasCertNotes': False,
        'hasKev': False,
        'hasOval': False,
        'isVulnerable': False,
        'keywordExactMatch': False,
        'keywordSearch': "keywordSearch_example",
        'lastModStartDate': "1970-01-01T00:00:00.00Z",
        'lastModEndDate': "1970-01-01T00:00:00.00Z",
        'pubStartDate': "1970-01-01T00:00:00.00Z",
        'pubEndDate': "1970-01-01T00:00:00.00Z",
        'resultsPerPage': 0,
        'startIndex': 0,
        'sourceIdentifier': "sourceIdentifier_example",
        'virtualMatchString': "virtualMatchString_example",
    }
    try:
        # CVE API
        api_response = api_instance.get_cves(
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling VulnerabilitiesApi->get_cves: %s\n" % e)
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
cpeName | CpeNameSchema | | optional
cveId | CveIdSchema | | optional
cvssV2Metrics | CvssV2MetricsSchema | | optional
cvssV2Severity | CvssV2SeveritySchema | | optional
cvssV3Metrics | CvssV3MetricsSchema | | optional
cvssV3Severity | CvssV3SeveritySchema | | optional
cweId | CweIdSchema | | optional
hasCertAlerts | HasCertAlertsSchema | | optional
hasCertNotes | HasCertNotesSchema | | optional
hasKev | HasKevSchema | | optional
hasOval | HasOvalSchema | | optional
isVulnerable | IsVulnerableSchema | | optional
keywordExactMatch | KeywordExactMatchSchema | | optional
keywordSearch | KeywordSearchSchema | | optional
lastModStartDate | LastModStartDateSchema | | optional
lastModEndDate | LastModEndDateSchema | | optional
pubStartDate | PubStartDateSchema | | optional
pubEndDate | PubEndDateSchema | | optional
resultsPerPage | ResultsPerPageSchema | | optional
startIndex | StartIndexSchema | | optional
sourceIdentifier | SourceIdentifierSchema | | optional
virtualMatchString | VirtualMatchStringSchema | | optional


# CpeNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CveIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CvssV2MetricsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CvssV2SeveritySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["LOW", "MEDIUM", "HIGH", ] 

# CvssV3MetricsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CvssV3SeveritySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["LOW", "MEDIUM", "HIGH", "CRITICAL", ] 

# CweIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# HasCertAlertsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, bool,  | NoneClass, BoolClass,  |  | if omitted the server will use the default value of False

# HasCertNotesSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, bool,  | NoneClass, BoolClass,  |  | if omitted the server will use the default value of False

# HasKevSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, bool,  | NoneClass, BoolClass,  |  | if omitted the server will use the default value of False

# HasOvalSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, bool,  | NoneClass, BoolClass,  |  | if omitted the server will use the default value of False

# IsVulnerableSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, bool,  | NoneClass, BoolClass,  |  | if omitted the server will use the default value of False

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

# PubStartDateSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# PubEndDateSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

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

# SourceIdentifierSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# VirtualMatchStringSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_cves.ApiResponseFor200) | successful operation

#### get_cves.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CveOas**](../../models/CveOas.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

