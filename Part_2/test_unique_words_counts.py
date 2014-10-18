import unittest

from unique_words_count import unique_words_count

class TestCountUnique(unittest.TestCase):
    def test_count_no_words(self):
        self.assertEqual(0, unique_words_count([]))

    def test_count_one_words(self):
        self.assertEqual(1, unique_words_count(["python"]))

    def test_count_one_words_many_times(self):
        self.assertEqual(1, unique_words_count(["python", "python", "python", "python"]))

    def test_count_different_words(self):
        self.assertEqual(4, unique_words_count(["perl", "c++", "python", "erlang"]))

    def test_count_different_and_same_words(self):
        self.assertEqual(4, unique_words_count(["perl", "python", "c++", "python", "erlang"]))

if __name__ == '__main__':
    unittest.main()
