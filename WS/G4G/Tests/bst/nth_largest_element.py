from unittest import TestCase

from DS.algos.graphs.bst import BST
from G4G.Problems.bst.nth_largest_element import KthLargestElement


class LVSTestCase(TestCase):
    def setUp(self):
        self.input_array = [8, 58, 71, 80, 18, 31, 32, 63, 92, 31, 43, 3, 91, 91, 93, 25, 80, 28, 58]
        self.bst = BST()
        for i in self.input_array:
            self.bst.add(i)

    def test_nth_smallest_element(self):
        k_el = KthLargestElement(self.bst)

        self.assertEqual(k_el.get_kth_largest_node(4).key, 80)
        self.assertEqual(k_el.get_kth_largest_node(2).key, 92)
        self.assertEqual(k_el.get_kth_largest_node(8).key, 43)
        self.assertEqual(k_el.get_kth_largest_node(3).key, 91)
