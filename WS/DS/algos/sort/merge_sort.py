"""
O(nlgn) run time at all times
"""
from copy import copy


def merge(array, p, q, r):
    #print array, p, q, r
    left_half = copy(array[p:q+1])
    right_half = copy(array[q+1:r+1])
    #print "merging ", l,  " ", r

    i = 0
    j = 0
    k = p

    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            array[k] = left_half[i]
            i += 1
        else:
            array[k] = right_half[j]
            j += 1

        k += 1

    while i < len(left_half):
        array[k] = left_half[i]
        i += 1
        k += 1

    while j < len(right_half):
        array[k] = right_half[j]
        j += 1
        k += 1


def merge_sort(array, p, r):
    if p < r:
        mid = (p + r) // 2
        print mid
        merge_sort(array, p, mid)
        merge_sort(array, mid + 1, r)
        merge(array, p, mid, r)

    return array
