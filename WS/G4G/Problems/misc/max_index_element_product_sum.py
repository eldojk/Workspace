# coding=utf-8
"""
amzn

http://www.geeksforgeeks.org/maximum-sum-iarri-among-rotations-given-array/

The idea is to compute value of a rotation using value of previous rotation. When we rotate an array by one, following
changes happen in sum of i*arr[i].
1) Multiplier of arr[i-1] changes from 0 to n-1, i.e., arr[i-1] * (n-1) is added to current value.
2) Multipliers of other terms is decremented by 1. i.e., (cum_sum – arr[i-1]) is subtracted from current value where
cum_sum is sum of all numbers.
next_val = curr_val - (cum_sum - arr[i-1]) + arr[i-1] * (n-1);
"""


def max_sum(array):
    n = len(array)

    cum_sum = 0
    for c in array:
        cum_sum += c

    curr_val = 0
    for i in range(n):
        curr_val += i * array[i]

    result = curr_val

    for i in range(1, n):
        next_val = curr_val - (cum_sum - array[i - 1]) + (array[i - 1] * (n - 1))

        curr_val = next_val

        result = max(result, next_val)

    return result


if __name__ == '__main__':
    print max_sum([8, 3, 1, 2])