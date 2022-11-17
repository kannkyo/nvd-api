# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from nvd_api.paths.cvehistory_2_0_ import Api

from nvd_api.paths import PathValues

path = PathValues.CVEHISTORY_2_0_