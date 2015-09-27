import unittest
import utils
from decimal import Decimal


class UtilsTest(unittest.TestCase):
    """Test the implementation of the various utils functions"""

    def test_convert_to_decimal(self):
        """A string number should be converted to a decimal"""
        result = utils.convert_to_decimal('5.01')
        self.assertAlmostEqual(result, Decimal(5.01))

    def test_decimal_convert_fail(self):
        """A non-number string should retun None"""
        result = utils.convert_to_decimal('HAHAHHA')
        self.assertIsNone(result)
