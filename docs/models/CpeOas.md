# openapi_client.model.cpe_oas.CpeOas

JSON Schema for NVD Common Product Enumeration (CPE) API version 2.0

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | JSON Schema for NVD Common Product Enumeration (CPE) API version 2.0 | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**startIndex** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**totalResults** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**resultsPerPage** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**format** | str,  | str,  |  | 
**version** | str,  | str,  |  | 
**[products](#products)** | list, tuple,  | tuple,  | NVD feed array of CPE | 
**timestamp** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# products

NVD feed array of CPE

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | NVD feed array of CPE | 

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
**[cpe](#cpe)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# cpe

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**created** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**deprecated** | bool,  | BoolClass,  |  | 
**cpeName** | str,  | str,  |  | 
**lastModified** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**cpeNameId** | str, uuid.UUID,  | str,  |  | value must be a uuid
**[titles](#titles)** | list, tuple,  | tuple,  |  | [optional] 
**[refs](#refs)** | list, tuple,  | tuple,  |  | [optional] 
**[deprecatedBy](#deprecatedBy)** | list, tuple,  | tuple,  |  | [optional] 

# titles

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  | Human readable title for CPE | 

# items

Human readable title for CPE

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Human readable title for CPE | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**lang** | str,  | str,  |  | 
**title** | str,  | str,  |  | 

# refs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  | Internet resource for CPE | 

# items

Internet resource for CPE

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Internet resource for CPE | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**ref** | str,  | str,  |  | 
**type** | str,  | str,  |  | [optional] must be one of ["Advisory", "Change Log", "Product", "Project", "Vendor", "Version", ] 

# deprecatedBy

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
**cpeName** | str,  | str,  |  | [optional] 
**cpeNameId** | str, uuid.UUID,  | str,  |  | [optional] value must be a uuid
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

