from nvd_api.api.vulnerabilities_api import VulnerabilitiesApi  # noqa: E501
from datetime import datetime


class NvdApi(object):
    def __init__(self):
        self.vulnerabilities_api = VulnerabilitiesApi()

    def get_cves(self,
                 cpe_name:  str = None,
                 cve_id:  str = None,
                 cvss_v2_metrics:  str = None,
                 cvss_v2_severity:  str = None,
                 cvss_v3_metrics:  str = None,
                 cvss_v3_severity:  str = None,
                 cwe_id:  str = None,
                 has_cert_alerts:  str = None,
                 has_cert_notes:  str = None,
                 has_kev:  str = None,
                 has_oval:  str = None,
                 is_vulnerable:  str = None,
                 keyword_exact_match:  str = None,
                 keyword_search: str = None,
                 last_mod_start_date: datetime = None,
                 last_mod_end_date: datetime = None,
                 pub_start_date: datetime = None,
                 pub_end_date: datetime = None,
                 results_per_page: int = 2000,
                 start_index: int = None,
                 source_identifier:  str = None,
                 virtual_match_string:  str = None):

        if last_mod_start_date is not None and last_mod_start_date is None:
            raise ValueError(
                "must use last_mod_start_date with last_mod_start_date")

        if last_mod_start_date is not None and last_mod_start_date is None:
            raise ValueError(
                "must use last_mod_start_date with last_mod_start_date")

        if cvss_v2_metrics is not None and cvss_v3_metrics is not None:
            raise ValueError(
                "can not use cvss_v2_metrics with cvss_v3_metrics")

        if cvss_v2_severity is not None and cvss_v3_severity is not None:
            raise ValueError(
                "can not use cvss_v2_severity with cvss_v3_severity")

        if cvss_v3_metrics is not None and cvss_v2_metrics is not None:
            raise ValueError(
                "can not use cvss_v3_metrics with cvss_v2_metrics")

        if cvss_v3_severity is not None and cvss_v2_severity is not None:
            raise ValueError(
                "can not use cvss_v3_severity with cvss_v2_severity")

        if is_vulnerable is not None and cpe_name is None:
            raise ValueError("must use is_vulnerable with cpe_name")

        if keyword_exact_match is not None and keyword_search is None:
            raise ValueError(
                "must use keyword_exact_match with keyword_search")

        if last_mod_start_date is not None and last_mod_start_date is None:
            raise ValueError(
                "must use last_mod_start_date with last_mod_start_date")

        ret = self.vulnerabilities_api \
            .get_cves(cpe_name=cpe_name,
                      cve_id=cve_id,
                      cvss_v2_metrics=cvss_v2_metrics,
                      cvss_v2_severity=cvss_v2_severity,
                      cvss_v3_metrics=cvss_v3_metrics,
                      cvss_v3_severity=cvss_v3_severity,
                      cwe_id=cwe_id,
                      has_cert_alerts=has_cert_alerts,
                      has_cert_notes=has_cert_notes,
                      has_kev=has_kev,
                      has_oval=has_oval,
                      is_vulnerable=is_vulnerable,
                      keyword_exact_match=keyword_exact_match,
                      keyword_search=keyword_search,
                      last_mod_start_date=last_mod_start_date,
                      last_mod_end_date=last_mod_end_date,
                      pub_start_date=pub_start_date,
                      pub_end_date=pub_end_date,
                      results_per_page=results_per_page,
                      start_index=start_index,
                      source_identifier=source_identifier,
                      virtual_match_string=virtual_match_string)

        return ret

    def get_cve_history(self,
                        change_start_date: datetime = None,
                        change_end_date: datetime = None,
                        cve_id: str = None,
                        event_name: str = None,
                        results_per_page: int = None,
                        start_index: int = None):

        if change_start_date is not None and change_end_date is None:
            raise ValueError("must use change_start_date with change_end_date")

        if change_end_date is not None and change_start_date is None:
            raise ValueError("must use change_end_date with change_start_date")

        ret = self.vulnerabilities_api \
            .get_cve_history(change_start_date=change_start_date,
                             change_end_date=change_end_date,
                             cve_id=cve_id,
                             event_name=event_name,
                             results_per_page=results_per_page,
                             start_index=start_index)

        return ret
