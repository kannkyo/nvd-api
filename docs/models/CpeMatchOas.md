# openapi_client.model.cpe_match_oas.CpeMatchOas

JSON Schema for NVD CVE Applicability Statement CPE Match API version 2.0

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | JSON Schema for NVD CVE Applicability Statement CPE Match API version 2.0 | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**startIndex** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**totalResults** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**resultsPerPage** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**format** | str,  | str,  |  | 
**version** | str,  | str,  |  | 
**[matchStrings](#matchStrings)** | list, tuple,  | tuple,  | Array of CPE match strings | 
**timestamp** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# matchStrings

Array of CPE match strings

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Array of CPE match strings | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  | CPE match string or range | 

# items

CPE match string or range

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | CPE match string or range | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**created** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**criteria** | str,  | str,  |  | 
**lastModified** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**matchCriteriaId** | str, uuid.UUID,  | str,  |  | value must be a uuid
**status** | str,  | str,  |  | 
**versionStartExcluding** | str,  | str,  |  | [optional] 
**versionStartIncluding** | str,  | str,  |  | [optional] 
**versionEndExcluding** | str,  | str,  |  | [optional] 
**versionEndIncluding** | str,  | str,  |  | [optional] 
**cpeLastModified** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**[matches](#matches)** | list, tuple,  | tuple,  |  | [optional] 

# matches

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**cpeName** | str,  | str,  |  | 
**cpeNameId** | str, uuid.UUID,  | str,  |  | value must be a uuid

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

