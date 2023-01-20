from enum import Enum
import logging
import time
from datetime import datetime
from nvd_api.model.cpe_match_oas import CpeMatchOas
from nvd_api.model.cpe_oas import CpeOas
from nvd_api.model.cve_history_oas import CveHistoryOas
from nvd_api.model.cve_oas import CveOas

from nvd_api.api.products_api import ProductsApi  # noqa: E501
from nvd_api.api.vulnerabilities_api import VulnerabilitiesApi
from nvd_api.exceptions import ApiValueError  # noqa: E501

logger = logging.getLogger()


class FLAG(Enum):
    """Flag class"""

    TRUE = ""
    FALSE = None


class NvdApiClient(object):
    """NVD API Client class
    """

    def __init__(self, wait_time: int = 6000):
        """Constructor  # noqa: E501

        Args:
            wait_time (int, optional): wait time (ms) after api execution. Defaults to 6000.
        """
        self._vulnerabilities_api = VulnerabilitiesApi()
        self._products_api = ProductsApi()
        self.wait_time = wait_time

    def get_cves(self,
                 cpe_name: str = None,
                 cve_id: str = None,
                 cvss_v2_metrics: str = None,
                 cvss_v2_severity: str = None,
                 cvss_v3_metrics: str = None,
                 cvss_v3_severity: str = None,
                 cwe_id: str = None,
                 has_cert_alerts: FLAG = FLAG.FALSE,
                 has_cert_notes: FLAG = FLAG.FALSE,
                 has_kev: FLAG = FLAG.FALSE,
                 has_oval: FLAG = FLAG.FALSE,
                 is_vulnerable: FLAG = FLAG.FALSE,
                 keyword_exact_match: FLAG = FLAG.FALSE,
                 keyword_search: str = None,
                 last_mod_start_date: datetime = None,
                 last_mod_end_date: datetime = None,
                 pub_start_date: datetime = None,
                 pub_end_date: datetime = None,
                 results_per_page: int = 2000,
                 start_index: int = None,
                 source_identifier: str = None,
                 virtual_match_string: str = None) -> CveOas:
        """CVE API  # noqa: E501

        Args:
            cpe_name (str, optional): CPE Name. Defaults to None.
            cve_id (str, optional): CVE ID. Defaults to None.
            cvss_v2_metrics (str, optional): CVSSv2 vector string. Defaults to None.
            cvss_v2_severity (str, optional): CVSSv2 qualitative severity rating. Defaults to None.
            cvss_v3_metrics (str, optional): CVSSv3 vector string. Defaults to None.
            cvss_v3_severity (str, optional): CVSSv3 qualitative severity rating. Defaults to None.
            cwe_id (str, optional): CWE ID. Defaults to None.
            has_cert_alerts (FLAG, optional): contain a Technical Alert from US-CERT. Defaults to None.
            has_cert_notes (FLAG, optional): contain a Vulnerability Note from CERT/CC. Defaults to None.
            has_kev (FLAG, optional): appear in CISA's Known Exploited Vulnerabilities (KEV) Catalog. Defaults to None.
            has_oval (FLAG, optional): contain information from MITRE's Open Vulnerability and Assessment Language (OVAL). Defaults to None.
            is_vulnerable (FLAG, optional): returns only CVE associated with a specific CPE. Defaults to None.
            keyword_exact_match (FLAG, optional): returns any CVE where a word or phrase. Defaults to None.
            keyword_search (str, optional): a word or phrase is found in the current description. Defaults to None.
            last_mod_start_date (datetime, optional): search by modified date. Defaults to None.
            last_mod_end_date (datetime, optional): search by modified date. Defaults to None.
            pub_start_date (datetime, optional): search by published date. Defaults to None.
            pub_end_date (datetime, optional): search by published date. Defaults to None.
            results_per_page (int, optional): max number of records (default is 2000). Defaults to None.
            start_index (int, optional): the index of the first match string. Defaults to None.
            source_identifier (str, optional): returns CVE where the exact value of sourceIdentifier appears. Defaults to None.
            virtual_match_string (str, optional): CVE more broadly than cpeName. Defaults to None.

        Returns:
            AsyncResult: API Result
        """

        self._verify_cvss_severity(cvss_v2_severity, cvss_v3_severity)
        self._verify_cvss_metrics(cvss_v2_metrics, cvss_v3_metrics)
        self._verify_last_mod_dates(last_mod_start_date, last_mod_end_date)
        self._verify_pub_dates(pub_start_date, pub_end_date)
        self._verify_vulnerable(is_vulnerable, cpe_name)
        self._verify_keyword(keyword_exact_match, keyword_search)

        kwargs = dict(cpe_name=cpe_name,
                      cve_id=cve_id,
                      cvss_v2_metrics=cvss_v2_metrics,
                      cvss_v2_severity=cvss_v2_severity,
                      cvss_v3_metrics=cvss_v3_metrics,
                      cvss_v3_severity=cvss_v3_severity,
                      cwe_id=cwe_id,
                      has_cert_alerts=has_cert_alerts.value,
                      has_cert_notes=has_cert_notes.value,
                      has_kev=has_kev.value,
                      has_oval=has_oval.value,
                      is_vulnerable=is_vulnerable.value,
                      keyword_exact_match=keyword_exact_match.value,
                      keyword_search=keyword_search,
                      last_mod_start_date=last_mod_start_date,
                      last_mod_end_date=last_mod_end_date,
                      pub_start_date=pub_start_date,
                      pub_end_date=pub_end_date,
                      results_per_page=results_per_page,
                      start_index=start_index,
                      source_identifier=source_identifier,
                      virtual_match_string=virtual_match_string)
        kwargs = {k: v for k, v in kwargs.items() if v is not None}  # Noneは削除

        logger.debug(f"execute cves api : kwargs={kwargs}")
        ret = self._vulnerabilities_api.get_cves(**kwargs)
        logger.debug(f"execute cves api : response={ret}")
        self._sleep()

        return ret

    def get_cve_history(self,
                        change_start_date: datetime = None,
                        change_end_date: datetime = None,
                        cve_id: str = None,
                        event_name: str = None,
                        results_per_page: int = None,
                        start_index: int = None) -> CveHistoryOas:
        """CVE Change History API  # noqa: E501

        Args:
            change_start_date (datetime, optional): search by changed date. Defaults to None.
            change_end_date (datetime, optional): search by changed date. Defaults to None.
            cve_id (str, optional): CVE ID. Defaults to None.
            event_name (str, optional): returns all CVE associated with a specific type of change event. Defaults to None.
            results_per_page (int, optional): max number of records (default is 5000). Defaults to None.
            start_index (int, optional): the index of the first match string. Defaults to None.

        Returns:
            CveHistoryOas: API Result
        """

        self._verify_change_dates(change_start_date, change_end_date)

        kwargs = dict(change_start_date=change_start_date,
                      change_end_date=change_end_date,
                      cve_id=cve_id,
                      event_name=event_name,
                      results_per_page=results_per_page,
                      start_index=start_index)
        kwargs = {k: v for k, v in kwargs.items() if v is not None}  # Noneは削除

        logger.debug(f"execute cve history api : kwargs={kwargs}")
        ret = self._vulnerabilities_api.get_cve_history(**kwargs)
        logger.debug(f"execute cve history api : response={ret}")
        self._sleep()

        return ret

    def get_cpes(self,
                 cpe_name_id: str = None,
                 cpe_match_string: str = None,
                 keyword_exact_match: FLAG = FLAG.FALSE,
                 keyword_search: str = None,
                 last_mod_start_date: datetime = None,
                 last_mod_end_date: datetime = None,
                 match_criteria_id: str = None,
                 results_per_page: int = None,
                 start_index: int = None) -> CpeOas:
        """CPE API  # noqa: E501

        Args:
            cpe_name_id (str, optional): specific CPE record UUID. Defaults to None.
            cpe_match_string (str, optional): CPE Name. Defaults to None.
            keyword_exact_match (FLAG, optional): if CPE exactly match or not. Defaults to None. Defaults to None.
            keyword_search (str, optional): a word or phrase is found in the metadata title or reference links. Defaults to None.
            last_mod_start_date (datetime, optional): search CPE by modified date. Defaults to None.
            last_mod_end_date (datetime, optional): search CPE by modified date. Defaults to None.
            match_criteria_id (str, optional): search CPE by uuid. Defaults to None.
            results_per_page (int, optional): max number of CPE records (default is 10000). Defaults to None.
            start_index (int, optional): the index of the first match string. Defaults to None.

        Returns:
            CpeOas: API Result
        """
        self._verify_last_mod_dates(last_mod_start_date, last_mod_end_date)
        self._verify_keyword(keyword_exact_match, keyword_search)

        kwargs = dict(cpe_name_id=cpe_name_id,
                      cpe_match_string=cpe_match_string,
                      keyword_exact_match=keyword_exact_match.value,
                      keyword_search=keyword_search,
                      last_mod_start_date=last_mod_start_date,
                      last_mod_end_date=last_mod_end_date,
                      match_criteria_id=match_criteria_id,
                      results_per_page=results_per_page,
                      start_index=start_index)
        kwargs = {k: v for k, v in kwargs.items() if v is not None}  # Noneは削除

        logger.debug(f"execute cpes api : kwargs={kwargs}")
        ret = self._products_api.get_cpes(**kwargs)
        logger.debug(f"execute cpes api : response={ret}")
        self._sleep()

        return ret

    def get_cpe_match(self,
                      cve_id: str = None,
                      last_mod_start_date: datetime = None,
                      last_mod_end_date: datetime = None,
                      match_criteria_id: str = None,
                      results_per_page: int = None,
                      start_index: int = None) -> CpeMatchOas:
        """Match Criteria API  # noqa: E501

        Args:
            cve_id (str, optional): CVE ID. Defaults to None.
            last_mod_start_date (datetime, optional): search by modified date. Defaults to None.
            last_mod_end_date (datetime, optional): search by modified date. Defaults to None.
            match_criteria_id (str, optional): specific by UUID. Defaults to None.
            results_per_page (int, optional): max number of records (default is 5000). Defaults to None.
            start_index (int, optional): the index of the first match string. Defaults to None.

        Returns:
            CpeMatchOas: API Result
        """
        self._verify_last_mod_dates(last_mod_start_date, last_mod_end_date)

        kwargs = dict(cve_id=cve_id,
                      last_mod_start_date=last_mod_start_date,
                      last_mod_end_date=last_mod_end_date,
                      match_criteria_id=match_criteria_id,
                      results_per_page=results_per_page,
                      start_index=start_index)
        kwargs = {k: v for k, v in kwargs.items() if v is not None}  # Noneは削除

        logger.debug(f"execute cpe match api : kwargs={kwargs}")
        ret = self._products_api.get_cpe_match(**kwargs)
        logger.debug(f"execute cpe match api : response={ret}")
        self._sleep()

        return ret

    def _verify_change_dates(self,
                             change_start_date: datetime | None,
                             change_end_date: datetime | None):
        if change_start_date is not None and change_end_date is None:
            raise ApiValueError(
                "must use change_start_date with change_end_date")

        if change_end_date is not None and change_start_date is None:
            raise ApiValueError(
                "must use change_end_date with change_start_date")

    def _verify_last_mod_dates(self,
                               last_mod_start_date: datetime | None,
                               last_mod_end_date: datetime | None):
        if last_mod_start_date is not None and last_mod_end_date is None:
            raise ApiValueError(
                "must use last_mod_start_date with last_mod_end_date")

        if last_mod_end_date is not None and last_mod_start_date is None:
            raise ApiValueError(
                "must use last_mod_end_date with last_mod_start_date")

    def _verify_pub_dates(self,
                          pub_start_date: datetime | None,
                          pub_end_date: datetime | None):
        if pub_start_date is not None and pub_end_date is None:
            raise ApiValueError(
                "must use pub_start_date with pub_end_date")

        if pub_end_date is not None and pub_start_date is None:
            raise ApiValueError(
                "must use pub_end_date with pub_start_date")

    def _verify_cvss_metrics(self,
                             cvss_v2_metrics: str | None,
                             cvss_v3_metrics: str | None):
        if cvss_v2_metrics is not None and cvss_v3_metrics is not None:
            raise ApiValueError(
                "can not use cvss_v2_metrics with cvss_v3_metrics")

    def _verify_cvss_severity(self,
                              cvss_v2_severity: str | None,
                              cvss_v3_severity: str | None):
        if cvss_v2_severity is not None and cvss_v3_severity is not None:
            raise ApiValueError(
                "can not use cvss_v2_severity with cvss_v3_severity")

    def _verify_vulnerable(self,
                           is_vulnerable: FLAG,
                           cpe_name: str | None,):
        if is_vulnerable is FLAG.TRUE and cpe_name is None:
            raise ApiValueError("must use is_vulnerable with cpe_name")

    def _verify_keyword(self,
                        keyword_exact_match: FLAG,
                        keyword_search: str | None,):
        if keyword_exact_match is FLAG.TRUE and keyword_search is None:
            raise ApiValueError(
                "must use keyword_exact_match with keyword_search")

    def _sleep(self, wait_time: int = None):
        if wait_time is None:
            time.sleep(self.wait_time/1000)
        else:
            time.sleep(wait_time/1000)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    client = NvdApiClient()
    response = client.get_cve_history(
        change_start_date="2021-08-04T00:00:00.000",
        change_end_date="2021-10-23T00:00:00.000",
        event_name="CVE Rejected",
        results_per_page=1,
        start_index=1
    )
    response = client.get_cves(
        last_mod_start_date="2018-10-10T00:00:00.000",
        # last_mod_end_date="2018-10-20T00:00:00.000",
        pub_start_date="2006-05-15T00:00:00.000",
        pub_end_date="2006-05-25T00:00:00.000",
        results_per_page=1,
        start_index=1
    )
