import unittest

from is_prime import is_prime


class IsPrimeTest(unittest.TestCase):
    """This is a test class for testing is_prime funciton"""

    def test_case1(self):
        self.assertTrue(is_prime(7), "7 should not be prime")

    def test_case2(self):
        self.assertFalse(is_prime(8), "8 should be prime")

    def test_case3(self):
        self.assertEqual(sum(3, 2), 5, "5 is the sum of 3 and 2")


if __name__ == '__main__':
    unittest.main()