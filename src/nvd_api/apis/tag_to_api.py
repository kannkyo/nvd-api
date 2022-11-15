import typing_extensions

from nvd_api.apis.tags import TagValues
from nvd_api.apis.tags.products_api import ProductsApi
from nvd_api.apis.tags.vulnerabilities_api import VulnerabilitiesApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.PRODUCTS: ProductsApi,
        TagValues.VULNERABILITIES: VulnerabilitiesApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.PRODUCTS: ProductsApi,
        TagValues.VULNERABILITIES: VulnerabilitiesApi,
    }
)
