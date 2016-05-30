from copy import copy
from unittest import TestCase

from DS.algos.sort.merge_sort import merge_sort


class MergeSortTestCase(TestCase):
    def setUp(self):
        self.sorted_array = [1, 3, 4, 7, 9, 11]
        self.list_to_sort = [3, 2, 1, 5, 77, 54, 6, 9, 3, 2, 0, 8, 7]

    def tearDown(self):
        pass

    def test_merge_sort_should_sort(self):
        expected_output = copy(self.list_to_sort)
        expected_output.sort()
        last_index = len(self.list_to_sort) - 1

        observed_output = merge_sort(self.list_to_sort, 0, last_index)

        self.assertSequenceEqual(observed_output, expected_output)
