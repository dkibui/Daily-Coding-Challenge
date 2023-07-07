import unittest
from isogram import is_isogram


class TestIsIsogram(unittest.TestCase):
    def test_empty_string(self):
        self.assertTrue(is_isogram(''))

    def test_isogram_with_lower_case_letters(self):
        self.assertTrue(is_isogram('isogram'))

    def test_non_isogram_with_lower_case_letters(self):
        self.assertFalse(is_isogram('hello'))

    def test_isogram_with_mixed_case_letters(self):
        self.assertTrue(is_isogram('AbcDefG'))

    def test_non_isogram_with_mixed_case_letters(self):
        self.assertFalse(is_isogram('OpenAI'))

    def test_isogram_with_special_characters(self):
        self.assertTrue(is_isogram('!@#$%^&*'))

    def test_non_isogram_with_special_characters(self):
        self.assertFalse(is_isogram('hello!'))
