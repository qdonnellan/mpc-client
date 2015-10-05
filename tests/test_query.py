import unittest
from mpc_client.query import Query


class QueryTest(unittest.TestCase):

    def test_filter_parameters(self):
        """Adding a filter should append a string to parameters"""
        q = Query()
        q.filter(hello="World")
        self.assertEqual(q._parameters['hello'], "World")

    def test_default_order(self):
        """Adding an order parameter should update parameters"""
        q = Query()
        q.order('hello')
        self.assertEqual(q._parameters['order_by'], "hello")

    def test_order_desc(self):
        """Adding a descending order paramter should work as expected"""
        q = Query().order('hello', desc=True)
        self.assertEqual(q._parameters['order_by_desc'], "hello")

    def test_change_order(self):
        """Overriding an order paramter by a descending order parameter should
        remove the original parameter altogether"""
        q = Query().order("something")
        q.order("something_else", desc=True)
        self.assertIsNone(q._parameters.get('order_by', None))