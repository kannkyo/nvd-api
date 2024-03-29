"""
    NVD API 2.0 Python API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Contact: 15080890+kannkyo@users.noreply.github.com
    Generated by: https://openapi-generator.tech
"""


import unittest
from datetime import date, datetime

from nvd_api.low_api.models import (
    CveOas, CveOasVulnerabilitiesInner, CveOasVulnerabilitiesInnerCve,
    CveOasVulnerabilitiesInnerCveConfigurationsInner,
    CveOasVulnerabilitiesInnerCveConfigurationsInnerNodesInner,
    CveOasVulnerabilitiesInnerCveConfigurationsInnerNodesInnerCpeMatchInner,
    CveOasVulnerabilitiesInnerCveDescriptionsInner,
    CveOasVulnerabilitiesInnerCveMetrics,
    CveOasVulnerabilitiesInnerCveMetricsCvssMetricV2Inner,
    CveOasVulnerabilitiesInnerCveMetricsCvssMetricV30Inner,
    CveOasVulnerabilitiesInnerCveMetricsCvssMetricV31Inner,
    CveOasVulnerabilitiesInnerCveReferencesInner,
    CveOasVulnerabilitiesInnerCveVendorCommentsInner,
    CveOasVulnerabilitiesInnerCveWeaknessesInner,
    JSONSchemaForCommonVulnerabilityScoringSystemVersion20,
    JSONSchemaForCommonVulnerabilityScoringSystemVersion30,
    JSONSchemaForCommonVulnerabilityScoringSystemVersion31)


class TestCveOas(unittest.TestCase):
    """CveOas unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_cve_oas(self):
        # execute ###########################################################
        cpe_match = [CveOasVulnerabilitiesInnerCveConfigurationsInnerNodesInnerCpeMatchInner(  # noqa
            vulnerable=True,
            criteria="cpe:2.3:a:eric_allman:sendmail:5.58:*:*:*:*:*:*:*",
            match_criteria_id="1D07F493-9C8D-44A4-8652-F28B46CBA27C",
            version_start_including="v1.0.0",
            version_end_including="v1.5.0",
            version_start_excluding="v2.0.0",
            version_end_excluding="v2.5.0"
        )]
        configurations = [CveOasVulnerabilitiesInnerCveConfigurationsInner(
            nodes=[CveOasVulnerabilitiesInnerCveConfigurationsInnerNodesInner(
                operator="OR",
                cpe_match=cpe_match,
                negate=True
            )],
            operator="OR",
            negate=True
        )]
        descriptions = [CveOasVulnerabilitiesInnerCveDescriptionsInner(
            lang="en",
            value="this is description")]
        weaknesses = [CveOasVulnerabilitiesInnerCveWeaknessesInner(
            source="nvd@nist.gov",
            type="Primary",
            description=[CveOasVulnerabilitiesInnerCveDescriptionsInner(
                lang="en",
                value="this is weaknesses")]
        )]
        cvss_metric_v2 = [CveOasVulnerabilitiesInnerCveMetricsCvssMetricV2Inner(  # noqa
            source="nvd@nist.gov",
            type="Primary",
            cvss_data=JSONSchemaForCommonVulnerabilityScoringSystemVersion20(
                vector_string="AV:N/AC:L/Au:N/C:N/I:N/A:P",
                base_score=5.0,
                version="2.0",
                access_vector="NETWORK",
                access_complexity="LOW",
                authentication="NONE",
                availability_impact="PARTIAL",
                confidentiality_impact="NONE",
                integrity_impact="NONE",
                exploitability="UNPROVEN",
                remediation_level="OFFICIAL_FIX",
                report_confidence="UNCONFIRMED",
                temporal_score=3.5,
                collateral_damage_potential="LOW_MEDIUM",
                target_distribution="MEDIUM",
                confidentiality_requirement="NOT_DEFINED",
                integrity_requirement="MEDIUM",
                availability_requirement="NOT_DEFINED",
                environmental_score=3.5),
            base_severity="HIGH",
            exploitability_score=1.2,
            impact_score=5.1,
            ac_insuf_info=True,
            obtain_all_privilege=True,
            obtain_user_privilege=True,
            obtain_other_privilege=True,
            user_interaction_required=True,
        )]
        cvss_metric_v30 = [CveOasVulnerabilitiesInnerCveMetricsCvssMetricV30Inner(  # noqa
            source="nvd@nist.gov",
            type="Primary",
            # TODO: add all attributes https://kannkyo.github.io/nvd-api/html/_static/openapi.html#/Vulnerabilities/getCves # noqa
            cvss_data=JSONSchemaForCommonVulnerabilityScoringSystemVersion30(
                vector_string="CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H",
                base_score=7.5,
                base_severity="HIGH",
                version="3.0",
                attack_vector="NETWORK",
                attack_complexity="LOW",
                privileges_required="NONE",
                user_interaction="NONE",
                scope="UNCHANGED",
                confidentiality_impact="NONE",
                integrity_impact="NONE",
                availability_impact="HIGH",
                exploit_code_maturity="UNPROVEN",
                remediation_level="WORKAROUND",
                report_confidence="CONFIRMED",
                temporal_score=3.5,
                confidentiality_requirement="MEDIUM",
                integrity_requirement="HIGH",
                availability_requirement="LOW",
                modified_attack_vector="NETWORK",
                modified_attack_complexity="LOW",
                modified_privileges_required="NOT_DEFINED",
                modified_user_interaction="NOT_DEFINED",
                modified_scope="CHANGED",
                modified_confidentiality_impact="NONE",
                modified_integrity_impact="LOW",
                modified_availability_impact="NOT_DEFINED",
                environmental_score=3.5,
                environmental_severity="CRITICAL"),
            exploitability_score=1.2,
            impact_score=5.1
        )]
        cvss_metric_v31 = [CveOasVulnerabilitiesInnerCveMetricsCvssMetricV31Inner(  # noqa
            source="nvd@nist.gov",
            type="Primary",
            # TODO: add all attributes https://kannkyo.github.io/nvd-api/html/_static/openapi.html#/Vulnerabilities/getCves # noqa
            cvss_data=JSONSchemaForCommonVulnerabilityScoringSystemVersion31(
                vector_string="CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H",
                base_score=7.5,
                base_severity="HIGH",
                version="3.1",
                attack_vector="NETWORK",
                attack_complexity="LOW",
                privileges_required="NONE",
                user_interaction="NONE",
                scope="UNCHANGED",
                confidentiality_impact="NONE",
                integrity_impact="NONE",
                availability_impact="HIGH",
                exploit_code_maturity="UNPROVEN",
                remediation_level="WORKAROUND",
                report_confidence="CONFIRMED",
                temporal_score=3.5,
                confidentiality_requirement="MEDIUM",
                integrity_requirement="HIGH",
                availability_requirement="LOW",
                modified_attack_vector="NETWORK",
                modified_attack_complexity="LOW",
                modified_privileges_required="NOT_DEFINED",
                modified_user_interaction="NOT_DEFINED",
                modified_scope="CHANGED",
                modified_confidentiality_impact="NONE",
                modified_integrity_impact="LOW",
                modified_availability_impact="NOT_DEFINED",
                environmental_score=3.5,
                environmental_severity="CRITICAL"),
            exploitability_score=1.2,
            impact_score=5.1
        )]
        metrics = CveOasVulnerabilitiesInnerCveMetrics(
            cvss_metric_v2=cvss_metric_v2,
            cvss_metric_v30=cvss_metric_v30,
            cvss_metric_v31=cvss_metric_v31
        )
        cve = CveOasVulnerabilitiesInnerCve(
            id="CVE-2022-1234",
            published=datetime(2023, 1, 2, 12, 34, 56, 789),
            last_modified=datetime(2023, 1, 2, 12, 34, 56, 789),
            descriptions=descriptions,
            references=[CveOasVulnerabilitiesInnerCveReferencesInner(
                url="http://hoge.com",
                source="from nvd",
                tags=["Exploit", "Mailing List"])],
            source_identifier="cve@mitre.org",
            vuln_status="Analyzed",
            evaluator_comment="evaluator_comment",
            evaluator_solution="evaluator_solution",
            evaluator_impact="evaluator_impact",
            cisa_exploit_add=date(2023, 1, 2),
            cisa_action_due=date(2023, 1, 2),
            cisa_required_action="Apply updates per vendor instructions.",
            cisa_vulnerability_name="Exchange Server Server-Side Request Forgery Vulnerability",  # noqa
            vendor_comments=[CveOasVulnerabilitiesInnerCveVendorCommentsInner(
                organization="Red Hat",
                comment="Not vulnerable.",
                last_modified=datetime(2023, 1, 2, 12, 34, 56, 789))],
            configurations=configurations,
            weaknesses=weaknesses,
            metrics=metrics)
        vulnerabilities = [CveOasVulnerabilitiesInner(cve=cve)]
        cve = CveOas(
            results_per_page=1,
            start_index=2,
            total_results=3,
            format="format",
            version="version",
            timestamp=datetime(2023, 1, 2, 12, 34, 56, 789),
            vulnerabilities=vulnerabilities)

        # verify ###########################################################
        assert cve.results_per_page == 1
        assert cve.start_index == 2
        assert cve.total_results == 3
        assert cve.format == "format"
        assert cve.version == "version"
        assert cve.timestamp == datetime(2023, 1, 2, 12, 34, 56, 789)
        assert cve.vulnerabilities[0].cve.id == "CVE-2022-1234"
        assert cve.vulnerabilities[0].cve.published == datetime(2023, 1, 2, 12, 34, 56, 789)  # noqa
        assert cve.vulnerabilities[0].cve.last_modified == datetime(2023, 1, 2, 12, 34, 56, 789)  # noqa
        assert cve.vulnerabilities[0].cve.source_identifier == "cve@mitre.org"
        assert cve.vulnerabilities[0].cve.vuln_status == "Analyzed"
        assert cve.vulnerabilities[0].cve.evaluator_comment == "evaluator_comment"  # noqa
        assert cve.vulnerabilities[0].cve.evaluator_solution == "evaluator_solution"  # noqa
        assert cve.vulnerabilities[0].cve.evaluator_impact == "evaluator_impact"  # noqa
        assert cve.vulnerabilities[0].cve.cisa_exploit_add == date(2023, 1, 2)
        assert cve.vulnerabilities[0].cve.cisa_action_due == date(2023, 1, 2)
        assert cve.vulnerabilities[0].cve.cisa_required_action == "Apply updates per vendor instructions."  # noqa
        assert cve.vulnerabilities[0].cve.cisa_vulnerability_name == "Exchange Server Server-Side Request Forgery Vulnerability"  # noqa
        assert cve.vulnerabilities[0].cve.descriptions[0].lang == "en"
        assert cve.vulnerabilities[0].cve.descriptions[0].value == "this is description"  # noqa
        assert cve.vulnerabilities[0].cve.vendor_comments[0].organization == "Red Hat"  # noqa
        assert cve.vulnerabilities[0].cve.vendor_comments[0].comment == "Not vulnerable."  # noqa
        assert cve.vulnerabilities[0].cve.vendor_comments[0].last_modified == datetime(2023, 1, 2, 12, 34, 56, 789)  # noqa
        assert cve.vulnerabilities[0].cve.weaknesses[0].source == "nvd@nist.gov"  # noqa
        assert cve.vulnerabilities[0].cve.weaknesses[0].type == "Primary"  # noqa
        assert cve.vulnerabilities[0].cve.weaknesses[0].description[0].lang == "en"  # noqa
        assert cve.vulnerabilities[0].cve.weaknesses[0].description[0].value == "this is weaknesses"  # noqa
        assert cve.vulnerabilities[0].cve.references[0].url == "http://hoge.com"  # noqa
        assert cve.vulnerabilities[0].cve.references[0].source == "from nvd"  # noqa
        assert cve.vulnerabilities[0].cve.references[0].tags == ["Exploit", "Mailing List"]  # noqa
        assert cve.vulnerabilities[0].cve.configurations[0].operator == "OR"  # noqa
        assert cve.vulnerabilities[0].cve.configurations[0].negate is True  # noqa
        assert cve.vulnerabilities[0].cve.configurations[0].nodes[0].operator == "OR"  # noqa
        assert cve.vulnerabilities[0].cve.configurations[0].nodes[0].negate is True  # noqa
        assert cve.vulnerabilities[0].cve.configurations[0].nodes[0].cpe_match[0].vulnerable == True  # noqa
        assert cve.vulnerabilities[0].cve.configurations[0].nodes[0].cpe_match[0].criteria == "cpe:2.3:a:eric_allman:sendmail:5.58:*:*:*:*:*:*:*"  # noqa
        assert cve.vulnerabilities[0].cve.configurations[0].nodes[0].cpe_match[0].match_criteria_id == "1D07F493-9C8D-44A4-8652-F28B46CBA27C"  # noqa
        assert cve.vulnerabilities[0].cve.configurations[0].nodes[0].cpe_match[0].version_start_including == "v1.0.0"  # noqa
        assert cve.vulnerabilities[0].cve.configurations[0].nodes[0].cpe_match[0].version_end_including == "v1.5.0"  # noqa
        assert cve.vulnerabilities[0].cve.configurations[0].nodes[0].cpe_match[0].version_start_excluding == "v2.0.0"  # noqa
        assert cve.vulnerabilities[0].cve.configurations[0].nodes[0].cpe_match[0].version_end_excluding == "v2.5.0"  # noqa

        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v2[0].source == "nvd@nist.gov"  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v2[0].type == "Primary"  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v2[0].cvss_data.vector_string == "AV:N/AC:L/Au:N/C:N/I:N/A:P"  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v2[0].cvss_data.base_score == 5.0  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v2[0].cvss_data.version == "2.0"  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v2[0].cvss_data.access_vector == "NETWORK"  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v2[0].cvss_data.access_complexity == "LOW"  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v2[0].cvss_data.authentication == "NONE"  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v2[0].cvss_data.availability_impact == "PARTIAL"  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v2[0].cvss_data.confidentiality_impact == "NONE"  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v2[0].cvss_data.integrity_impact == "NONE"  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v2[0].cvss_data.exploitability == "UNPROVEN"  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v2[0].cvss_data.remediation_level == "OFFICIAL_FIX"  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v2[0].cvss_data.report_confidence == "UNCONFIRMED"  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v2[0].cvss_data.temporal_score == 3.5  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v2[0].cvss_data.collateral_damage_potential == "LOW_MEDIUM"  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v2[0].cvss_data.target_distribution == "MEDIUM"  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v2[0].cvss_data.confidentiality_requirement == "NOT_DEFINED"  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v2[0].cvss_data.integrity_requirement == "MEDIUM"  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v2[0].cvss_data.availability_requirement == "NOT_DEFINED"  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v2[0].cvss_data.environmental_score == 3.5  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v2[0].base_severity == "HIGH"  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v2[0].exploitability_score == 1.2  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v2[0].impact_score == 5.1  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v2[0].ac_insuf_info is True  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v2[0].obtain_all_privilege is True  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v2[0].obtain_user_privilege is True  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v2[0].obtain_other_privilege is True  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v2[0].user_interaction_required is True  # noqa

        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v30[0].source == "nvd@nist.gov"  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v30[0].type == "Primary"  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v30[0].cvss_data.vector_string == "CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H"  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v30[0].cvss_data.base_score == 7.5  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v30[0].cvss_data.base_severity == "HIGH"  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v30[0].cvss_data.version == "3.0"  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v30[0].cvss_data.attack_vector == "NETWORK"  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v30[0].cvss_data.attack_complexity == "LOW"  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v30[0].cvss_data.privileges_required == "NONE"  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v30[0].cvss_data.user_interaction == "NONE"  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v30[0].cvss_data.scope == "UNCHANGED"  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v30[0].cvss_data.confidentiality_impact == "NONE"  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v30[0].cvss_data.integrity_impact == "NONE"  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v30[0].cvss_data.availability_impact == "HIGH"  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v30[0].cvss_data.exploit_code_maturity == "UNPROVEN"  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v30[0].cvss_data.remediation_level == "WORKAROUND"  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v30[0].cvss_data.report_confidence == "CONFIRMED"  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v30[0].cvss_data.temporal_score == 3.5  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v30[0].cvss_data.confidentiality_requirement == "MEDIUM"  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v30[0].cvss_data.integrity_requirement == "HIGH"  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v30[0].cvss_data.availability_requirement == "LOW"  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v30[0].cvss_data.modified_attack_vector == "NETWORK"  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v30[0].cvss_data.modified_attack_complexity == "LOW"  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v30[0].cvss_data.modified_privileges_required == "NOT_DEFINED"  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v30[0].cvss_data.modified_user_interaction == "NOT_DEFINED"  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v30[0].cvss_data.modified_scope == "CHANGED"  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v30[0].cvss_data.modified_confidentiality_impact == "NONE"  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v30[0].cvss_data.modified_integrity_impact == "LOW"  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v30[0].cvss_data.modified_availability_impact == "NOT_DEFINED"  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v30[0].cvss_data.environmental_score == 3.5  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v30[0].cvss_data.environmental_severity == "CRITICAL"  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v30[0].exploitability_score == 1.2  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v30[0].impact_score == 5.1  # noqa

        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v31[0].source == "nvd@nist.gov"  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v31[0].type == "Primary"  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v31[0].cvss_data.vector_string == "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H"  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v31[0].cvss_data.base_score == 7.5  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v31[0].cvss_data.base_severity == "HIGH"  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v31[0].cvss_data.version == "3.1"  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v31[0].cvss_data.attack_vector == "NETWORK"  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v31[0].cvss_data.attack_complexity == "LOW"  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v31[0].cvss_data.privileges_required == "NONE"  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v31[0].cvss_data.user_interaction == "NONE"  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v31[0].cvss_data.scope == "UNCHANGED"  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v31[0].cvss_data.confidentiality_impact == "NONE"  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v31[0].cvss_data.integrity_impact == "NONE"  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v31[0].cvss_data.availability_impact == "HIGH"  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v31[0].cvss_data.exploit_code_maturity == "UNPROVEN"  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v31[0].cvss_data.remediation_level == "WORKAROUND"  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v31[0].cvss_data.report_confidence == "CONFIRMED"  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v31[0].cvss_data.temporal_score == 3.5  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v31[0].cvss_data.confidentiality_requirement == "MEDIUM"  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v31[0].cvss_data.integrity_requirement == "HIGH"  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v31[0].cvss_data.availability_requirement == "LOW"  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v31[0].cvss_data.modified_attack_vector == "NETWORK"  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v31[0].cvss_data.modified_attack_complexity == "LOW"  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v31[0].cvss_data.modified_privileges_required == "NOT_DEFINED"  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v31[0].cvss_data.modified_user_interaction == "NOT_DEFINED"  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v31[0].cvss_data.modified_scope == "CHANGED"  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v31[0].cvss_data.modified_confidentiality_impact == "NONE"  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v31[0].cvss_data.modified_integrity_impact == "LOW"  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v31[0].cvss_data.modified_availability_impact == "NOT_DEFINED"  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v31[0].cvss_data.environmental_score == 3.5  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v31[0].cvss_data.environmental_severity == "CRITICAL"  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v31[0].exploitability_score == 1.2  # noqa
        assert cve.vulnerabilities[0].cve.metrics.cvss_metric_v31[0].impact_score == 5.1  # noqa


if __name__ == '__main__':
    unittest.main()
