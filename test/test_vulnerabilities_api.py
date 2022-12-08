"""
    NVD API 2.0 Python API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Contact: 15080890+kannkyo@users.noreply.github.com
    Generated by: https://openapi-generator.tech
"""


from time import sleep
import unittest

import nvd_api
from nvd_api.api.vulnerabilities_api import VulnerabilitiesApi  # noqa: E501
from pprint import pprint


class TestVulnerabilitiesApi(unittest.TestCase):
    """VulnerabilitiesApi unit test stubs"""

    def setUp(self):
        self.api = VulnerabilitiesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_cve_history(self):
        """Test case for get_cve_history

        CVE Change History API  # noqa: E501
        """
        pass

    def test_get_cves_by_cve(self):
        """Test case for get_cves

        CVE API  # noqa: E501
        """
        try:
            response = self.api.get_cves(
                cpe_name="cpe:2.3:a:ibm:mq:9.0.0.0:*:*:*:lts:*:*:*",
                cve_id="CVE-2019-4227",
                # cvss_v2_metrics="AV:L/AC:L/Au:N/C:C/I:C/A:C",
                # cvss_v2_severity="HIGH",
                # cvss_v3_metrics="",
                # cvss_v3_severity="HIGH",
                cwe_id="CWE-384",
                # has_cert_alerts="",
                # has_cert_notes="",
                # has_kev="",
                # has_oval="",
                # is_vulnerable="",
                # keyword_exact_match="",
                # keyword_search="",
                # last_mod_start_date="",
                # last_mod_end_date="",
                # pub_start_date="",
                # pub_end_date="",
                # results_per_page=1,
                # start_index=1,
                # source_identifier="",
                # virtual_match_string=""
            )
            sleep(5)
            pprint(response)
            assert(len(response.vulnerabilities) > 0)
        except nvd_api.ApiException as e:
            print("Exception: %s\n" % e)

    def test_get_cves_by_cvss_v2(self):
        """Test case for get_cves

        CVE API  # noqa: E501
        """
        try:
            response = self.api.get_cves(
                cpe_name="cpe:2.3:o:debian:debian_linux:3.0:*:*:*:*:*:*:*",
                # cve_id="CVE-1999-1572",
                cvss_v2_metrics="AV:L/AC:L/Au:N/C:C/I:C/A:C",
                cvss_v2_severity="HIGH",
                # cvss_v3_metrics="",
                # cvss_v3_severity="HIGH",
                # cwe_id="CWE-384",
                # has_cert_alerts="",
                # has_cert_notes="",
                # has_kev="",
                # has_oval="",
                # is_vulnerable="",
                # keyword_exact_match="",
                # keyword_search="",
                # last_mod_start_date="",
                # last_mod_end_date="",
                # pub_start_date="",
                # pub_end_date="",
                results_per_page=1,
                start_index=1,
                # source_identifier="",
                # virtual_match_string=""
            )
            sleep(5)
            pprint(response)
            assert(len(response.vulnerabilities) > 0)
        except nvd_api.ApiException as e:
            print("Exception: %s\n" % e)

    def test_get_cves_by_cvss_v3(self):
        """Test case for get_cves

        CVE API  # noqa: E501
        """
        try:
            response = self.api.get_cves(
                cpe_name="cpe:2.3:o:debian:debian_linux:3.0:*:*:*:*:*:*:*",
                # cve_id="CVE-1999-1572",
                # cvss_v2_metrics="",
                # cvss_v2_severity="",
                cvss_v3_metrics="CVSS:3.0/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H",
                cvss_v3_severity="HIGH",
                # cwe_id="CWE-384",
                # has_cert_alerts="",
                # has_cert_notes="",
                # has_kev="",
                # has_oval="",
                # is_vulnerable="",
                # keyword_exact_match="",
                # keyword_search="",
                # last_mod_start_date="",
                # last_mod_end_date="",
                # pub_start_date="",
                # pub_end_date="",
                results_per_page=1,
                start_index=1,
                # source_identifier="",
                # virtual_match_string=""
            )
            sleep(5)
            pprint(response)
            assert(len(response.vulnerabilities) > 0)
        except nvd_api.ApiException as e:
            print("Exception: %s\n" % e)

    def test_get_cves_by_date(self):
        """Test case for get_cves

        CVE API  # noqa: E501
        """
        try:
            response = self.api.get_cves(
                # cpe_name="cpe:2.3:a:phpbb_group:phpbb:*:*:*:*:*:*:*:*",
                # cve_id="CVE-2006-2360",
                # cvss_v2_metrics="",
                # cvss_v2_severity="",
                # cvss_v3_metrics="",
                # cvss_v3_severity="MEDIUM",
                # cwe_id="CWE-384",

                # 後で追加
                # has_cert_alerts="",
                # has_cert_notes="",
                # has_kev="",
                # has_oval="",

                # is_vulnerable="",
                # keyword_exact_match="",
                # keyword_search="",
                last_mod_start_date="2018-10-10T00:00:00.000",
                last_mod_end_date="2018-10-20T00:00:00.000",
                pub_start_date="2006-05-15T00:00:00.000",
                pub_end_date="2006-05-25T00:00:00.000",
                results_per_page=1,
                start_index=1,
                # source_identifier="",
                # virtual_match_string=""
            )
            sleep(5)
            pprint(response)
            assert(len(response.vulnerabilities) > 0)
        except nvd_api.ApiException as e:
            print("Exception: %s\n" % e)


if __name__ == '__main__':
    unittest.main()
