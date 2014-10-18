import unittest

from is_an_bn import is_an_bn

class TestIsAnBn(unittest.TestCase):

    def test_empty_string(self):
        self.assertTrue(is_an_bn(''))

    def test_equal_a_not_equal_b(self):
        self.assertFalse(is_an_bn("aaaaaabbbb"))

    def test_only_b(self):
        self.assertFalse(is_an_bn("bbbbb"))

    def test_only_a(self):
        self.assertFalse(is_an_bn("aaaa"))

    def test_in_an_bn(self):
        self.assertTrue(is_an_bn("aaabbb"))

    def test_different_chars(self):
        self.assertFalse(is_an_bn("emilaaabbb"))


if __name__ == '__main__':
    unittest.main()