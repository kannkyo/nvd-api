import unittest
from datetime import datetime

from nvd_api.low_api.models import (
    CpeMatchOas, CpeMatchOasMatchStringsInner,
    CpeMatchOasMatchStringsInnerMatchString,
    CpeMatchOasMatchStringsInnerMatchStringMatchesInner, CpeOas,
    CpeOasProductsInner, CpeOasProductsInnerCpe,
    CpeOasProductsInnerCpeTitlesInner, CveHistoryOas,
    CveHistoryOasCveChangesInner, CveHistoryOasCveChangesInnerChange,
    CveHistoryOasCveChangesInnerChangeDetailsInner, CveOas,
    CveOasVulnerabilitiesInner, CveOasVulnerabilitiesInnerCve,
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
            id="CVE-2022-1234",
            published=datetime.now(),
            last_modified=datetime.now(),
            descriptions=descriptions,
            references=references)
        vulnerabilities = [CveOasVulnerabilitiesInner(cve=cve)]
        cve = CveOas(results_per_page=1,
                     start_index=2,
                     total_results=3,
                     format="a",
                     version="b",
                     timestamp=datetime.now(),
                     vulnerabilities=vulnerabilities)
        assert (cve is not None)

    def test_cve_model_using_args(self):
        references = [CveOasVulnerabilitiesInnerCveReferencesInner(
            "http://hoge.com")]
        descriptions = [CveOasVulnerabilitiesInnerCveDescriptionsInner(
            "en",
            "hogehoge")]
        cve = CveOasVulnerabilitiesInnerCve(
            "CVE-2022-1234",
            datetime.now(),
            datetime.now(),
            descriptions,
            references)
        vulnerabilities = [CveOasVulnerabilitiesInner(cve=cve)]
        cve = CveOas(1, 2, 3, "a", "b", datetime.now(), vulnerabilities)
        assert (cve is not None)

    def test_cve_history_model(self):
        details = [CveHistoryOasCveChangesInnerChangeDetailsInner(
            type="CVSS V2",
            action="Added",
            new_value="(AV:N/AC:L/Au:N/C:N/I:N/A:P)"
        )]
        change = CveHistoryOasCveChangesInnerChange(
            cve_id="CVE-2019-1010218",
            event_name="Initial Analysis",
            cve_change_id="E52AFC66-FAFE-4393-B7FF-4EC2FA6CB6C4",
            source_identifier="nvd@nist.gov",
            created=datetime.now(),
            details=details
        )
        cve_changes = [CveHistoryOasCveChangesInner(change=change)]
        cve_history = CveHistoryOas(results_per_page=1,
                                    start_index=2,
                                    total_results=3,
                                    format="a",
                                    version="b",
                                    timestamp=datetime.now(),
                                    cve_changes=cve_changes)
        assert (cve_history is not None)

    def test_cpe_model(self):
        titles = [CpeOasProductsInnerCpeTitlesInner("Microsoft Access", "en")]
        cpe = CpeOasProductsInnerCpe(
            deprecated=False,
            cpe_name="cpe:2.3:a:microsoft:access:-:*:*:*:*:*:*:*",
            cpe_name_id="87316812-5F2C-4286-94FE-CC98B9EAEF53",
            last_modified=datetime(2011, 1, 12, 14, 35, 56, 427000),
            created=datetime(2007, 8, 23, 21, 5, 57, 937000),
            titles=titles
        )
        products = [CpeOasProductsInner(cpe=cpe)]
        cpe = CpeOas(results_per_page=1,
                     start_index=2,
                     total_results=3,
                     format="a",
                     version="b",
                     timestamp=datetime.now(),
                     products=products)
        assert (cpe is not None)

    def test_cpe_match_model(self):
        matches = [CpeMatchOasMatchStringsInnerMatchStringMatchesInner(
            cpe_name="cpe:2.3:o:microsoft:windows:-:*:*:*:*:*:*:*",
            cpe_name_id="32D33F53-B7FC-4674-BD03-299D70A278F3"
        )]
        match_string = CpeMatchOasMatchStringsInnerMatchString(
            match_criteria_id="A2572D17-1DE6-457B-99CC-64AFD54487EA",
            criteria="cpe:2.3:o:microsoft:windows:-:*:*:*:*:*:*:*",
            last_modified=datetime(2022, 9, 26, 22, 47, 53, 533000),
            cpe_last_modified=datetime(2021, 3, 3, 22, 41, 34, 363000),
            created=datetime(2019, 6, 17, 9, 16, 33, 960000),
            status="Active",
            matches=matches
        )
        match_strings = [CpeMatchOasMatchStringsInner(
            match_string=match_string)]
        cpe_match = CpeMatchOas(results_per_page=1,
                                start_index=2,
                                total_results=3,
                                format="a",
                                version="b",
                                timestamp=datetime.now(),
                                match_strings=match_strings)
        assert (cpe_match is not None)
