=================
NVD API Client
=================


NVD API client is a community driven NVD API 2.0 client. 
This client support `Vulnerabilities`_ API and `Products`_ API.

.. _Vulnerabilities: https://nvd.nist.gov/developers/vulnerabilities
.. _Products: https://nvd.nist.gov/developers/products

.. image:: https://badge.fury.io/py/nvd-api.svg
    :target: https://badge.fury.io/py/nvd-api

.. image:: https://github.com/kannkyo/nvd-api/actions/workflows/python-ci.yml/badge.svg
    :target: https://github.com/kannkyo/nvd-api/actions/workflows/python-ci.yml

.. image:: https://codecov.io/gh/kannkyo/nvd-api/branch/main/graph/badge.svg?token=ASYLVG3X9O
    :target: https://codecov.io/gh/kannkyo/nvd-api

.. image:: https://github.com/kannkyo/nvd-api/actions/workflows/scorecards.yml/badge.svg
    :target: https://github.com/kannkyo/nvd-api/actions/workflows/scorecards.yml

.. image:: https://bestpractices.coreinfrastructure.org/projects/6889/badge
    :target: https://bestpractices.coreinfrastructure.org/projects/6889

Getting Start
=============

Products / CPE API
---------------------

This API's simple example is bellow.

.. code-block:: python

    from client import NvdApiClient
    from pprint import pprint

    client = NvdApiClient()

    response = client.get_cpes(
        cpe_name_id="87316812-5F2C-4286-94FE-CC98B9EAEF53",
        results_per_page=1,
        start_index=0
    )
    pprint(response)

`get_cpes` method check API's all constraints and limitations.

* cpeNameId and matchCriteriaId must be uuid format.
* cpeMatchString must be CPEv2.3 format.
* If filtering by keywordExactMatch, keywordSearch is REQUIRED.
* If filtering by the last modified date, both lastModStartDate and lastModEndDate are REQUIRED.
* resultsPerPage's maximum allowable limit is 10,000.
* The maximum allowable range when using any date range parameters is 120 consecutive days.

Products / Match Criteria API
-----------------------------

This API's simple example is bellow.

.. code-block:: python

    from nvd_api import NvdApiClient
    from pprint import pprint

    client = NvdApiClient()

    response = client.get_cpe_match(
        cve_id="CVE-2022-32223",
        results_per_page=1,
        start_index=0
    )
    pprint(response)

`get_cpe_match` method check API's all constraints and limitations.

* cveId is must be CVE ID format.
* If filtering by the last modified date, both lastModStartDate and lastModEndDate are REQUIRED.
* matchCriteriaId must be uuid format.
* resultsPerPage's maximum allowable limit is 5,000.
* The maximum allowable range when using any date range parameters is 120 consecutive days.
* cpeName must be CPEv2.3 format.

Vulnerabilities / CVE API
---------------------------

This API's simple example is bellow.

.. code-block:: python

    from nvd_api import NvdApiClient
    from pprint import pprint

    client = NvdApiClient()

    response = client.get_cves(
        cpe_name="cpe:2.3:o:debian:debian_linux:3.0:*:*:*:*:*:*:*",
        cvss_v2_metrics="AV:L/AC:L/Au:N/C:C/I:C/A:C",
        cvss_v2_severity="HIGH",
        results_per_page=1,
        start_index=1
    )
    pprint(response)

* cpeName must be CPEv2.3 format.
* cveId is must be CVE ID format.
* cvssV2Severity, cvssV2Metrics is must be CVSS v2 format.
* cvssV3Severity, cvssV3Metrics is must be CVSS v3 format.
* cweId is must be CWE ID format.
* resultsPerPage's maximum allowable limit is 2,000.
* If filtering by keywordExactMatch, keywordSearch is REQUIRED.
* If filtering by the last modified date, both lastModStartDate and lastModEndDate are REQUIRED.
* If filtering by the last modified date, both pubStartDate and pubEndDate are REQUIRED.
* The maximum allowable range when using any date range parameters is 120 consecutive days.
* cvssV2Metrics cannot be used in requests that include cvssV3Metrics.
* cvssV3Metrics cannot be used in requests that include cvssV2Metrics.
* cvssV2Severity cannot be used in requests that include cvssV3Severity.
* cvssV3Severity cannot be used in requests that include cvssV2Severity.

Vulnerabilities / CVE Change History API
-------------------------------------------

This API's simple example is bellow.

.. code-block:: python

    from nvd_api import NvdApiClient
    from pprint import pprint

    client = NvdApiClient()

    response = client.get_cve_history(
        change_start_date="2021-08-04T00:00:00.000",
        change_end_date="2021-10-23T00:00:00.000",
        event_name="CVE Rejected",
        results_per_page=1,
        start_index=1
    )
    pprint(response)

`get_cve_history` method check API's all constraints and limitations.

* If filtering by the change date, both changeStartDate and changeEndDate are REQUIRED.
* cveId is must be CVE ID format.
* resultsPerPage's maximum allowable limit is 5,000.
* The maximum allowable range when using any date range parameters is 120 consecutive days.

With API Key
---------------------

If you have the nvd api key, you can set key to client.

.. code-block:: python

    from nvd_api import NvdApiClient
    from pprint import pprint

    client = NvdApiClient(wait_time=1 * 1000, api_key='THIS IS API KEY')

    response = client.get_cves(
        cpe_name="cpe:2.3:o:debian:debian_linux:3.0:*:*:*:*:*:*:*",
        cvss_v2_metrics="AV:L/AC:L/Au:N/C:C/I:C/A:C",
        cvss_v2_severity="HIGH",
        results_per_page=1,
        start_index=1
    )
    pprint(response)

* api_key : api key published by nvd.
* wait_time : interval time to execute api (with api key is 50 requests in a rolling 30s window, without api key is 5 requests in a rolling 30s window)
