"""
    NVD API 2.0 Python API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Contact: 15080890+kannkyo@users.noreply.github.com
    Generated by: https://openapi-generator.tech
"""


import unittest
from datetime import datetime

from nvd_api.low_api.models import (
    CpeMatchOas, CpeMatchOasMatchStringsInner,
    CpeMatchOasMatchStringsInnerMatchString,
    CpeMatchOasMatchStringsInnerMatchStringMatchesInner)


class TestCpeMatchOas(unittest.TestCase):
    """CpeMatchOas unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_cpe_match_oas(self):
        # execute ###########################################################
        matches = [CpeMatchOasMatchStringsInnerMatchStringMatchesInner(
            cpe_name="cpe:2.3:o:microsoft:windows:-:*:*:*:*:*:*:*",
            cpe_name_id="32D33F53-B7FC-4674-BD03-299D70A278F3"
        )]
        match_string = CpeMatchOasMatchStringsInnerMatchString(
            criteria="cpe:2.3:o:microsoft:windows:-:*:*:*:*:*:*:*",
            match_criteria_id="A2572D17-1DE6-457B-99CC-64AFD54487EA",
            created=datetime(2023, 1, 2, 12, 34, 56, 789),
            last_modified=datetime(2023, 1, 2, 12, 34, 56, 789),
            status="Active",
            cpe_last_modified=datetime(2023, 1, 2, 12, 34, 56, 789),
            version_start_including="v1.0.0",
            version_end_including="v1.5.0",
            version_start_excluding="v2.0.0",
            version_end_excluding="v2.5.0",
            matches=matches
        )

        match_strings = [CpeMatchOasMatchStringsInner(
            match_string=match_string)]
        cpe_match = CpeMatchOas(
            results_per_page=1,
            start_index=2,
            total_results=3,
            format="format",
            version="version",
            timestamp=datetime(2023, 1, 2, 12, 34, 56, 789),
            match_strings=match_strings)

        # verify ###########################################################
        assert cpe_match.results_per_page == 1
        assert cpe_match.start_index == 2
        assert cpe_match.total_results == 3
        assert cpe_match.format == "format"
        assert cpe_match.version == "version"
        assert cpe_match.timestamp == datetime(2023, 1, 2, 12, 34, 56, 789)
        assert cpe_match.match_strings[0].match_string.criteria == "cpe:2.3:o:microsoft:windows:-:*:*:*:*:*:*:*"  # noqa
        assert cpe_match.match_strings[0].match_string.match_criteria_id == "A2572D17-1DE6-457B-99CC-64AFD54487EA"  # noqa
        assert cpe_match.match_strings[0].match_string.created == datetime(2023, 1, 2, 12, 34, 56, 789)  # noqa
        assert cpe_match.match_strings[0].match_string.last_modified == datetime(2023, 1, 2, 12, 34, 56, 789)  # noqa
        assert cpe_match.match_strings[0].match_string.status == "Active"  # noqa
        assert cpe_match.match_strings[0].match_string.cpe_last_modified == datetime(2023, 1, 2, 12, 34, 56, 789)  # noqa
        assert cpe_match.match_strings[0].match_string.version_start_including == "v1.0.0"  # noqa
        assert cpe_match.match_strings[0].match_string.version_end_including == "v1.5.0"  # noqa
        assert cpe_match.match_strings[0].match_string.version_start_excluding == "v2.0.0"  # noqa
        assert cpe_match.match_strings[0].match_string.version_end_excluding == "v2.5.0"  # noqa
        assert cpe_match.match_strings[0].match_string.matches[0].cpe_name == "cpe:2.3:o:microsoft:windows:-:*:*:*:*:*:*:*"  # noqa
        assert cpe_match.match_strings[0].match_string.matches[0].cpe_name_id == "32D33F53-B7FC-4674-BD03-299D70A278F3"  # noqa

    def test_cpe_match_oas_using_args(self):
        # execute ###########################################################
        matches = [CpeMatchOasMatchStringsInnerMatchStringMatchesInner(
            "cpe:2.3:o:microsoft:windows:-:*:*:*:*:*:*:*",
            "32D33F53-B7FC-4674-BD03-299D70A278F3"
        )]
        match_string = CpeMatchOasMatchStringsInnerMatchString(
            "cpe:2.3:o:microsoft:windows:-:*:*:*:*:*:*:*",
            "A2572D17-1DE6-457B-99CC-64AFD54487EA",
            datetime(2023, 1, 2, 12, 34, 56, 789),
            datetime(2023, 1, 2, 12, 34, 56, 789),
            "Active",
            cpe_last_modified=datetime(2023, 1, 2, 12, 34, 56, 789),
            version_start_including="v1.0.0",
            version_end_including="v1.5.0",
            version_start_excluding="v2.0.0",
            version_end_excluding="v2.5.0",
            matches=matches)
        match_strings = [CpeMatchOasMatchStringsInner(
            match_string)]
        cpe_match = CpeMatchOas(
            1,
            2,
            3,
            "format",
            "version",
            datetime(2023, 1, 2, 12, 34, 56, 789),
            match_strings)

        # verify ###########################################################
        assert cpe_match.results_per_page == 1
        assert cpe_match.start_index == 2
        assert cpe_match.total_results == 3
        assert cpe_match.format == "format"
        assert cpe_match.version == "version"
        assert cpe_match.timestamp == datetime(2023, 1, 2, 12, 34, 56, 789)
        assert cpe_match.match_strings[0].match_string.criteria == "cpe:2.3:o:microsoft:windows:-:*:*:*:*:*:*:*"  # noqa
        assert cpe_match.match_strings[0].match_string.match_criteria_id == "A2572D17-1DE6-457B-99CC-64AFD54487EA"  # noqa
        assert cpe_match.match_strings[0].match_string.created == datetime(2023, 1, 2, 12, 34, 56, 789)  # noqa
        assert cpe_match.match_strings[0].match_string.last_modified == datetime(2023, 1, 2, 12, 34, 56, 789)  # noqa
        assert cpe_match.match_strings[0].match_string.status == "Active"  # noqa
        assert cpe_match.match_strings[0].match_string.cpe_last_modified == datetime(2023, 1, 2, 12, 34, 56, 789)  # noqa
        assert cpe_match.match_strings[0].match_string.version_start_including == "v1.0.0"  # noqa
        assert cpe_match.match_strings[0].match_string.version_end_including == "v1.5.0"  # noqa
        assert cpe_match.match_strings[0].match_string.version_start_excluding == "v2.0.0"  # noqa
        assert cpe_match.match_strings[0].match_string.version_end_excluding == "v2.5.0"  # noqa
        assert cpe_match.match_strings[0].match_string.matches[0].cpe_name == "cpe:2.3:o:microsoft:windows:-:*:*:*:*:*:*:*"  # noqa
        assert cpe_match.match_strings[0].match_string.matches[0].cpe_name_id == "32D33F53-B7FC-4674-BD03-299D70A278F3"  # noqa


if __name__ == '__main__':
    unittest.main()
