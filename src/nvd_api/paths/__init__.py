# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from nvd_api.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    CVES_2_0_ = "/cves/2.0/"
    CVEHISTORY_2_0_ = "/cvehistory/2.0/"
    CPES_2_0_ = "/cpes/2.0/"
    CPEMATCH_2_0_ = "/cpematch/2.0/"
