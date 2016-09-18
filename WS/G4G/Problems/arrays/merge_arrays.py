"""
given two sorted arrays merge them inplace if array1 has a buffer to hold array2
CTCI 11.1 #360
"""


def merge_arrays(array1, array2):
    index_a = len(array1) - len(array2) - 1
    index_b = len(array2) - 1
    index_merged = len(array1) - 1

    while index_a >= 0 and index_b >= 0:
        if array1[index_a] > array2[index_b]:
            array1[index_merged] = array1[index_a]
            index_merged -= 1
            index_a -= 1
        else:
            array1[index_merged] = array2[index_b]
            index_merged -= 1
            index_b -= 1

    return array1

# print merge_arrays([1, 2, 3, 4, None, None, None], [1, 2, 3])
