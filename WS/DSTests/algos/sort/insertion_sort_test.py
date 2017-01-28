from copy import copy
from unittest import TestCase

from DS.algos.sort.insertion_sort import insertion_sort


class InsertionSortTestCase(TestCase):
    def setUp(self):
        self.sorted_array = [1, 3, 4, 7, 9, 11]
        self.list_to_sort = [3, 2, 1, 5, 77, 54, 6, 9, 3, 2, 0, 8, 7]

    def test_insertion_sort(self):
        expected_output = copy(self.list_to_sort)
        expected_output.sort()

        observed_output = insertion_sort(self.list_to_sort)

        self.assertSequenceEqual(expected_output, observed_output)



