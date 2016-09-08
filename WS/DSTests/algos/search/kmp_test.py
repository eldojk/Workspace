from unittest import TestCase

from DS.algos.search.kmp import KMP


class InsertionSortTestCase(TestCase):
    def setUp(self):
        self.string = 'abxabcabcaby'
        self.kmp = KMP(self.string)

    def test_kmp(self):
        self.assertTrue(self.kmp.search_substring('abcabcaby'))
        self.assertTrue(self.kmp.search_substring('abcaby'))
        self.assertTrue(self.kmp.search_substring('abx'))
        self.assertTrue(self.kmp.search_substring('bcaby'))

        self.assertFalse(self.kmp.search_substring('baby'))
        self.assertFalse(self.kmp.search_substring('babyz'))
        self.assertFalse(self.kmp.search_substring('abxabcabcc'))
        self.assertFalse(self.kmp.search_substring('vvv'))
