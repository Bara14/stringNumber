import unittest

from main import increaseNumber


class TestSum(unittest.TestCase):

    def test_no_digit(self):
        self.assertEqual(increaseNumber('rtrtrt'), 'rtrtrt1', "Should add 1 ad the end of string")

    def test_one_digit(self):
        self.assertEqual(increaseNumber('rtrtrt9'), 'rtrtrt10', "Should increase last digit by 1")

    def test_zero_as_last_digit(self):
        self.assertEqual(increaseNumber('rtrtrt0004000'), 'rtrtrt0004001', "Should increase last digit by 1")

    def test_string_with_digits_not_at_the_end(self):
        self.assertEqual(increaseNumber('r000trt000rt0004000'), 'r000trt000rt0004001', "Should increase last digit by 1")

    def test_multiple_digit(self):
        self.assertEqual(increaseNumber('rtrtrt19'), 'rtrtrt20', "Should increase last digits by 1")

    def test_multiple_digit_with_significant_zeros(self):
        self.assertEqual(increaseNumber('rtrtrt00019'), 'rtrtrt00020', "Should increase last digits by 1 and add significant zeros")

