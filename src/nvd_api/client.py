import logging
import time
from datetime import datetime
from enum import Enum

from nvd_api.low_api.api_client import ApiClient
from nvd_api.low_api.apis import ProductsApi, VulnerabilitiesApi
from nvd_api.low_api.configuration import Configuration
from nvd_api.low_api.exceptions import ApiValueError
from nvd_api.low_api.models import CpeMatchOas, CpeOas, CveHistoryOas, CveOas

logger = logging.getLogger()


class VERSION_TYPE(Enum):
    INCLUDING = "including"
    EXCLUDING = "excluding"


class CVSS_V2_SEVERITY(Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


class CVSS_V3_SEVERITY(Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"


class EVENT_NAME(Enum):
    INITIAL_ANALYSIS = "Initial Analysis"
    REANALYSIS = "Reanalysis"
    CVE_MODIFIED = "CVE Modified"
    MODIFIED_ANALYSIS = "Modified Analysis"
    CVE_TRANSLATED = "CVE Translated"
    VENDOR_COMMENT = "Vendor Comment"
    CVE_SOURCE_UPDATE = "CVE Source Update"
    CPE_DEPRECATION_REMAP = "CPE Deprecation Remap"
    CWE_REMAP = "CWE Remap"
    CVE_REJECTED = "CVE Rejected"
    CVE_UNREJECTED = "CVE Unrejected"


class NvdApiClient(object):
    """NVD API Client class
    """

    MAX_PAGE_LIMIT_CVE_API = 2000
    MAX_PAGE_LIMIT_CVE_HISTORY_API = 5000
    MAX_PAGE_LIMIT_CPE_API = 10000
    MAX_PAGE_LIMIT_CPE_MATCH_API = 5000

    def __init__(self, wait_time: int = 6000, api_key=None):
        """Constructor  # noqa: E501

        Args:
            wait_time (int, optional): wait time (ms) after api execution. Defaults to 6000.
        """
        configuration = Configuration()
        if api_key:
            configuration.api_key['ApiKeyAuth'] = api_key
        api_client = ApiClient(configuration)

        self._vulnerabilities_api = VulnerabilitiesApi(api_client)
        self._products_api = ProductsApi(api_client)
        self.wait_time = wait_time

    def get_cves(self,
                 cpe_name: str = None,
                 cve_id: str = None,
                 cvss_v2_metrics: str = None,
                 cvss_v2_severity: CVSS_V2_SEVERITY = None,
                 cvss_v3_metrics: str = None,
                 cvss_v3_severity: CVSS_V3_SEVERITY = None,
                 cwe_id: str = None,
                 has_cert_alerts: bool = False,
                 has_cert_notes: bool = False,
                 has_kev: bool = False,
                 has_oval: bool = False,
                 is_vulnerable: bool = False,
                 keyword_exact_match: bool = False,
                 keyword_search: str = None,
                 last_mod_start_date: datetime = None,
                 last_mod_end_date: datetime = None,
                 no_rejected: bool = False,
                 pub_start_date: datetime = None,
                 pub_end_date: datetime = None,
                 results_per_page: int = 2000,
                 start_index: int = None,
                 source_identifier: str = None,
                 version_end: str = None,
                 version_end_type: VERSION_TYPE = None,
                 version_start: str = None,
                 version_start_type: VERSION_TYPE = None,
                 virtual_match_string: str = None) -> CveOas:
        """CVE API  # noqa: E501

        Args:
            cpe_name (str, optional): CPE Name. Defaults to None.
            cve_id (str, optional): CVE ID. Defaults to None.
            cvss_v2_metrics (str, optional): CVSSv2 vector string. Defaults to None.
            cvss_v2_severity (CVSS_V2_SEVERITY, optional): CVSSv2 qualitative severity rating. Defaults to None.
            cvss_v3_metrics (str, optional): CVSSv3 vector string. Defaults to None.
            cvss_v3_severity (CVSS_V3_SEVERITY, optional): CVSSv3 qualitative severity rating. Defaults to None.
            cwe_id (str, optional): CWE ID. Defaults to None.
            has_cert_alerts (bool, optional): contain a Technical Alert from US-CERT. Defaults to False.
            has_cert_notes (bool, optional): contain a Vulnerability Note from CERT/CC. Defaults to False.
            has_kev (bool, optional): appear in CISA's Known Exploited Vulnerabilities (KEV) Catalog. Defaults to False.
            has_oval (bool, optional): contain information from MITRE's Open Vulnerability and Assessment Language (OVAL). Defaults to False.
            is_vulnerable (bool, optional): returns only CVE associated with a specific CPE. Defaults to False.
            keyword_exact_match (bool, optional): returns any CVE where a word or phrase. Defaults to False.
            keyword_search (str, optional): a word or phrase is found in the current description. Defaults to None.
            last_mod_start_date (datetime, optional): search by modified date. Defaults to None.
            last_mod_end_date (datetime, optional): search by modified date. Defaults to None.
            no_rejected (bool, optional): return the CVE API includes CVE records with the REJECT or Rejected status. Defaults to False.
            pub_start_date (datetime, optional): search by published date. Defaults to None.
            pub_end_date (datetime, optional): search by published date. Defaults to None.
            results_per_page (int, optional): max number of records (default is 2000). Defaults to None.
            start_index (int, optional): the index of the first match string. Defaults to None.
            source_identifier (str, optional): returns CVE where the exact value of sourceIdentifier appears. Defaults to None.
            version_end (str, optional): return only the CVEs associated with CPEs in specific version ranges. Defaults to None.
            version_end_type (VERSION_TYPE, optional): return only the CVEs associated with CPEs in specific version ranges. Defaults to None.
            version_start (str, optional): return only the CVEs associated with CPEs in specific version ranges. Defaults to None.
            version_start_type (VERSION_TYPE, optional): return only the CVEs associated with CPEs in specific version ranges. Defaults to None.
            virtual_match_string (str, optional): CVE more broadly than cpeName. Defaults to None.

        Returns:
            AsyncResult: API Result
        """

        if type(cvss_v2_severity) == CVSS_V2_SEVERITY:
            cvss_v2_severity = cvss_v2_severity.value

        if type(cvss_v3_severity) == CVSS_V3_SEVERITY:
            cvss_v3_severity = cvss_v3_severity.value

        if type(version_start_type) == VERSION_TYPE:
            version_start_type = version_start_type.value

        if type(version_end_type) == VERSION_TYPE:
            version_end_type = version_end_type.value

        last_mod_start_date = self._convert_datetime(last_mod_start_date)
        last_mod_end_date = self._convert_datetime(last_mod_end_date)
        pub_start_date = self._convert_datetime(pub_start_date)
        pub_end_date = self._convert_datetime(pub_end_date)

        self._verify_cvss_severity(cvss_v2_severity, cvss_v3_severity)
        self._verify_cvss_metrics(cvss_v2_metrics, cvss_v3_metrics)
        self._verify_last_mod_dates(last_mod_start_date, last_mod_end_date)
        self._verify_pub_dates(pub_start_date, pub_end_date)
        self._verify_vulnerable(is_vulnerable, cpe_name)
        self._verify_keyword(keyword_exact_match, keyword_search)
        self._verify_version_start(version_start, version_start_type)
        self._verify_version_end(version_end, version_end_type)

        has_cert_alerts = "" if has_cert_alerts else None
        has_cert_notes = "" if has_cert_notes else None
        has_kev = "" if has_kev else None
        has_oval = "" if has_oval else None
        is_vulnerable = "" if is_vulnerable else None
        keyword_exact_match = "" if keyword_exact_match else None
        no_rejected = "" if no_rejected else None

        kwargs = dict(cpe_name=cpe_name,
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
                      no_rejected=no_rejected,
                      pub_start_date=pub_start_date,
                      pub_end_date=pub_end_date,
                      results_per_page=results_per_page,
                      start_index=start_index,
                      source_identifier=source_identifier,
                      version_end=version_end,
                      version_end_type=version_end_type,
                      version_start=version_start,
                      version_start_type=version_start_type,
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
                        event_name: EVENT_NAME = None,
                        results_per_page: int = None,
                        start_index: int = None) -> CveHistoryOas:
        """CVE Change History API  # noqa: E501

        Args:
            change_start_date (datetime, optional): search by changed date. Defaults to None.
            change_end_date (datetime, optional): search by changed date. Defaults to None.
            cve_id (str, optional): CVE ID. Defaults to None.
            event_name (EVENT_NAME, optional): returns all CVE associated with a specific type of change event. Defaults to None.
            results_per_page (int, optional): max number of records (default is 5000). Defaults to None.
            start_index (int, optional): the index of the first match string. Defaults to None.

        Returns:
            CveHistoryOas: API Result
        """

        if type(event_name) == EVENT_NAME:
            event_name = event_name.value

        change_start_date = self._convert_datetime(change_start_date)
        change_end_date = self._convert_datetime(change_end_date)

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
                 keyword_exact_match: bool = False,
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
            keyword_exact_match (bool, optional): if CPE exactly match or not. Defaults to None. Defaults to False.
            keyword_search (str, optional): a word or phrase is found in the metadata title or reference links. Defaults to None.
            last_mod_start_date (datetime, optional): search CPE by modified date. Defaults to None.
            last_mod_end_date (datetime, optional): search CPE by modified date. Defaults to None.
            match_criteria_id (str, optional): search CPE by uuid. Defaults to None.
            results_per_page (int, optional): max number of CPE records (default is 10000). Defaults to None.
            start_index (int, optional): the index of the first match string. Defaults to None.

        Returns:
            CpeOas: API Result
        """

        last_mod_start_date = self._convert_datetime(last_mod_start_date)
        last_mod_end_date = self._convert_datetime(last_mod_end_date)

        self._verify_last_mod_dates(last_mod_start_date, last_mod_end_date)
        self._verify_keyword(keyword_exact_match, keyword_search)

        keyword_exact_match = "" if keyword_exact_match else None

        kwargs = dict(cpe_name_id=cpe_name_id,
                      cpe_match_string=cpe_match_string,
                      keyword_exact_match=keyword_exact_match,
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

        last_mod_start_date = self._convert_datetime(last_mod_start_date)
        last_mod_end_date = self._convert_datetime(last_mod_end_date)

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

    def get_all_cves(self,
                     cpe_name: str = None,
                     cve_id: str = None,
                     cvss_v2_metrics: str = None,
                     cvss_v2_severity: CVSS_V2_SEVERITY = None,
                     cvss_v3_metrics: str = None,
                     cvss_v3_severity: CVSS_V3_SEVERITY = None,
                     cwe_id: str = None,
                     has_cert_alerts: bool = False,
                     has_cert_notes: bool = False,
                     has_kev: bool = False,
                     has_oval: bool = False,
                     is_vulnerable: bool = False,
                     keyword_exact_match: bool = False,
                     keyword_search: str = None,
                     last_mod_start_date: datetime = None,
                     last_mod_end_date: datetime = None,
                     no_rejected: bool = False,
                     pub_start_date: datetime = None,
                     pub_end_date: datetime = None,
                     source_identifier: str = None,
                     version_end: str = None,
                     version_end_type: VERSION_TYPE = None,
                     version_start: str = None,
                     version_start_type: VERSION_TYPE = None,
                     virtual_match_string: str = None) -> CveOas:
        """All CVE API  # noqa: E501

        Args:
            cpe_name (str, optional): CPE Name. Defaults to None.
            cve_id (str, optional): CVE ID. Defaults to None.
            cvss_v2_metrics (str, optional): CVSSv2 vector string. Defaults to None.
            cvss_v2_severity (CVSS_V2_SEVERITY, optional): CVSSv2 qualitative severity rating. Defaults to None.
            cvss_v3_metrics (str, optional): CVSSv3 vector string. Defaults to None.
            cvss_v3_severity (CVSS_V3_SEVERITY, optional): CVSSv3 qualitative severity rating. Defaults to None.
            cwe_id (str, optional): CWE ID. Defaults to None.
            has_cert_alerts (bool, optional): contain a Technical Alert from US-CERT. Defaults to False.
            has_cert_notes (bool, optional): contain a Vulnerability Note from CERT/CC. Defaults to False.
            has_kev (bool, optional): appear in CISA's Known Exploited Vulnerabilities (KEV) Catalog. Defaults to False.
            has_oval (bool, optional): contain information from MITRE's Open Vulnerability and Assessment Language (OVAL). Defaults to False.
            is_vulnerable (bool, optional): returns only CVE associated with a specific CPE. Defaults to False.
            keyword_exact_match (bool, optional): returns any CVE where a word or phrase. Defaults to False.
            keyword_search (str, optional): a word or phrase is found in the current description. Defaults to None.
            last_mod_start_date (datetime, optional): search by modified date. Defaults to None.
            last_mod_end_date (datetime, optional): search by modified date. Defaults to None.
            no_rejected (bool, optional): return the CVE API includes CVE records with the REJECT or Rejected status. Defaults to False.
            pub_start_date (datetime, optional): search by published date. Defaults to None.
            pub_end_date (datetime, optional): search by published date. Defaults to None.
            source_identifier (str, optional): returns CVE where the exact value of sourceIdentifier appears. Defaults to None.
            version_end (str, optional): return only the CVEs associated with CPEs in specific version ranges. Defaults to None.
            version_end_type (VERSION_TYPE, optional): return only the CVEs associated with CPEs in specific version ranges. Defaults to None.
            version_start (str, optional): return only the CVEs associated with CPEs in specific version ranges. Defaults to None.
            version_start_type (VERSION_TYPE, optional): return only the CVEs associated with CPEs in specific version ranges. Defaults to None.
            virtual_match_string (str, optional): CVE more broadly than cpeName. Defaults to None.

        Returns:
            AsyncResult: API Result
        """
        limit = self.MAX_PAGE_LIMIT_CVE_API
        response = self.get_cves(start_index=0,
                                 results_per_page=limit,
                                 cpe_name=cpe_name,
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
                                 no_rejected=no_rejected,
                                 pub_start_date=pub_start_date,
                                 pub_end_date=pub_end_date,
                                 source_identifier=source_identifier,
                                 version_end=version_end,
                                 version_end_type=version_end_type,
                                 version_start=version_start,
                                 version_start_type=version_start_type,
                                 virtual_match_string=virtual_match_string)

        if response.total_results >= limit:
            count = response.total_results // limit + 1
            for start_index in range(1, count):
                r = self.get_cves(
                    start_index=start_index,
                    results_per_page=limit,
                    cpe_name=cpe_name,
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
                    no_rejected=no_rejected,
                    pub_start_date=pub_start_date,
                    pub_end_date=pub_end_date,
                    source_identifier=source_identifier,
                    version_end=version_end,
                    version_end_type=version_end_type,
                    version_start=version_start,
                    version_start_type=version_start_type,
                    virtual_match_string=virtual_match_string)
                response.vulnerabilities.extend(r.vulnerabilities)

        return response

    def get_all_cve_history(self,
                            change_start_date: datetime = None,
                            change_end_date: datetime = None,
                            cve_id: str = None,
                            event_name: EVENT_NAME = None,) -> CveHistoryOas:
        """All CVE Change History API  # noqa: E501

        Args:
            change_start_date (datetime, optional): search by changed date. Defaults to None.
            change_end_date (datetime, optional): search by changed date. Defaults to None.
            cve_id (str, optional): CVE ID. Defaults to None.
            event_name (EVENT_NAME, optional): returns all CVE associated with a specific type of change event. Defaults to None.

        Returns:
            CveHistoryOas: API Result
        """
        limit = self.MAX_PAGE_LIMIT_CVE_HISTORY_API
        response = self.get_cve_history(start_index=0,
                                        results_per_page=limit,
                                        change_start_date=change_start_date,
                                        change_end_date=change_end_date,
                                        cve_id=cve_id,
                                        event_name=event_name)

        if response.total_results >= limit:
            count = response.total_results // limit + 1
            for start_index in range(1, count):
                r = self.get_cve_history(start_index=start_index,
                                         results_per_page=limit,
                                         change_start_date=change_start_date,
                                         change_end_date=change_end_date,
                                         cve_id=cve_id,
                                         event_name=event_name)
                response.cve_changes.extend(r.cve_changes)

        return response

    def get_all_cpes(self,
                     cpe_name_id: str = None,
                     cpe_match_string: str = None,
                     keyword_exact_match: bool = False,
                     keyword_search: str = None,
                     last_mod_start_date: datetime = None,
                     last_mod_end_date: datetime = None,
                     match_criteria_id: str = None) -> CpeOas:
        """All CPE API  # noqa: E501

        Args:
            cpe_name_id (str, optional): specific CPE record UUID. Defaults to None.
            cpe_match_string (str, optional): CPE Name. Defaults to None.
            keyword_exact_match (bool, optional): if CPE exactly match or not. Defaults to None. Defaults to False.
            keyword_search (str, optional): a word or phrase is found in the metadata title or reference links. Defaults to None.
            last_mod_start_date (datetime, optional): search CPE by modified date. Defaults to None.
            last_mod_end_date (datetime, optional): search CPE by modified date. Defaults to None.
            match_criteria_id (str, optional): search CPE by uuid. Defaults to None.

        Returns:
            CpeOas: API Result
        """
        limit = self.MAX_PAGE_LIMIT_CPE_API
        response = self.get_cpes(start_index=0,
                                 results_per_page=limit,
                                 cpe_name_id=cpe_name_id,
                                 cpe_match_string=cpe_match_string,
                                 keyword_exact_match=keyword_exact_match,
                                 keyword_search=keyword_search,
                                 last_mod_start_date=last_mod_start_date,
                                 last_mod_end_date=last_mod_end_date,
                                 match_criteria_id=match_criteria_id)

        if response.total_results >= limit:
            count = response.total_results // limit + 1
            for start_index in range(1, count):
                r = self.get_cpes(start_index=start_index,
                                  results_per_page=limit,
                                  cpe_name_id=cpe_name_id,
                                  cpe_match_string=cpe_match_string,
                                  keyword_exact_match=keyword_exact_match,
                                  keyword_search=keyword_search,
                                  last_mod_start_date=last_mod_start_date,
                                  last_mod_end_date=last_mod_end_date,
                                  match_criteria_id=match_criteria_id)
                response.products.extend(r.products)

        return response

    def get_all_cpe_match(self,
                          cve_id: str = None,
                          last_mod_start_date: datetime = None,
                          last_mod_end_date: datetime = None,
                          match_criteria_id: str = None) -> CpeMatchOas:
        """All Match Criteria API  # noqa: E501

        Args:
            cve_id (str, optional): CVE ID. Defaults to None.
            last_mod_start_date (datetime, optional): search by modified date. Defaults to None.
            last_mod_end_date (datetime, optional): search by modified date. Defaults to None.
            match_criteria_id (str, optional): specific by UUID. Defaults to None.

        Returns:
            CpeMatchOas: API Result
        """
        limit = self.MAX_PAGE_LIMIT_CPE_MATCH_API
        response = self.get_cpe_match(start_index=0,
                                      results_per_page=limit,
                                      cve_id=cve_id,
                                      last_mod_start_date=last_mod_start_date,
                                      last_mod_end_date=last_mod_end_date,
                                      match_criteria_id=match_criteria_id)

        if response.total_results >= limit:
            count = response.total_results // limit + 1
            for start_index in range(1, count):
                r = self.get_cpe_match(start_index=start_index,
                                       results_per_page=limit,
                                       cve_id=cve_id,
                                       last_mod_start_date=last_mod_start_date,
                                       last_mod_end_date=last_mod_end_date,
                                       match_criteria_id=match_criteria_id)
                response.match_strings.extend(r.match_strings)

        return response

    def _convert_datetime(self, dt) -> datetime:
        if type(dt) == str:
            try:
                dt = datetime.fromisoformat(dt)
            except ValueError as e:
                raise ApiValueError(e)

        if dt is not None:
            dt = dt.replace(tzinfo=None)

        return dt

    def _verify_version_start(self,
                              version_start: str,
                              version_start_type: VERSION_TYPE):
        if version_start is not None and version_start_type is None:
            raise ApiValueError(
                "must use version_start with version_start_type")

        if version_start_type is not None and version_start is None:
            raise ApiValueError(
                "must use version_start_type with version_end")

    def _verify_version_end(self,
                            version_end: str,
                            version_end_type: VERSION_TYPE):
        if version_end is not None and version_end_type is None:
            raise ApiValueError(
                "must use version_end with version_end_type")

        if version_end_type is not None and version_end is None:
            raise ApiValueError(
                "must use version_end_type with version_end")

    def _verify_change_dates(self,
                             change_start_date: datetime,
                             change_end_date: datetime):
        if change_start_date is not None and change_end_date is None:
            raise ApiValueError(
                "must use change_start_date with change_end_date")

        if change_end_date is not None and change_start_date is None:
            raise ApiValueError(
                "must use change_end_date with change_start_date")

        if change_start_date is not None and change_end_date is not None:
            days = (change_end_date - change_start_date).days
            if days > 120:
                raise ApiValueError(
                    f"max date range is 120 days : start - end={days}")

    def _verify_last_mod_dates(self,
                               last_mod_start_date: datetime,
                               last_mod_end_date: datetime):
        if last_mod_start_date is not None and last_mod_end_date is None:
            raise ApiValueError(
                "must use last_mod_start_date with last_mod_end_date")

        if last_mod_end_date is not None and last_mod_start_date is None:
            raise ApiValueError(
                "must use last_mod_end_date with last_mod_start_date")

        if last_mod_start_date is not None and last_mod_end_date is not None:
            days = (last_mod_end_date - last_mod_start_date).days
            if days > 120:
                raise ApiValueError(
                    f"max date range is 120 days : start - end={days}")

    def _verify_pub_dates(self,
                          pub_start_date: datetime,
                          pub_end_date: datetime):
        if pub_start_date is not None and pub_end_date is None:
            raise ApiValueError(
                "must use pub_start_date with pub_end_date")

        if pub_end_date is not None and pub_start_date is None:
            raise ApiValueError(
                "must use pub_end_date with pub_start_date")

        if pub_start_date is not None and pub_end_date is not None:
            days = (pub_end_date - pub_start_date).days
            if days > 120:
                raise ApiValueError(
                    f"max date range is 120 days : start - end={days}")

    def _verify_cvss_metrics(self,
                             cvss_v2_metrics: str,
                             cvss_v3_metrics: str):
        if cvss_v2_metrics is not None and cvss_v3_metrics is not None:
            raise ApiValueError(
                "can not use cvss_v2_metrics with cvss_v3_metrics")

    def _verify_cvss_severity(self,
                              cvss_v2_severity: str,
                              cvss_v3_severity: str):
        if cvss_v2_severity is not None and cvss_v3_severity is not None:
            raise ApiValueError(
                "can not use cvss_v2_severity with cvss_v3_severity")

    def _verify_vulnerable(self,
                           is_vulnerable: bool,
                           cpe_name: str,):
        if is_vulnerable is True and cpe_name is None:
            raise ApiValueError("must use is_vulnerable with cpe_name")

    def _verify_keyword(self,
                        keyword_exact_match: bool,
                        keyword_search: str,):
        if keyword_exact_match is True and keyword_search is None:
            raise ApiValueError(
                "must use keyword_exact_match with keyword_search")

    def _sleep(self, wait_time: int = None):
        if wait_time is None:
            time.sleep(self.wait_time/1000)
        else:
            time.sleep(wait_time/1000)
