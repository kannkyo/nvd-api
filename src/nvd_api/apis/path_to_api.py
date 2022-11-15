import typing_extensions

from nvd_api.paths import PathValues
from nvd_api.apis.paths.cves_2_0_ import Cves20
from nvd_api.apis.paths.cvehistory_2_0_ import Cvehistory20
from nvd_api.apis.paths.cpes_2_0_ import Cpes20
from nvd_api.apis.paths.cpematch_2_0_ import Cpematch20

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.CVES_2_0_: Cves20,
        PathValues.CVEHISTORY_2_0_: Cvehistory20,
        PathValues.CPES_2_0_: Cpes20,
        PathValues.CPEMATCH_2_0_: Cpematch20,
    }
)

path_to_api = PathToApi(
    {
        PathValues.CVES_2_0_: Cves20,
        PathValues.CVEHISTORY_2_0_: Cvehistory20,
        PathValues.CPES_2_0_: Cpes20,
        PathValues.CPEMATCH_2_0_: Cpematch20,
    }
)
