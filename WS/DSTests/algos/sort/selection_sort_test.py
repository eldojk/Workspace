from copy import copy
from unittest import TestCase

from DS.algos.sort.selection_sort import find_min_index, swap, selection_sort


class SelectionSortTest(TestCase):
    def setUp(self):
        self.unsorted_list = [7, 8, 1, 4, 15, 44, 6, 11, 2, 21, 12]

    def tearDown(self):
        pass

    def test_find_min_index_should_return_index_of_first_occurring_min_element(self):
        min_index = find_min_index(self.unsorted_list, 0)
        self.assertEquals(2, min_index)

    def test_swap_should_swap(self):
        new_list = copy(self.unsorted_list)
        new_list[0] = 12
        new_list[len(new_list) - 1] = 7

        swap(self.unsorted_list, 0, len(self.unsorted_list) - 1)

        self.assertSequenceEqual(new_list, self.unsorted_list)

    def test_selection_sort_should_sort_list(self):
        sorted_list = copy(self.unsorted_list)
        sorted_list.sort()

        self.assertSequenceEqual(sorted_list, selection_sort(self.unsorted_list))
