import unittest

from prepare_meal import prepare_meal

class TestPrepareMeal(unittest.TestCase):

    def test_spam_only(self):
        self.assertEqual("spam spam spam spam ", prepare_meal(81))

    def test_eggs_only(self):
        self.assertEqual("eggs ", prepare_meal(5))

    def test_spam_and_eggs(self):
        self.assertEqual("spam and eggs ", prepare_meal(15))

    def test_more_spams_and_eggs(self):
        self.assertEqual("spam spam and eggs ", prepare_meal(45))

    def test_more_eggs_only(self):
        self.assertEqual("eggs and eggs ", prepare_meal(25))


if __name__ == '__main__':
    unittest.main()