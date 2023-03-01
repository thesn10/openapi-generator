# coding: utf-8

"""
    Echo Server API

    Echo Server API  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Contact: team@openapitools.org
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.data_query_all_of import DataQueryAllOf  # noqa: E501
from openapi_client.rest import ApiException

class TestDataQueryAllOf(unittest.TestCase):
    """DataQueryAllOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DataQueryAllOf
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DataQueryAllOf`
        """
        model = openapi_client.models.data_query_all_of.DataQueryAllOf()  # noqa: E501
        if include_optional :
            return DataQueryAllOf(
                suffix = '', 
                text = 'Some text', 
                var_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else :
            return DataQueryAllOf(
        )
        """

    def testDataQueryAllOf(self):
        """Test DataQueryAllOf"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()