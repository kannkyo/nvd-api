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
------------------

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

Products / CPE Match API
------------------------

.. code-block:: python

    from client import NvdApiClient
    from pprint import pprint

    client = NvdApiClient()

    response = client.get_cpe_match(
        cve_id="CVE-2022-32223",
        results_per_page=1,
        start_index=0
    )
    pprint(response)

Vulnerabilities / CVE API
-------------------------

.. code-block:: python

    from client import NvdApiClient
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

Vulnerabilities / CVE History API
---------------------------------

.. code-block:: python

    from client import NvdApiClient
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

