# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import nvd_api
from nvd_api.paths.cves_2_0_ import get  # noqa: E501
from nvd_api import configuration, schemas, api_client

from .. import ApiTestMixin


class TestCves20(ApiTestMixin, unittest.TestCase):
    """
    Cves20 unit test stubs
        CVE API  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = get.ApiForget(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
