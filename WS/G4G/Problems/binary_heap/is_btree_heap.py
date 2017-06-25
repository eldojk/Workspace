"""
Check if a binary tree is a heap

max heap on array of integers
"""


def is_heap(array, index):
    if index <= 1:
        return True

    return is_heap_property_met(array, index) and is_heap(array, index - 1)


def is_heap_property_met(array, index):
    """
    Validate that Node at index has no children greater than itself

    :param array:
    :param index:
    :return:
    """
    num_children = get_number_of_children(array, index)

    if num_children == 0:
        return True

    elif num_children == 1:
        return array[index] >= array[2 * index]

    else:
        return array[index] >= max(array[2 * index], array[2 * index + 1])


def get_number_of_children(array, index):
    """
    Get number of children for node at index

    :param array:
    :param index:
    :return:
    """
    l = 2 * index
    r = l + 1

    if r > len(array):
        return 0
    elif r < len(array):
        return 2
    else:
        return 1
