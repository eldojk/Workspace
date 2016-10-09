"""
http://www.geeksforgeeks.org/dynamic-programming-subset-sum-problem/

Given a set of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to
given sum.

Examples: set[] = {3, 34, 4, 12, 5, 2}, sum = 9
Output:  True  //There is a subset (4, 5) with sum 9.
"""
from copy import copy


def is_exists_valid_sum(elements, sm):
    is_valid_arr = [1] + [0 for i in range(sm)]

    for j in range(len(elements)):
        # maintaining the previous array every time as we can only use an element once
        # eg. is_v[8] for i = 4 will reduce to 1 * is_v[8-4] = 1* is_v[4] = 1. But we expect zero, because it
        # is using 4 twice in this case
        copy_arr = copy(is_valid_arr)
        for i in range(len(is_valid_arr)):
            el = elements[j]
            if i >= el and el <= sm and is_valid_arr[i] == 0:
                is_valid_arr[i] = 1 * copy_arr[i - elements[j]]

    return is_valid_arr[sm] == 1
