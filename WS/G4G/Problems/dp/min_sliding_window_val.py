"""
Given an Array of size n and a sliding window of size k (k << n), If the sliding window slides from the beginning of
the array, Find the minimum of the values at each position of the window. Find the minimum possible value at all
positions

[10	20	30	50	10	70	30	50	80	20	10], 3
[0	0	10	20	10	10	10	30	30	20	10]

	    10	20	30	50	10	70	30	50	80	20	10
0(1)	10	20	30	50	10	70	30	50	80	20	10
1(2)	0	10	20	30	10	10	30	30	50	20	10
2(3)	0	0	10	20	10	10	10	30	30	20	10

minimum in sliding window of size k = MIN (minimum of sliding window of size k-1, array[k])
"""
from copy import copy


def find_min_sliding_window(array, sw_size):
    sw_sizes = [[None for i in array] for j in range(sw_size)]
    sw_sizes[0] = copy(array)

    for i in range(1, sw_size):
        for j in range(i, len(array)):
            sw_sizes[i][j] = min(sw_sizes[i - 1][j - 1], array[j])

    return sw_sizes[sw_size - 1]


print find_min_sliding_window([10, 20, 30, 50, 10, 70, 30, 50, 80, 20, 10], 3)
