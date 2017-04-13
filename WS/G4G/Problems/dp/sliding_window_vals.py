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

Also
http://www.geeksforgeeks.org/sum-minimum-maximum-elements-subarrays-size-k/

Given an array of both positive and negative integers, the task is to compute sum of minimum and maximum elements of all sub-array of size k.

Examples:

Input : arr[] = {2, 5, -1, 7, -3, -1, -2}
        K = 4
Output : 18
Explanation : Subarrays of size 4 are :
     {2, 5, -1, 7},   min + max = -1 + 7 = 6
     {5, -1, 7, -3},  min + max = -3 + 7 = 4
     {-1, 7, -3, -1}, min + max = -3 + 7 = 4
     {7, -3, -1, -2}, min + max = -3 + 7 = 4
     Sum of all min & max = 6 + 4 + 4 + 4
                          = 18
"""
from copy import copy
from G4G.Problems.dp.min_matrix_cost_path_to_mn import print_matrix

"""
This is bad, use a bst
"""
def sliding_window_sizes(array, sw_size):
    min_sw_sizes = [[0 for i in array] for j in range(sw_size)]
    min_sw_sizes[0] = copy(array)

    max_sw_sizes = [[0 for i in array] for j in range(sw_size)]
    max_sw_sizes[0] = copy(array)

    for i in range(1, sw_size):
        for j in range(len(array)):
            # consider, sliding window size i - 1, ending one element before (j - 1) and add ith element thus
            # increasing the size. it'll be the newly added element is that elements is greater than max or less
            # than min
            min_sw_sizes[i][j] = min(min_sw_sizes[i - 1][j - 1], array[j])
            max_sw_sizes[i][j] = max(max_sw_sizes[i - 1][j - 1], array[j])

    return min_sw_sizes[sw_size - 1], max_sw_sizes[sw_size - 1]


if __name__ == '__main__':
    arr = [2, 5, -1, 7, -3, -1, -2]
    k = 4
    _min_sw, _max_sw = sliding_window_sizes(arr, k)

    reqd_sum = 0
    for i in range(k - 1, len(arr)):
        _sum = _max_sw[i] + _min_sw[i]
        print _sum,
        reqd_sum += _sum

    print ''
    print reqd_sum