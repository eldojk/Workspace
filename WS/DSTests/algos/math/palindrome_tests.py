from unittest import TestCase

from DS.algos.math.palindrome import is_palindrome


class PalindromeTestCase(TestCase):

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome('rotor'))
        self.assertFalse(is_palindrome('motor'))

    def test_is_palindrome_should_handle_cases(self):
        self.assertTrue(is_palindrome('rOtoR'))
        self.assertFalse(is_palindrome('motOr'))

    def test_is_palindrome_should_handle_varying_lengths(self):
        self.assertTrue(is_palindrome(""))
        self.assertTrue(is_palindrome("a"))