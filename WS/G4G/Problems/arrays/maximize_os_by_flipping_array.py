# coding=utf-8
"""
amzn

http://www.geeksforgeeks.org/maximize-number-0s-flipping-subarray/

This problem can be reduced to largest sub array sum problem. The idea is to consider
every 0 as -1 and every 1 as 1,
find the sum of largest sub array sum in this modified array. This sum is our required
max_diff ( count of 0s – count of
1s in any sub array). Finally we return the max_diff plus count of zeros in original array
"""
from G4G.Problems.dp.max_contiguous_sum import find_max_contiguous_sum


def count_zeroes(array):
    cnt = 0
    for c in array:
        if c == 0:
            cnt += 1

    return cnt


def replace_zero_with_neg_1s(array):
    new_arr = []

    for c in array:
        if c == 0:
            new_arr.append(-1)
        else:
            new_arr.append(c)

    return new_arr


def find_max_zeroes_we_can_get(array):
    num_zeroes = count_zeroes(array)
    new_arr = replace_zero_with_neg_1s(array)

    max_new_zeroes = find_max_contiguous_sum(new_arr)

    return num_zeroes + max_new_zeroes


if __name__ == '__main__':
    print find_max_zeroes_we_can_get([0, 1, 0, 0, 1, 1, 0])
