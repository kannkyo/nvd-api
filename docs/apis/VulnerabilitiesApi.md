# nvd_api.VulnerabilitiesApi

All URIs are relative to *https://services.nvd.nist.gov/rest/json*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_cve_history**](VulnerabilitiesApi.md#get_cve_history) | **GET** /cvehistory/2.0/ | CVE Change History API
[**get_cves**](VulnerabilitiesApi.md#get_cves) | **GET** /cves/2.0/ | CVE API


# **get_cve_history**
> CveHistoryOas get_cve_history()

CVE Change History API

### Example


```python
import time
import nvd_api
from nvd_api.api import vulnerabilities_api
from nvd_api.model.cve_history_oas import CveHistoryOas
from pprint import pprint
# Defining the host is optional and defaults to https://services.nvd.nist.gov/rest/json
# See configuration.py for a list of all supported configuration parameters.
configuration = nvd_api.Configuration(
    host = "https://services.nvd.nist.gov/rest/json"
)


# Enter a context with an instance of the API client
with nvd_api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = vulnerabilities_api.VulnerabilitiesApi(api_client)
    change_start_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | search by changed date (optional)
    change_end_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | search by changed date (optional)
    cve_id = "CVE-0480-2888001528021798096225500850762068629339333975650685139102691291732729478601482026509127275504175770" # str | CVE ID (optional)
    event_name = "eventName_example" # str | returns all CVE associated with a specific type of change event (optional)
    results_per_page = 0 # int | max number of records (default is 5000) (optional)
    start_index = 0 # int | the index of the first match string (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # CVE Change History API
        api_response = api_instance.get_cve_history(change_start_date=change_start_date, change_end_date=change_end_date, cve_id=cve_id, event_name=event_name, results_per_page=results_per_page, start_index=start_index)
        pprint(api_response)
    except nvd_api.ApiException as e:
        print("Exception when calling VulnerabilitiesApi->get_cve_history: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **change_start_date** | **datetime**| search by changed date | [optional]
 **change_end_date** | **datetime**| search by changed date | [optional]
 **cve_id** | **str**| CVE ID | [optional]
 **event_name** | **str**| returns all CVE associated with a specific type of change event | [optional]
 **results_per_page** | **int**| max number of records (default is 5000) | [optional]
 **start_index** | **int**| the index of the first match string | [optional]

### Return type

[**CveHistoryOas**](CveHistoryOas.md)

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

# **get_cves**
> CveOas get_cves()

CVE API

### Example


```python
import time
import nvd_api
from nvd_api.api import vulnerabilities_api
from nvd_api.model.cve_oas import CveOas
from pprint import pprint
# Defining the host is optional and defaults to https://services.nvd.nist.gov/rest/json
# See configuration.py for a list of all supported configuration parameters.
configuration = nvd_api.Configuration(
    host = "https://services.nvd.nist.gov/rest/json"
)


# Enter a context with an instance of the API client
with nvd_api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = vulnerabilities_api.VulnerabilitiesApi(api_client)
    cpe_name = "cpeName_example" # str | CPE Name (optional)
    cve_id = "CVE-0480-2888001528021798096225500850762068629339333975650685139102691291732729478601482026509127275504175770" # str | CVE ID (optional)
    cvss_v2_metrics = "cvssV2Metrics_example" # str | CVSSv2 vector string (optional)
    cvss_v2_severity = "LOW" # str | CVSSv2 qualitative severity rating (optional)
    cvss_v3_metrics = "cvssV3Metrics_example" # str | CVSSv3 vector string (optional)
    cvss_v3_severity = "LOW" # str | CVSSv3 qualitative severity rating (optional)
    cwe_id = "CWE-4" # str | CWE ID (optional)
    has_cert_alerts = "" # str | contain a Technical Alert from US-CERT (optional) if omitted the server will use the default value of ""
    has_cert_notes = "" # str | contain a Vulnerability Note from CERT/CC (optional) if omitted the server will use the default value of ""
    has_kev = "" # str | appear in CISA's Known Exploited Vulnerabilities (KEV) Catalog (optional) if omitted the server will use the default value of ""
    has_oval = "" # str | contain information from MITRE's Open Vulnerability and Assessment Language (OVAL) (optional) if omitted the server will use the default value of ""
    is_vulnerable = "" # str | returns only CVE associated with a specific CPE (optional) if omitted the server will use the default value of ""
    keyword_exact_match = "" # str | returns any CVE where a word or phrase (optional) if omitted the server will use the default value of ""
    keyword_search = "keywordSearch_example" # str | a word or phrase is found in the current description (optional)
    last_mod_start_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | search by modified date (optional)
    last_mod_end_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | search by modified date (optional)
    pub_start_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | search by published date (optional)
    pub_end_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | search by published date (optional)
    results_per_page = 0 # int | max number of records (default is 2000) (optional)
    start_index = 0 # int | the index of the first match string (optional)
    source_identifier = "sourceIdentifier_example" # str | returns CVE where the exact value of sourceIdentifier appears (optional)
    virtual_match_string = "virtualMatchString_example" # str | CVE more broadly than cpeName (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # CVE API
        api_response = api_instance.get_cves(cpe_name=cpe_name, cve_id=cve_id, cvss_v2_metrics=cvss_v2_metrics, cvss_v2_severity=cvss_v2_severity, cvss_v3_metrics=cvss_v3_metrics, cvss_v3_severity=cvss_v3_severity, cwe_id=cwe_id, has_cert_alerts=has_cert_alerts, has_cert_notes=has_cert_notes, has_kev=has_kev, has_oval=has_oval, is_vulnerable=is_vulnerable, keyword_exact_match=keyword_exact_match, keyword_search=keyword_search, last_mod_start_date=last_mod_start_date, last_mod_end_date=last_mod_end_date, pub_start_date=pub_start_date, pub_end_date=pub_end_date, results_per_page=results_per_page, start_index=start_index, source_identifier=source_identifier, virtual_match_string=virtual_match_string)
        pprint(api_response)
    except nvd_api.ApiException as e:
        print("Exception when calling VulnerabilitiesApi->get_cves: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cpe_name** | **str**| CPE Name | [optional]
 **cve_id** | **str**| CVE ID | [optional]
 **cvss_v2_metrics** | **str**| CVSSv2 vector string | [optional]
 **cvss_v2_severity** | **str**| CVSSv2 qualitative severity rating | [optional]
 **cvss_v3_metrics** | **str**| CVSSv3 vector string | [optional]
 **cvss_v3_severity** | **str**| CVSSv3 qualitative severity rating | [optional]
 **cwe_id** | **str**| CWE ID | [optional]
 **has_cert_alerts** | **str**| contain a Technical Alert from US-CERT | [optional] if omitted the server will use the default value of ""
 **has_cert_notes** | **str**| contain a Vulnerability Note from CERT/CC | [optional] if omitted the server will use the default value of ""
 **has_kev** | **str**| appear in CISA&#39;s Known Exploited Vulnerabilities (KEV) Catalog | [optional] if omitted the server will use the default value of ""
 **has_oval** | **str**| contain information from MITRE&#39;s Open Vulnerability and Assessment Language (OVAL) | [optional] if omitted the server will use the default value of ""
 **is_vulnerable** | **str**| returns only CVE associated with a specific CPE | [optional] if omitted the server will use the default value of ""
 **keyword_exact_match** | **str**| returns any CVE where a word or phrase | [optional] if omitted the server will use the default value of ""
 **keyword_search** | **str**| a word or phrase is found in the current description | [optional]
 **last_mod_start_date** | **datetime**| search by modified date | [optional]
 **last_mod_end_date** | **datetime**| search by modified date | [optional]
 **pub_start_date** | **datetime**| search by published date | [optional]
 **pub_end_date** | **datetime**| search by published date | [optional]
 **results_per_page** | **int**| max number of records (default is 2000) | [optional]
 **start_index** | **int**| the index of the first match string | [optional]
 **source_identifier** | **str**| returns CVE where the exact value of sourceIdentifier appears | [optional]
 **virtual_match_string** | **str**| CVE more broadly than cpeName | [optional]

### Return type

[**CveOas**](CveOas.md)

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

