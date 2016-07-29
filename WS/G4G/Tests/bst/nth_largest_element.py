from unittest import TestCase

from G4G.Problems.bst.nth_largest_element import nth_largest_element


class LVSTestCase(TestCase):
    def test_nth_smallest_element(self):
        input_array = [8, 58, 71, 18, 31, 32, 63, 92, 43, 3, 91, 93, 25, 80, 28]
        a = nth_largest_element(input_array, 3)
        self.assertEqual(a, 91)