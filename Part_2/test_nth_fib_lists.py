import unittest

from nth_fib_lists import nth_fib_lists

class testNthFibLists(unittest.TestCase):

    def test_nth_fib_lists_if_n_is_1(self):
        self.assertEqual([2], nth_fib_lists([2], [3], 1))

    def test_nth_fib_lists_if_n_is_2(self):
        self.assertEqual([3], nth_fib_lists([2], [3], 2))

    def test_nth_fib_lists_if_n_is_greater_than_2(self):
        self.assertEqual([2, 3, 5, 6], nth_fib_lists([2, 3], [5, 6], 3))

    def test_nth_fib_lists_if_n_is_3(self):
        self.assertEqual([5, 6, 2, 3, 5, 6], nth_fib_lists([2, 3], [5, 6], 4))

    def test_empty_list(self):
        self.assertEqual([], nth_fib_lists([], [], 20))

    def test_first_empty_list(self):
        self.assertEqual([3], nth_fib_lists([], [3], 3))




if __name__ == '__main__':
    unittest.main()