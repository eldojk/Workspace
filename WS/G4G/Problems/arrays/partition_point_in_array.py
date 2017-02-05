"""
http://www.geeksforgeeks.org/find-a-partition-point-in-array/
Input :  A[] = {4, 3, 2, 5, 8, 6, 7}
Output : 5

[4 4 4 5 8 8 8]
[2 2 2 5 6 6 7]
"""
from sys import maxint


def max_seen_so_far(array):
    max_arr = []
    max_el = -maxint

    for element in array:
        if element > max_el:
            max_el = element

        max_arr.append(max_el)

    return max_arr


def minimum_from_right(array):
    min_arr = [0 for i in array]
    min_el = maxint
    j = len(array) - 1

    while j > 0:
        element = array[j]
        if element < min_el:
            min_el = element

        min_arr[j] = min_el
        j -= 1

    return min_arr


def partition_element(array):
    max_so_far = max_seen_so_far(array)
    min_frm_right = minimum_from_right(array)
    partition = None

    for i in range(len(array)):
        if i == 0:
            if min_frm_right[i + 1] > array[i]:
                partition = array[i]
                break
        elif i == len(array) - 1:
            if max_so_far[i - 1] < array[i]:
                partition = array[i]
                break
        else:
            if max_so_far[i - 1] < array[i] < min_frm_right[i + 1]:
                partition = array[i]
                break

    if partition:
        print partition
    else:
        print -1


partition_element([4, 3, 2, 5, 8, 6, 7])
partition_element([5, 6, 2, 8, 10, 9, 8])
