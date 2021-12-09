# -*- coding: utf-8 -*-
import unittest
from . product import ProductSoap


class TestProduct(unittest.TestCase):

    def setUp(self):
        self.ps = ProductSoap(api_key="F8194B4C-F6B9-45AD-9914-8FDF53E8601C")

    def test_get_list_products(self):
        r = self.ps.get_product_list()
        print(r)
        # rc = self.ps.confirm_integration_product(r['result']['data'][0]['protocol_product'])
        # print rc
