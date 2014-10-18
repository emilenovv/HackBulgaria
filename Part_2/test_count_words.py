import unittest

from count_words import count_words

class TestCountWords(unittest.TestCase):
    def test_count_one_word(self):
        self.assertEqual({"apple": 1}, count_words(["apple"]))

    def test_count_more_words(self):
        self.assertEqual({"apple": 2}, count_words(["apple", "apple"]))

    def test_count_no_words(self):
        self.assertEqual({}, count_words([]))

    def test_count_different_words(self):
        self.assertEqual({'cow': 1, 'apple': 1}, count_words(["cow", "apple"]))


if __name__ == '__main__':
    unittest.main()