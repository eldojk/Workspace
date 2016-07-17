from unittest import TestCase

from G4G.Problems.stacks.largest_valid_substring import largest_valid_substring


class LVSTestCase(TestCase):
    def test_lvs_valid(self):
        self.assertEqual('(())', largest_valid_substring('(())'))
        self.assertEqual('(())', largest_valid_substring('(()))))'))
        self.assertEqual('(())', largest_valid_substring('(())()'))
        self.assertEqual('((())())', largest_valid_substring('((())())'))

    def test_lvs_invalid(self):
        self.assertEqual(None, largest_valid_substring('(((('))
        self.assertEqual(None, largest_valid_substring('))))))'))
