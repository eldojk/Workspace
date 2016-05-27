"""
Insertion sort repeatedly inserts an element in the sorted sub-array to its left.
"""


def insert(sorted_list, index, val):
    """
    Insert val at index in the sorted_list

    :param sorted_list:
    :param index:
    :param val:
    :return:
    """
    if index == 0:
        # Insert at beginning
        left_array = []
        right_array = sorted_list

    elif index == len(sorted_list):
        # Insert at end
        left_array = sorted_list
        right_array = []

    else:
        # Insert somewhere in between
        left_array = sorted_list[:index]
        right_array = sorted_list[index:]

    return left_array + [val] + right_array


def find_index_to_insert(sorted_list, val):
    """
    Finds the index for i to be inserted

    :param sorted_list:
    :param val:
    :return:
    """
    for i in range(len(sorted_list)):
        if sorted_list[i] >= val:
            return i

    return len(sorted_list)


def insertion_sort(unsorted_list):
    """
    Sorts the unsorted_list using insertion sort

    :param unsorted_list:
    :return:
    """
    sorted_list = unsorted_list[:1]

    for i in range(len(unsorted_list))[1:]:
        element = unsorted_list[i]
        index_to_insert = find_index_to_insert(sorted_list, element)
        sorted_list = insert(sorted_list, index_to_insert, element)

    return sorted_list


