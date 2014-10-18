import unittest

from sort_fraction import sort_fractions

class testSortFraction(unittest.TestCase):

    def test_empty_fraction(self):
        self.assertEqual([], sort_fractions([]))

    def test_one_fraction(self):
        self.assertEqual([(1, 3)], sort_fractions([(1, 3)]))

    def test_more_fractions(self):
        self.assertEqual([(1, 3), (1, 2), (2, 3)], sort_fractions([(2, 3), (1, 2), (1, 3)]))

    def test_more_fractions_with_zero_nominator(self):
        self.assertEqual([(0, 3), (1, 2), (2, 3)], sort_fractions([(2, 3), (1, 2), (0, 3)]))



if __name__ == '__main__':
    unittest.main()