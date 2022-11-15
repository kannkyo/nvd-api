# openapi_client.model.cve_history_oas.CveHistoryOas

JSON Schema for NVD CVE History API version 2.0

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | JSON Schema for NVD CVE History API version 2.0 | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**startIndex** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**totalResults** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**resultsPerPage** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**format** | str,  | str,  |  | 
**version** | str,  | str,  |  | 
**timestamp** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**[cveChanges](#cveChanges)** | list, tuple,  | tuple,  | Array of CVE Changes | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# cveChanges

Array of CVE Changes

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Array of CVE Changes | 

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
**[change](#change)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# change

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**sourceIdentifier** | str,  | str,  |  | 
**cveId** | str,  | str,  |  | 
**eventName** | str,  | str,  |  | 
**cveChangeId** | str, uuid.UUID,  | str,  |  | value must be a uuid
**created** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**[details](#details)** | list, tuple,  | tuple,  |  | [optional] 

# details

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
**type** | str,  | str,  |  | 
**action** | str,  | str,  |  | [optional] 
**oldValue** | str,  | str,  |  | [optional] 
**newValue** | str,  | str,  |  | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

