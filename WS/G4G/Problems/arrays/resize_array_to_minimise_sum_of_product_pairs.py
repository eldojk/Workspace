"""
http://www.geeksforgeeks.org/rearrange-array-minimize-sum-product-consecutive-pair-elements/

hint: pair smallest with largest and so on
"""
from copy import copy


def rearrange(array):
    array.sort()
    rev_array = copy(array)
    rev_array.reverse()
    rearranged_array = [0 for i in array]

    i = 1
    j = 0
    while i <= len(array):
        rearranged_array[i-1] = array[j]
        rearranged_array[i] = rev_array[j]
        i += 2
        j += 1

    return rearranged_array

print rearrange([9, 2, 8, 4, 5, 7, 6, 0])