import time
import unittest
from pprint import pprint

from nvd_api.low_api.api.vulnerabilities_api import VulnerabilitiesApi


class TestVulnerabilitiesApi(unittest.TestCase):
    def setUp(self):
        self.client = VulnerabilitiesApi()

    def tearDown(self):
        pass

    def test_client_without_configuration(self):
        time.sleep(15)
        response = self.client.get_cves(
            cve_id="CVE-2022-32223",
            results_per_page=1,
            start_index=0
        )
        pprint(response)
        assert (len(response.vulnerabilities) > 0)
        time.sleep(15)
