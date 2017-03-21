"""
http://www.geeksforgeeks.org/dynamic-programming-set-14-maximum-sum-increasing-subsequence/

if input is {1, 101, 2, 3, 100, 4, 5}, then output should be 106 (1 + 2 + 3 + 100)

same approach as longest increasing sub sequence, here instead of tracking the lengths of the sub sequence,
we will track the sum of elements in it
"""
from copy import copy


def maximum_increasing_sub_sequence_sum(array):
    sums = copy(array)

    # starting from second element
    for i in range(1, len(array)):

        # every preceding element
        for j in range(i):

            if array[j] < array[i]:
                result = sums[j] + array[i]

                if result > sums[i]:
                    sums[i] = result

    return max(sums)


if __name__ == '__main__':
    print maximum_increasing_sub_sequence_sum([1, 101, 2, 3, 100, 4, 5])
