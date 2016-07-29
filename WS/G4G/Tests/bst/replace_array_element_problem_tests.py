from unittest import TestCase

from G4G.Problems.bst.replace_array_element_problem import replace_inorder_successor


class LVSTestCase(TestCase):
    def test_replace_inorder_successor(self):
        input_array = [8, 58, 71, 18, 31, 32, 63, 92, 43, 3, 91, 93, 25, 80, 28]
        output_array = replace_inorder_successor(input_array)
        expected_output = [18, 63, 80, 25, 32, 43, 80, 93, 80, 25, 93, -1, 28, -1, -1]
        self.assertSequenceEqual(output_array, expected_output)