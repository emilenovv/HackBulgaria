import unittest

from simplify_fraction import simplify_fraction, find_divisors

class TestSimplifyFraction(unittest.TestCase):

    def test_find_divisors_greater_than_zero(self):
        self.assertEqual([1, 2, 3, 6], find_divisors(6))

    def test_find_divisors_zero(self):
        self.assertEqual([], find_divisors(0))

    def test_simplify_fraction(self):
        self.assertEqual((1, 2), simplify_fraction((2, 4)))

    def test_simplify_fraction_zero_nominator(self):
        self.assertEqual((0), simplify_fraction((0, 4)))


if __name__ == '__main__':
    unittest.main()