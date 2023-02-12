import unittest
from pprint import pprint

from nvd_api.low_api.api.products_api import ProductsApi


class TestProductsApi(unittest.TestCase):
    def setUp(self):
        self.client = ProductsApi()

    def tearDown(self):
        pass

    def test_client_without_configuration(self):
        response = self.client.get_cpes(
            cpe_name_id="87316812-5F2C-4286-94FE-CC98B9EAEF53",
            results_per_page=1,
            start_index=0
        )
        pprint(response)
