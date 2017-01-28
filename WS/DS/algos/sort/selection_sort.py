"""
No best/worst case. O(n2) is always taken regardless of how elements are arranged in the array

Takes each element, finds the minimum element to its right less than the element and swap it.
"""


def find_min_index(array, start_index):
    """
    Finds the index of the smallest element in the array

    :param array:
    :param start_index:
    :return:
    """
    end_index = len(array) - 1
    minimum = start_index
    while start_index <= end_index:
        if array[start_index] < array[minimum]:
            minimum = start_index

        start_index += 1

    return minimum


def swap(array, first_index, second_index):
    """
    Swap two array elements

    :param array:
    :param first_index:
    :param second_index:
    :return:
    """
    temp = array[first_index]
    array[first_index] = array[second_index]
    array[second_index] = temp


def selection_sort(list_to_sort):
    """
    Selection sort on a list

    :param list_to_sort:
    :return:
    """
    for index in range(len(list_to_sort)):
        min_index = find_min_index(list_to_sort, index)
        swap(list_to_sort, index, min_index)
        print list_to_sort

    return list_to_sort
