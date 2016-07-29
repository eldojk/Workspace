from unittest import TestCase

from DS.algos.graphs.bst import BST
from DS.algos.graphs.range_search import range_search


class RangeSearchTest(TestCase):
    def setUp(self):
        self.bst = BST()
        self.array = [8, 58, 71, 18, 31, 32, 63, 92, 43, 3, 91, 93, 25, 80, 28]
        for i in self.array:
            self.bst.add(i)

    def test_range_search_with_present_elements(self):
        op = range_search(self.bst, 18, 71)
        print op
        self.assertSequenceEqual(op, [18, 25, 28, 31, 32, 43, 58, 63, 71])

    def test_range_search_with_absent_elements(self):
        op = range_search(self.bst, 17, 72)
        print op
        self.assertSequenceEqual(op, [18, 25, 28, 31, 32, 43, 58, 63, 71])
