import unittest
from mpc_client.models.mpc_object import MpcObject
from decimal import Decimal


class MpcObjectTest(unittest.TestCase):
    """Test the implementation of the MpcObject"""
    fake_mpc_object = MpcObject({
        "param1": '5.01',
        "param2": 'Hahaha totally not a decimal value'
    })

    def test_convert_to_decimal(self):
        """A string number should be converted to a decimal"""
        result = self.fake_mpc_object._get_as_decimal('param1')
        self.assertAlmostEqual(result, Decimal(5.01))

    def test_decimal_convert_fail(self):
        """A non-number string should retun None"""
        result = self.fake_mpc_object._get_as_decimal('param2')
        self.assertIsNone(result)
