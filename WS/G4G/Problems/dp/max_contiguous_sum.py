"""
To find max contiguous sum of an integer array, Lets initialize another array sum[i] with the same values as array[i]
sum[i] denotes the maximum contiguous sum with array[i] as the ending element, i.e sum till i from 0 which is maximum
and contiguous
now starting from the second element it is obvious that the maximum contiguous sum will be the value of
MAX(sum[i-1] + array[i], sum[i])
since the sequence has to end at some place, choose maximum of this :)
"""
from copy import copy


def find_max_contiguous_sum(array):
    sum_arr = copy(array)

    for i in range(1, len(array)):
        sum_arr[i] = max(sum_arr[i - 1] + array[i], sum_arr[i])

    return max(sum_arr)


if __name__ == '__main__':
    print find_max_contiguous_sum([-2, -3, 4, -1, -2, 1, 5, -3])