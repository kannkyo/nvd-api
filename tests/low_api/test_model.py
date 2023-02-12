import unittest
from datetime import datetime
from pprint import pprint

from nvd_api.low_api.models import (
    CveOas, CveOasVulnerabilitiesInner, CveOasVulnerabilitiesInnerCve,
    CveOasVulnerabilitiesInnerCveDescriptionsInner,
    CveOasVulnerabilitiesInnerCveReferencesInner)


class TestModel(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_cve_model(self):
        references = [CveOasVulnerabilitiesInnerCveReferencesInner(
            url="http://hoge.com")]
        descriptions = [CveOasVulnerabilitiesInnerCveDescriptionsInner(
            lang="en",
            value="hogehoge")]
        cve = CveOasVulnerabilitiesInnerCve(
            published=datetime.now(),
            id="CVE-2022-1234",
            last_modified=datetime.now(),
            descriptions=descriptions,
            references=references)
        vulnerabilities = [CveOasVulnerabilitiesInner(cve=cve)]
        cve = CveOas(results_per_page=1,
                     start_index=2,
                     total_results=3,
                     format="a",
                     version="b",
                     vulnerabilities=vulnerabilities,
                     timestamp=datetime.now())
        assert (cve is not None)
