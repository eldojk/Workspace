"""
No best/worst case. O(n2) is always taken regardless of how elements are arranged in the array
"""


def find_min_index(array, start_index):
    """
    Finds the index of the smallest element in the array

    :param array:
    :param start_index:
    :return:
    """
    sliced_array = array[start_index:]
    min_element = sliced_array[0]
    min_index = 0

    for i in range(len(sliced_array)):
        if sliced_array[i] < min_element:
            min_element = sliced_array[i]
            min_index = i

    return min_index + start_index


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

    return list_to_sort
