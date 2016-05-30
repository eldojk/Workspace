from copy import copy
from unittest import TestCase

from DS.algos.sort.insertion_sort import insert, find_index_to_insert, insertion_sort


class InsertionSortTestCase(TestCase):
    def setUp(self):
        self.sorted_array = [1, 3, 4, 7, 9, 11]
        self.list_to_sort = [3, 2, 1, 5, 77, 54, 6, 9, 3, 2, 0, 8, 7]

    def tearDown(self):
        pass

    def test_insert_should_insert_correctly_normal(self):
        expected_output = self.sorted_array + [5]
        expected_output.sort()

        observed_output = insert(self.sorted_array, 3, 5)

        self.assertSequenceEqual(expected_output, observed_output)

    def test_insert_should_insert_correctly_at_beginning(self):
        expected_output = self.sorted_array + [-3]
        expected_output.sort()

        observed_output = insert(self.sorted_array, 0, -3)

        self.assertSequenceEqual(expected_output, observed_output)

    def test_insert_should_insert_correctly_at_end(self):
        expected_output = self.sorted_array + [22]
        expected_output.sort()

        observed_output = insert(self.sorted_array, 6, 22)

        self.assertSequenceEqual(expected_output, observed_output)

    def test_find_index_to_insert_should_insert_correctly_normal(self):
        self.assertEqual(find_index_to_insert(self.sorted_array, -3), 0)

    def test_find_index_to_insert_should_insert_correctly_at_beginning(self):
        self.assertEqual(find_index_to_insert(self.sorted_array, 5), 3)

    def test_find_index_to_insert_should_insert_correctly_at_end(self):
        self.assertEqual(find_index_to_insert(self.sorted_array, 22), 6)

    def test_insertion_sort(self):
        expected_output = copy(self.list_to_sort)
        expected_output.sort()

        observed_output = insertion_sort(self.list_to_sort)

        self.assertSequenceEqual(expected_output, observed_output)



