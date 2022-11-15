# openapi_client.model.cve_oas.CveOas

JSON Schema for NVD Vulnerability Data API version 2.0

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | JSON Schema for NVD Vulnerability Data API version 2.0 | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**startIndex** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**totalResults** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**resultsPerPage** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**format** | str,  | str,  |  | 
**[vulnerabilities](#vulnerabilities)** | list, tuple,  | tuple,  | NVD feed array of CVE | 
**version** | str,  | str,  |  | 
**timestamp** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# vulnerabilities

NVD feed array of CVE

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | NVD feed array of CVE | 

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
**[cve](#cve)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# cve

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[references](#references)** | list, tuple,  | tuple,  |  | 
**[descriptions](#descriptions)** | list, tuple,  | tuple,  |  | 
**id** | str,  | str,  |  | [optional] 
**sourceIdentifier** | str,  | str,  |  | [optional] 
**vulnStatus** | str,  | str,  |  | [optional] 
**published** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**lastModified** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**evaluatorComment** | str,  | str,  |  | [optional] 
**evaluatorSolution** | str,  | str,  |  | [optional] 
**evaluatorImpact** | str,  | str,  |  | [optional] 
**cisaExploitAdd** | str, date,  | str,  |  | [optional] value must conform to RFC-3339 full-date YYYY-MM-DD
**cisaActionDue** | str, date,  | str,  |  | [optional] value must conform to RFC-3339 full-date YYYY-MM-DD
**cisaRequiredAction** | str,  | str,  |  | [optional] 
**cisaVulnerabilityName** | str,  | str,  |  | [optional] 
**[metrics](#metrics)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Metric scores for a vulnerability as found on NVD. | [optional] 
**[weaknesses](#weaknesses)** | list, tuple,  | tuple,  |  | [optional] 
**[configurations](#configurations)** | list, tuple,  | tuple,  |  | [optional] 
**[vendorComments](#vendorComments)** | list, tuple,  | tuple,  |  | [optional] 

# descriptions

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
**lang** | str,  | str,  |  | 
**value** | str,  | str,  |  | 

# references

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
**url** | str,  | str,  |  | 
**source** | str,  | str,  |  | [optional] 
**[tags](#tags)** | list, tuple,  | tuple,  |  | [optional] 

# tags

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# metrics

Metric scores for a vulnerability as found on NVD.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Metric scores for a vulnerability as found on NVD. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[cvssMetricV31](#cvssMetricV31)** | list, tuple,  | tuple,  | CVSS V3.1 score. | [optional] 
**[cvssMetricV30](#cvssMetricV30)** | list, tuple,  | tuple,  | CVSS V3.0 score. | [optional] 
**[cvssMetricV2](#cvssMetricV2)** | list, tuple,  | tuple,  | CVSS V2.0 score. | [optional] 

# cvssMetricV31

CVSS V3.1 score.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | CVSS V3.1 score. | 

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
**[cvssData](#cvssData)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 
**source** | str,  | str,  |  | 
**[type](#type)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | must be one of ["Primary", "Secondary", ] 
**exploitabilityScore** | decimal.Decimal, int, float,  | decimal.Decimal,  | CVSS subscore. | [optional] 
**impactScore** | decimal.Decimal, int, float,  | decimal.Decimal,  | CVSS subscore. | [optional] 

# type

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | must be one of ["Primary", "Secondary", ] 

# cvssData

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**baseSeverity** | str,  | str,  |  | must be one of ["NONE", "LOW", "MEDIUM", "HIGH", "CRITICAL", ] 
**baseScore** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | 
**vectorString** | str,  | str,  |  | 
**version** | str,  | str,  | CVSS Version | must be one of ["3.1", ] 
**attackVector** | str,  | str,  |  | [optional] must be one of ["NETWORK", "ADJACENT_NETWORK", "LOCAL", "PHYSICAL", ] 
**attackComplexity** | str,  | str,  |  | [optional] must be one of ["HIGH", "LOW", ] 
**privilegesRequired** | str,  | str,  |  | [optional] must be one of ["HIGH", "LOW", "NONE", ] 
**userInteraction** | str,  | str,  |  | [optional] must be one of ["NONE", "REQUIRED", ] 
**scope** | str,  | str,  |  | [optional] must be one of ["UNCHANGED", "CHANGED", ] 
**confidentialityImpact** | str,  | str,  |  | [optional] must be one of ["NONE", "LOW", "HIGH", ] 
**integrityImpact** | str,  | str,  |  | [optional] must be one of ["NONE", "LOW", "HIGH", ] 
**availabilityImpact** | str,  | str,  |  | [optional] must be one of ["NONE", "LOW", "HIGH", ] 
**exploitCodeMaturity** | str,  | str,  |  | [optional] must be one of ["UNPROVEN", "PROOF_OF_CONCEPT", "FUNCTIONAL", "HIGH", "NOT_DEFINED", ] 
**remediationLevel** | str,  | str,  |  | [optional] must be one of ["OFFICIAL_FIX", "TEMPORARY_FIX", "WORKAROUND", "UNAVAILABLE", "NOT_DEFINED", ] 
**reportConfidence** | str,  | str,  |  | [optional] must be one of ["UNKNOWN", "REASONABLE", "CONFIRMED", "NOT_DEFINED", ] 
**temporalScore** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**temporalSeverity** | str,  | str,  |  | [optional] must be one of ["NONE", "LOW", "MEDIUM", "HIGH", "CRITICAL", ] 
**confidentialityRequirement** | str,  | str,  |  | [optional] must be one of ["LOW", "MEDIUM", "HIGH", "NOT_DEFINED", ] 
**integrityRequirement** | str,  | str,  |  | [optional] must be one of ["LOW", "MEDIUM", "HIGH", "NOT_DEFINED", ] 
**availabilityRequirement** | str,  | str,  |  | [optional] must be one of ["LOW", "MEDIUM", "HIGH", "NOT_DEFINED", ] 
**modifiedAttackVector** | str,  | str,  |  | [optional] must be one of ["NETWORK", "ADJACENT_NETWORK", "LOCAL", "PHYSICAL", "NOT_DEFINED", ] 
**modifiedAttackComplexity** | str,  | str,  |  | [optional] must be one of ["HIGH", "LOW", "NOT_DEFINED", ] 
**modifiedPrivilegesRequired** | str,  | str,  |  | [optional] must be one of ["HIGH", "LOW", "NONE", "NOT_DEFINED", ] 
**modifiedUserInteraction** | str,  | str,  |  | [optional] must be one of ["NONE", "REQUIRED", "NOT_DEFINED", ] 
**modifiedScope** | str,  | str,  |  | [optional] must be one of ["UNCHANGED", "CHANGED", "NOT_DEFINED", ] 
**modifiedConfidentialityImpact** | str,  | str,  |  | [optional] must be one of ["NONE", "LOW", "HIGH", "NOT_DEFINED", ] 
**modifiedIntegrityImpact** | str,  | str,  |  | [optional] must be one of ["NONE", "LOW", "HIGH", "NOT_DEFINED", ] 
**modifiedAvailabilityImpact** | str,  | str,  |  | [optional] must be one of ["NONE", "LOW", "HIGH", "NOT_DEFINED", ] 
**environmentalScore** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**environmentalSeverity** | str,  | str,  |  | [optional] must be one of ["NONE", "LOW", "MEDIUM", "HIGH", "CRITICAL", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# cvssMetricV30

CVSS V3.0 score.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | CVSS V3.0 score. | 

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
**[cvssData](#cvssData)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 
**source** | str,  | str,  |  | 
**[type](#type)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | must be one of ["Primary", "Secondary", ] 
**exploitabilityScore** | decimal.Decimal, int, float,  | decimal.Decimal,  | CVSS subscore. | [optional] 
**impactScore** | decimal.Decimal, int, float,  | decimal.Decimal,  | CVSS subscore. | [optional] 

# type

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | must be one of ["Primary", "Secondary", ] 

# cvssData

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**baseSeverity** | str,  | str,  |  | must be one of ["NONE", "LOW", "MEDIUM", "HIGH", "CRITICAL", ] 
**baseScore** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | 
**vectorString** | str,  | str,  |  | 
**version** | str,  | str,  | CVSS Version | must be one of ["3.0", ] 
**attackVector** | str,  | str,  |  | [optional] must be one of ["NETWORK", "ADJACENT_NETWORK", "LOCAL", "PHYSICAL", ] 
**attackComplexity** | str,  | str,  |  | [optional] must be one of ["HIGH", "LOW", ] 
**privilegesRequired** | str,  | str,  |  | [optional] must be one of ["HIGH", "LOW", "NONE", ] 
**userInteraction** | str,  | str,  |  | [optional] must be one of ["NONE", "REQUIRED", ] 
**scope** | str,  | str,  |  | [optional] must be one of ["UNCHANGED", "CHANGED", ] 
**confidentialityImpact** | str,  | str,  |  | [optional] must be one of ["NONE", "LOW", "HIGH", ] 
**integrityImpact** | str,  | str,  |  | [optional] must be one of ["NONE", "LOW", "HIGH", ] 
**availabilityImpact** | str,  | str,  |  | [optional] must be one of ["NONE", "LOW", "HIGH", ] 
**exploitCodeMaturity** | str,  | str,  |  | [optional] must be one of ["UNPROVEN", "PROOF_OF_CONCEPT", "FUNCTIONAL", "HIGH", "NOT_DEFINED", ] 
**remediationLevel** | str,  | str,  |  | [optional] must be one of ["OFFICIAL_FIX", "TEMPORARY_FIX", "WORKAROUND", "UNAVAILABLE", "NOT_DEFINED", ] 
**reportConfidence** | str,  | str,  |  | [optional] must be one of ["UNKNOWN", "REASONABLE", "CONFIRMED", "NOT_DEFINED", ] 
**temporalScore** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**temporalSeverity** | str,  | str,  |  | [optional] must be one of ["NONE", "LOW", "MEDIUM", "HIGH", "CRITICAL", ] 
**confidentialityRequirement** | str,  | str,  |  | [optional] must be one of ["LOW", "MEDIUM", "HIGH", "NOT_DEFINED", ] 
**integrityRequirement** | str,  | str,  |  | [optional] must be one of ["LOW", "MEDIUM", "HIGH", "NOT_DEFINED", ] 
**availabilityRequirement** | str,  | str,  |  | [optional] must be one of ["LOW", "MEDIUM", "HIGH", "NOT_DEFINED", ] 
**modifiedAttackVector** | str,  | str,  |  | [optional] must be one of ["NETWORK", "ADJACENT_NETWORK", "LOCAL", "PHYSICAL", "NOT_DEFINED", ] 
**modifiedAttackComplexity** | str,  | str,  |  | [optional] must be one of ["HIGH", "LOW", "NOT_DEFINED", ] 
**modifiedPrivilegesRequired** | str,  | str,  |  | [optional] must be one of ["HIGH", "LOW", "NONE", "NOT_DEFINED", ] 
**modifiedUserInteraction** | str,  | str,  |  | [optional] must be one of ["NONE", "REQUIRED", "NOT_DEFINED", ] 
**modifiedScope** | str,  | str,  |  | [optional] must be one of ["UNCHANGED", "CHANGED", "NOT_DEFINED", ] 
**modifiedConfidentialityImpact** | str,  | str,  |  | [optional] must be one of ["NONE", "LOW", "HIGH", "NOT_DEFINED", ] 
**modifiedIntegrityImpact** | str,  | str,  |  | [optional] must be one of ["NONE", "LOW", "HIGH", "NOT_DEFINED", ] 
**modifiedAvailabilityImpact** | str,  | str,  |  | [optional] must be one of ["NONE", "LOW", "HIGH", "NOT_DEFINED", ] 
**environmentalScore** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**environmentalSeverity** | str,  | str,  |  | [optional] must be one of ["NONE", "LOW", "MEDIUM", "HIGH", "CRITICAL", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# cvssMetricV2

CVSS V2.0 score.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | CVSS V2.0 score. | 

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
**[cvssData](#cvssData)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 
**source** | str,  | str,  |  | 
**[type](#type)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | must be one of ["Primary", "Secondary", ] 
**baseSeverity** | str,  | str,  |  | [optional] 
**exploitabilityScore** | decimal.Decimal, int, float,  | decimal.Decimal,  | CVSS subscore. | [optional] 
**impactScore** | decimal.Decimal, int, float,  | decimal.Decimal,  | CVSS subscore. | [optional] 
**acInsufInfo** | bool,  | BoolClass,  |  | [optional] 
**obtainAllPrivilege** | bool,  | BoolClass,  |  | [optional] 
**obtainUserPrivilege** | bool,  | BoolClass,  |  | [optional] 
**obtainOtherPrivilege** | bool,  | BoolClass,  |  | [optional] 
**userInteractionRequired** | bool,  | BoolClass,  |  | [optional] 

# type

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | must be one of ["Primary", "Secondary", ] 

# cvssData

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**baseScore** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | 
**vectorString** | str,  | str,  |  | 
**version** | str,  | str,  | CVSS Version | must be one of ["2.0", ] 
**accessVector** | str,  | str,  |  | [optional] must be one of ["NETWORK", "ADJACENT_NETWORK", "LOCAL", ] 
**accessComplexity** | str,  | str,  |  | [optional] must be one of ["HIGH", "MEDIUM", "LOW", ] 
**authentication** | str,  | str,  |  | [optional] must be one of ["MULTIPLE", "SINGLE", "NONE", ] 
**confidentialityImpact** | str,  | str,  |  | [optional] must be one of ["NONE", "PARTIAL", "COMPLETE", ] 
**integrityImpact** | str,  | str,  |  | [optional] must be one of ["NONE", "PARTIAL", "COMPLETE", ] 
**availabilityImpact** | str,  | str,  |  | [optional] must be one of ["NONE", "PARTIAL", "COMPLETE", ] 
**exploitability** | str,  | str,  |  | [optional] must be one of ["UNPROVEN", "PROOF_OF_CONCEPT", "FUNCTIONAL", "HIGH", "NOT_DEFINED", ] 
**remediationLevel** | str,  | str,  |  | [optional] must be one of ["OFFICIAL_FIX", "TEMPORARY_FIX", "WORKAROUND", "UNAVAILABLE", "NOT_DEFINED", ] 
**reportConfidence** | str,  | str,  |  | [optional] must be one of ["UNCONFIRMED", "UNCORROBORATED", "CONFIRMED", "NOT_DEFINED", ] 
**temporalScore** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**collateralDamagePotential** | str,  | str,  |  | [optional] must be one of ["NONE", "LOW", "LOW_MEDIUM", "MEDIUM_HIGH", "HIGH", "NOT_DEFINED", ] 
**targetDistribution** | str,  | str,  |  | [optional] must be one of ["NONE", "LOW", "MEDIUM", "HIGH", "NOT_DEFINED", ] 
**confidentialityRequirement** | str,  | str,  |  | [optional] must be one of ["LOW", "MEDIUM", "HIGH", "NOT_DEFINED", ] 
**integrityRequirement** | str,  | str,  |  | [optional] must be one of ["LOW", "MEDIUM", "HIGH", "NOT_DEFINED", ] 
**availabilityRequirement** | str,  | str,  |  | [optional] must be one of ["LOW", "MEDIUM", "HIGH", "NOT_DEFINED", ] 
**environmentalScore** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# weaknesses

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
**[description](#description)** | list, tuple,  | tuple,  |  | 
**source** | str,  | str,  |  | 
**type** | str,  | str,  |  | 

# description

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
**lang** | str,  | str,  |  | 
**value** | str,  | str,  |  | 

# configurations

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
**[nodes](#nodes)** | list, tuple,  | tuple,  |  | 
**operator** | str,  | str,  |  | [optional] must be one of ["AND", "OR", ] 
**negate** | bool,  | BoolClass,  |  | [optional] 

# nodes

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  | Defines a configuration node in an NVD applicability statement. | 

# items

Defines a configuration node in an NVD applicability statement.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Defines a configuration node in an NVD applicability statement. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**operator** | str,  | str,  |  | must be one of ["AND", "OR", ] 
**[cpeMatch](#cpeMatch)** | list, tuple,  | tuple,  |  | 
**negate** | bool,  | BoolClass,  |  | [optional] 

# cpeMatch

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

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
**vulnerable** | bool,  | BoolClass,  |  | 
**criteria** | str,  | str,  |  | 
**matchCriteriaId** | str, uuid.UUID,  | str,  |  | value must be a uuid
**versionStartExcluding** | str,  | str,  |  | [optional] 
**versionStartIncluding** | str,  | str,  |  | [optional] 
**versionEndExcluding** | str,  | str,  |  | [optional] 
**versionEndIncluding** | str,  | str,  |  | [optional] 

# vendorComments

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
**organization** | str,  | str,  |  | 
**comment** | str,  | str,  |  | 
**lastModified** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

