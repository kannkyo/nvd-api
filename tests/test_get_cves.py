"""
    NVD API 2.0 Python API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Contact: 15080890+kannkyo@users.noreply.github.com
    Generated by: https://openapi-generator.tech
"""


import os
import unittest
from pprint import pprint

from nvd_api.client import (CVSS_V2_SEVERITY, CVSS_V3_SEVERITY, VERSION_TYPE,
                            NvdApiClient)
from nvd_api.low_api.exceptions import ApiValueError, NotFoundException


class TestGetCves(unittest.TestCase):
    def setUp(self):
        api_key = os.getenv('NVD_API_KEY')
        if api_key:
            self.client = NvdApiClient(wait_time=1 * 1000, api_key=api_key)  # noqa: E501
        else:
            self.client = NvdApiClient(wait_time=10 * 1000)  # noqa: E501

    def tearDown(self):
        pass

    def test_get_by_cve(self):
        response = self.client.get_cves(
            cpe_name="cpe:2.3:a:ibm:mq:9.0.0.0:*:*:*:lts:*:*:*",
            cve_id="CVE-2019-4227",
            cwe_id="CWE-384",
            is_vulnerable=True,
            source_identifier="nvd@nist.gov"
        )
        pprint(response)
        assert response.results_per_page == 1
        assert response.start_index == 0
        assert response.total_results == 1
        assert response.format == 'NVD_CVE'
        assert response.version == '2.0'
        assert response.timestamp is not None
        assert (len(response.vulnerabilities) > 0)

    def test_get_by_specific_cpe_name(self):
        response = self.client.get_cves(
            cpe_name="cpe:2.3:o:microsoft:windows_10:1607:*:*:*:*:*:*:*",
            results_per_page=1,
            start_index=0
        )
        pprint(response)
        assert (len(response.vulnerabilities) > 0)

    def test_get_by_incomplete_cpe_name(self):
        response = self.client.get_cves(
            cpe_name="cpe:2.3:o:microsoft:windows_10:1607",
            results_per_page=1,
            start_index=0
        )
        pprint(response)
        assert (len(response.vulnerabilities) > 0)

    def test_get_by_cvss_v2(self):
        response = self.client.get_cves(
            cpe_name="cpe:2.3:o:debian:debian_linux:3.0:*:*:*:*:*:*:*",
            cvss_v2_metrics="AV:L/AC:L/Au:N/C:C/I:C/A:C",
            cvss_v2_severity=CVSS_V2_SEVERITY.HIGH,
            results_per_page=1,
            start_index=1
        )
        pprint(response)
        assert (len(response.vulnerabilities) > 0)

    def test_get_by_cvss_v3(self):
        response = self.client.get_cves(
            cpe_name="cpe:2.3:o:debian:debian_linux:3.0:*:*:*:*:*:*:*",
            cvss_v3_metrics="AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H",
            cvss_v3_severity=CVSS_V3_SEVERITY.HIGH,
            results_per_page=1,
            start_index=0
        )
        pprint(response)
        assert (len(response.vulnerabilities) > 0)

    def test_get_by_has_flags(self):
        response = self.client.get_cves(
            has_cert_alerts=True,
            has_cert_notes=True,
            has_kev=True,
            has_oval=True,
            no_rejected=True,
            results_per_page=1,
            start_index=1
        )
        pprint(response)
        assert (len(response.vulnerabilities) > 0)

    def test_get_by_keywords(self):
        response = self.client.get_cves(
            keyword_exact_match=True,
            keyword_search="CentOS",
            results_per_page=1,
            start_index=1
        )
        pprint(response)
        assert (len(response.vulnerabilities) > 0)

    def test_get_by_date(self):
        response = self.client.get_cves(
            last_mod_start_date="2018-10-10T00:00:00.000",
            last_mod_end_date="2018-10-20T00:00:00.000",
            pub_start_date="2006-05-15T00:00:00.000",
            pub_end_date="2006-05-25T00:00:00.000",
            results_per_page=1,
            start_index=1
        )
        pprint(response)
        assert (len(response.vulnerabilities) > 0)

    def test_get_by_virtual_match_string(self):
        response = self.client.get_cves(
            results_per_page=1,
            start_index=1,
            virtual_match_string="cpe:2.3:*:*:*:*:*:*:de"
        )
        pprint(response)
        assert (len(response.vulnerabilities) > 0)

    def test_get_by_version_range(self):
        response = self.client.get_cves(
            virtual_match_string='cpe:2.3:o:linux:linux_kernel',
            version_start='2.2',
            version_start_type=VERSION_TYPE.INCLUDING,
            version_end='2.6',
            version_end_type=VERSION_TYPE.EXCLUDING,
            results_per_page=1,
            start_index=0,
        )
        pprint(response)
        assert (len(response.vulnerabilities) > 0)

    def test_use_mod_end_date_without_mod_start_date(self):
        with self.assertRaises(ApiValueError):
            response = self.client.get_cves(
                last_mod_end_date="2018-10-20T00:00:00.000",
                results_per_page=1,
                start_index=1
            )
            pprint(response)

    def test_use_mod_start_date_without_mod_end_date(self):
        with self.assertRaises(ApiValueError):
            response = self.client.get_cves(
                last_mod_start_date="2018-10-10T00:00:00.000",
                results_per_page=1,
                start_index=1
            )
            pprint(response)

    def test_use_pub_end_date_without_pub_start_date(self):
        with self.assertRaises(ApiValueError):
            response = self.client.get_cves(
                pub_end_date="2006-05-25T00:00:00.000",
                results_per_page=1,
                start_index=1
            )
            pprint(response)

    def test_use_pub_start_date_without_pub_end_date(self):
        with self.assertRaises(ApiValueError):
            response = self.client.get_cves(
                pub_start_date="2006-05-15T00:00:00.000",
                results_per_page=1,
                start_index=1
            )
            pprint(response)

    def test_use_cvss_v2_and_v3_metrics(self):
        with self.assertRaises(ApiValueError):
            response = self.client.get_cves(
                cpe_name="cpe:2.3:o:debian:debian_linux:3.0:*:*:*:*:*:*:*",
                cvss_v2_metrics="AV:L/AC:L/Au:N/C:C/I:C/A:C",
                cvss_v3_metrics="CVSS:3.0/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H",
                results_per_page=1,
                start_index=1
            )
            pprint(response)

    def test_use_cvss_v2_and_v3_severity(self):
        with self.assertRaises(ApiValueError):
            response = self.client.get_cves(
                cpe_name="cpe:2.3:o:debian:debian_linux:3.0:*:*:*:*:*:*:*",
                cvss_v2_severity=CVSS_V2_SEVERITY.HIGH,
                cvss_v3_severity=CVSS_V3_SEVERITY.HIGH,
                results_per_page=1,
                start_index=1
            )
            pprint(response)

    def test_use_keyword_exact_match_without_keyword_search(self):
        with self.assertRaises(ApiValueError):
            response = self.client.get_cves(
                keyword_exact_match=True,
                results_per_page=1,
                start_index=1
            )
            pprint(response)

    def test_use_is_vulnerable_without_cpe_name(self):
        with self.assertRaises(ApiValueError):
            response = self.client.get_cves(
                cve_id="CVE-2019-4227",
                cwe_id="CWE-384",
                is_vulnerable=True,
                source_identifier="nvd@nist.gov"
            )
            pprint(response)

    def test_use_version_start_without_version_start_type(self):
        with self.assertRaises(ApiValueError):
            response = self.client.get_cves(
                virtual_match_string='cpe:2.3:o:linux:linux_kernel',
                version_start='2.2',
                version_end='2.6',
                version_end_type=VERSION_TYPE.EXCLUDING,
                results_per_page=1,
                start_index=0,
            )
            pprint(response)

    def test_use_version_start_type_without_version_start(self):
        with self.assertRaises(ApiValueError):
            response = self.client.get_cves(
                virtual_match_string='cpe:2.3:o:linux:linux_kernel',
                version_start_type=VERSION_TYPE.INCLUDING,
                version_end='2.6',
                version_end_type=VERSION_TYPE.EXCLUDING,
                results_per_page=1,
                start_index=0,
            )
            pprint(response)

    def test_use_version_end_without_version_end_type(self):
        with self.assertRaises(ApiValueError):
            response = self.client.get_cves(
                virtual_match_string='cpe:2.3:o:linux:linux_kernel',
                version_start='2.2',
                version_start_type=VERSION_TYPE.INCLUDING,
                version_end='2.6',
                results_per_page=1,
                start_index=0,
            )
            pprint(response)

    def test_use_version_end_type_without_version_end(self):
        with self.assertRaises(ApiValueError):
            response = self.client.get_cves(
                virtual_match_string='cpe:2.3:o:linux:linux_kernel',
                version_start='2.2',
                version_start_type=VERSION_TYPE.INCLUDING,
                version_end_type=VERSION_TYPE.EXCLUDING,
                results_per_page=1,
                start_index=0,
            )
            pprint(response)

    def test_valid_iso_datetime_format(self):
        response = self.client.get_cves(
            last_mod_start_date="2018-10-10T00:00:00.000",
            last_mod_end_date="2018-10-20T00:00:00.000",
            pub_start_date="2006-05-15T00:00:00.000+09:00",
            pub_end_date="2006-05-25T00:00:00",
            results_per_page=1,
            start_index=1
        )
        pprint(response)
        assert (len(response.vulnerabilities) > 0)

    def test_invalid_cpe_name(self):
        with self.assertRaises(NotFoundException):
            response = self.client.get_cves(
                cpe_name="INVALID:2.3:a:ibm:mq:9.0.0.0:*:*:*:lts:*:*:*",
                is_vulnerable=True
            )
            pprint(response)

    def test_invalid_cve_id(self):
        with self.assertRaises(ApiValueError):
            response = self.client.get_cves(
                cpe_name="cpe:2.3:a:ibm:mq:9.0.0.0:*:*:*:lts:*:*:*",
                cve_id="INVALID-2019-4227",
                cwe_id="CWE-384",
                is_vulnerable=True,
                source_identifier="nvd@nist.gov"
            )
            pprint(response)

    def test_invalid_cvss_v2_metrics(self):
        with self.assertRaises(ApiValueError):
            response = self.client.get_cves(
                cpe_name="cpe:2.3:o:debian:debian_linux:3.0:*:*:*:*:*:*:*",
                cvss_v2_metrics="INVALID:L/AC:L/Au:N/C:C/I:C/A:C",
                cvss_v2_severity=CVSS_V2_SEVERITY.HIGH,
                results_per_page=1,
                start_index=1
            )
            pprint(response)

    def test_invalid_cvss_v2_severity(self):
        with self.assertRaises(ApiValueError):
            response = self.client.get_cves(
                cpe_name="cpe:2.3:o:debian:debian_linux:3.0:*:*:*:*:*:*:*",
                cvss_v2_metrics="AV:L/AC:L/Au:N/C:C/I:C/A:C",
                cvss_v2_severity="INVALID",
                results_per_page=1,
                start_index=1
            )
            pprint(response)

    def test_invalid_cvss_v3_metrics(self):
        with self.assertRaises(ApiValueError):
            response = self.client.get_cves(
                cpe_name="cpe:2.3:o:debian:debian_linux:3.0:*:*:*:*:*:*:*",
                cvss_v3_metrics="INVALID:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H",
                cvss_v3_severity=CVSS_V3_SEVERITY.HIGH,
                results_per_page=1,
                start_index=0
            )
            pprint(response)

    def test_invalid_cvss_v3_severity(self):
        with self.assertRaises(ApiValueError):
            response = self.client.get_cves(
                cpe_name="cpe:2.3:o:debian:debian_linux:3.0:*:*:*:*:*:*:*",
                cvss_v3_metrics="AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H",
                cvss_v3_severity="INVALID",
                results_per_page=1,
                start_index=0
            )
            pprint(response)

    def test_invalid_cwe_id(self):
        with self.assertRaises(ApiValueError):
            response = self.client.get_cves(
                cpe_name="cpe:2.3:a:ibm:mq:9.0.0.0:*:*:*:lts:*:*:*",
                cve_id="CVE-2019-4227",
                cwe_id="INVALID-384",
                is_vulnerable=True,
                source_identifier="nvd@nist.gov"
            )
            pprint(response)

    def test_invalid_last_mod_start_date(self):
        with self.assertRaises(ApiValueError):
            response = self.client.get_cves(
                last_mod_start_date="invalid datetime",
                last_mod_end_date="2018-10-20T00:00:00.000",
                results_per_page=1,
                start_index=1
            )
            pprint(response)

    def test_invalid_last_mod_end_date(self):
        with self.assertRaises(ApiValueError):
            response = self.client.get_cves(
                last_mod_start_date="2018-10-10T00:00:00.000",
                last_mod_end_date="invalid datetime",
                results_per_page=1,
                start_index=1
            )
            pprint(response)

    def test_invalid_last_mod_date_range(self):
        with self.assertRaises(ApiValueError):
            response = self.client.get_cves(
                last_mod_start_date="2018-12-01T00:00:00.000",
                last_mod_end_date="2019-04-01T00:00:00.000",  # 121 days
                results_per_page=1,
                start_index=1
            )
            pprint(response)

    def test_invalid_pub_start_date(self):
        with self.assertRaises(ApiValueError):
            response = self.client.get_cves(
                pub_start_date="invalid datetime",
                pub_end_date="2006-05-25T00:00:00.000",
                results_per_page=1,
                start_index=1
            )
            pprint(response)

    def test_invalid_pub_end_date(self):
        with self.assertRaises(ApiValueError):
            response = self.client.get_cves(
                pub_start_date="2006-05-15T00:00:00.000",
                pub_end_date="invalid datetime",
                results_per_page=1,
                start_index=1
            )
            pprint(response)

    def test_invalid_pub_date_range(self):
        with self.assertRaises(ApiValueError):
            response = self.client.get_cves(
                pub_start_date="2018-12-01T00:00:00.000",
                pub_end_date="2019-04-01T00:00:00.000",  # 121 days
                results_per_page=1,
                start_index=1
            )
            pprint(response)

    def test_invalid_virtual_match_string(self):
        with self.assertRaises(NotFoundException):
            response = self.client.get_cves(
                results_per_page=1,
                start_index=1,
                virtual_match_string="INVALID:2.3:*:*:*:*:*:*:de"
            )
            pprint(response)

    def test_invalid_results_per_page(self):
        with self.assertRaises(ApiValueError):
            response = self.client.get_cves(
                cpe_name="cpe:2.3:o:debian:debian_linux:3.0:*:*:*:*:*:*:*",
                cvss_v2_metrics="AV:L/AC:L/Au:N/C:C/I:C/A:C",
                cvss_v2_severity=CVSS_V2_SEVERITY.HIGH,
                results_per_page=2001,
                start_index=1
            )
            pprint(response)

        with self.assertRaises(ApiValueError):
            response = self.client.get_cves(
                cpe_name="cpe:2.3:o:debian:debian_linux:3.0:*:*:*:*:*:*:*",
                cvss_v2_metrics="AV:L/AC:L/Au:N/C:C/I:C/A:C",
                cvss_v2_severity=CVSS_V2_SEVERITY.HIGH,
                results_per_page=-1,
                start_index=1
            )
            pprint(response)

    def test_invalid_start_index(self):
        with self.assertRaises(ApiValueError):
            response = self.client.get_cves(
                cpe_name="cpe:2.3:o:debian:debian_linux:3.0:*:*:*:*:*:*:*",
                cvss_v2_metrics="AV:L/AC:L/Au:N/C:C/I:C/A:C",
                cvss_v2_severity=CVSS_V2_SEVERITY.HIGH,
                results_per_page=1,
                start_index=-1
            )
            pprint(response)

    def test_invalid_api_key(self):
        with self.assertRaises(NotFoundException):
            client = NvdApiClient(wait_time=15 * 1000, api_key='invalid key')
            response = client.get_cves(
                cpe_name="cpe:2.3:a:ibm:mq:9.0.0.0:*:*:*:lts:*:*:*",
                cve_id="CVE-2019-4227",
                cwe_id="CWE-384",
                is_vulnerable=True,
                source_identifier="nvd@nist.gov"
            )
            pprint(response)

    def test_max_page_limit(self):
        max_limit = NvdApiClient.MAX_PAGE_LIMIT_CVE_API
        response = self.client.get_cves(results_per_page=max_limit)
        assert (len(response.vulnerabilities) > 0)

        with self.assertRaises(ApiValueError):
            response = self.client.get_cves(
                results_per_page=max_limit + 1)


if __name__ == '__main__':
    unittest.main()
