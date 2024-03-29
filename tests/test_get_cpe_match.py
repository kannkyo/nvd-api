"""
    NVD API 2.0 Python API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Contact: 15080890+kannkyo@users.noreply.github.com
    Generated by: https://openapi-generator.tech
"""


import os
import unittest
from datetime import datetime
from pprint import pprint

from nvd_api.client import NvdApiClient
from nvd_api.low_api.exceptions import ApiValueError, NotFoundException
from nvd_api.low_api.models import CpeMatchOasMatchStringsInnerMatchString


class TestGetCpeMatch(unittest.TestCase):
    def setUp(self):
        api_key = os.getenv('NVD_API_KEY')
        if api_key:
            self.client = NvdApiClient(wait_time=1 * 1000, api_key=api_key)  # noqa: E501
        else:
            self.client = NvdApiClient(wait_time=10 * 1000)  # noqa: E501

    def tearDown(self):
        pass

    def test_get_by_cve_id(self):
        response = self.client.get_cpe_match(
            cve_id="CVE-2022-32223",
            results_per_page=1,
            start_index=0
        )
        pprint(response)

        assert response.results_per_page == 1
        assert response.start_index == 0
        assert response.total_results == 6
        assert response.format == 'NVD_CPEMatchString'
        assert response.version == '2.0'
        assert response.timestamp is not None

        assert (len(response.match_strings) > 0)

        cpe_match: CpeMatchOasMatchStringsInnerMatchString = response.match_strings[0].match_string  # noqa

        assert cpe_match.match_criteria_id == "A2572D17-1DE6-457B-99CC-64AFD54487EA"  # noqa
        assert cpe_match.criteria == "cpe:2.3:o:microsoft:windows:-:*:*:*:*:*:*:*"  # noqa
        assert cpe_match.last_modified == datetime(2022, 9, 26, 22, 47, 53, 533000)  # noqa
        assert cpe_match.cpe_last_modified == datetime(2021, 3, 3, 22, 41, 34, 363000)  # noqa
        assert cpe_match.created == datetime(2019, 6, 17, 9, 16, 33, 960000)  # noqa
        assert cpe_match.status == "Active"
        assert cpe_match.matches[0].cpe_name == "cpe:2.3:o:microsoft:windows:-:*:*:*:*:*:*:*"  # noqa
        assert cpe_match.matches[0].cpe_name_id == "32D33F53-B7FC-4674-BD03-299D70A278F3"  # noqa
        assert cpe_match.matches[1].cpe_name == "cpe:2.3:o:microsoft:windows:-:*:*:*:*:*:x64:*"  # noqa
        assert cpe_match.matches[1].cpe_name_id == "2470AF67-0E77-4E85-92E8-79DE0D826055"  # noqa
        assert cpe_match.matches[2].cpe_name == "cpe:2.3:o:microsoft:windows:-:*:*:*:*:*:x86:*"  # noqa
        assert cpe_match.matches[2].cpe_name_id == "892CAEC7-9569-4385-8335-239B83D58837"  # noqa

    def test_get_all_cpe_match(self):
        response = self.client.get_all_cpe_match(
            last_mod_start_date="2021-01-01T00:00:00.000",
            last_mod_end_date="2021-03-01T00:00:00.000"
        )
        assert (len(response.match_strings) > 5000)

    def test_get_by_date(self):
        response = self.client.get_cpe_match(
            last_mod_start_date="2021-08-04T13:00:00.000",
            last_mod_end_date="2021-10-22T13:36:00.000",
            results_per_page=1,
            start_index=0
        )
        assert (len(response.match_strings) > 0)

    def test_get_by_match_criteria_id(self):
        response = self.client.get_cpe_match(
            match_criteria_id="36FBCF0F-8CEE-474C-8A04-5075AF53FAF4",
            results_per_page=1,
            start_index=0
        )
        pprint(response)
        assert (len(response.match_strings) > 0)

    def test_use_mod_end_date_without_mod_start_date(self):
        with self.assertRaises(ApiValueError):
            response = self.client.get_cpe_match(
                last_mod_end_date="2018-10-20T00:00:00.000"
            )
            pprint(response)

    def test_use_mod_start_date_without_mod_end_date(self):
        with self.assertRaises(ApiValueError):
            response = self.client.get_cpe_match(
                last_mod_start_date="2018-10-10T00:00:00.000"
            )
            pprint(response)

    def test_invalid_cve_id(self):
        with self.assertRaises(ApiValueError):
            response = self.client.get_cpe_match(
                cve_id="INVALID-2022-32223",
                results_per_page=1,
                start_index=0
            )
            pprint(response)

    def test_invalid_last_mod_start_date(self):
        with self.assertRaises(ApiValueError):
            response = self.client.get_cpe_match(
                last_mod_start_date="invalid datetime",
                last_mod_end_date="2021-10-22T13:36:00.000",
                results_per_page=1,
                start_index=0
            )
            pprint(response)

    def test_invalid_last_mod_end_date(self):
        with self.assertRaises(ApiValueError):
            response = self.client.get_cpe_match(
                last_mod_start_date="2021-08-04T13:00:00.000",
                last_mod_end_date="invalid datetime",
                results_per_page=1,
                start_index=0
            )
            pprint(response)

    def test_invalid_last_mod_date_range(self):
        with self.assertRaises(ApiValueError):
            response = self.client.get_cpe_match(
                last_mod_start_date="2018-12-01T00:00:00.000",
                last_mod_end_date="2019-04-01T00:00:00.000",  # 121 days
                results_per_page=1,
                start_index=1
            )
            pprint(response)

    def test_invalid_match_criteria_id(self):
        with self.assertRaises(NotFoundException):
            response = self.client.get_cpe_match(
                match_criteria_id="INVALID-8CEE-474C-8A04-5075AF53FAF4",
                results_per_page=1,
                start_index=0
            )
            pprint(response)

    def test_invalid_results_per_page(self):
        with self.assertRaises(ApiValueError):
            response = self.client.get_cpe_match(
                cve_id="CVE-2022-32223",
                results_per_page=5001,
                start_index=0
            )
            pprint(response)

        with self.assertRaises(ApiValueError):
            response = self.client.get_cpe_match(
                cve_id="CVE-2022-32223",
                results_per_page=-1,
                start_index=0
            )
            pprint(response)

    def test_invalid_start_index(self):
        with self.assertRaises(ApiValueError):
            response = self.client.get_cpe_match(
                cve_id="CVE-2022-32223",
                results_per_page=1,
                start_index=-1
            )
            pprint(response)

    def test_invalid_api_key(self):
        with self.assertRaises(NotFoundException):
            client = NvdApiClient(wait_time=15 * 1000, api_key='invalid key')
            response = client.get_cpe_match(
                cve_id="CVE-2022-32223",
                results_per_page=1,
                start_index=0
            )
            pprint(response)

    def test_max_page_limit(self):
        max_limit = NvdApiClient.MAX_PAGE_LIMIT_CPE_MATCH_API
        response = self.client.get_cpe_match(results_per_page=max_limit)
        assert (len(response.match_strings) > 0)

        with self.assertRaises(ApiValueError):
            response = self.client.get_cpe_match(
                results_per_page=max_limit + 1)


if __name__ == '__main__':
    unittest.main()
