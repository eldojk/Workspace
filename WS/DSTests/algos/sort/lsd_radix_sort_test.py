from copy import copy
from unittest import TestCase

from DS.algos.sort.lsd_radix_sort import LSDRadixSort


class InsertionSortTestCase(TestCase):
    def setUp(self):
        self.list_to_sort = ["abdc", "abca", "aaba", "dbac", "dcba", "baac"]
        self.sorted_list = copy(self.list_to_sort)
        self.sorted_list.sort()

    def test_lsd_radix_sort(self):
        sorter = LSDRadixSort(self.list_to_sort, 4)
        output = sorter.sort()
        self.assertSequenceEqual(self.sorted_list, output)
