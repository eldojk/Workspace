"""
http://www.geeksforgeeks.org/how-to-check-if-a-given-array-represents-a-binary-heap/

"""


def is_array_max_heap(array, size, parent):
    if parent > size:
        return True

    child1 = 2 * parent
    child2 = child1 + 1

    return array[parent] > array[child1] and array[parent] > array[child2]


def is_array_min_heap(array, size, parent):
    if parent > size:
        return True

    child1 = 2 * parent
    child2 = child1 + 1

    return array[parent] < array[child1] and array[parent] < array[child2]


def is_array_heap(array):
    return is_array_max_heap(array, len(array), 1) or is_array_min_heap(array, len(array), 1)


print is_array_heap([90, 15, 10, 7, 12, 2])
