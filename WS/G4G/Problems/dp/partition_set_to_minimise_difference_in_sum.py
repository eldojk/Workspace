"""
amzn

#tricky
http://www.geeksforgeeks.org/partition-a-set-into-two-subsets-such-that-the-difference-of-subset-sums-is-minimum/

Input:  arr[] = {1, 6, 11, 5}
Output: 1
Explanation:
Subset1 = {1, 5, 6}, sum of Subset1 = 12
Subset2 = {11}, sum of Subset2 = 11

The task is to divide the set into two parts.
We will consider the following factors for dividing it.
Let
  dp[i+1][j+1] = {true if some subset from 1st to i'th has a sum
                      equal to j
                   0 otherwise}

    i ranges from {1..n}
    j ranges from {0..(sum of all elements)}

So
    dp[i+1][j+1]  will be true if
    1) The sum j is achieved including i'th item
    2) The sum j is achieved excluding i'th item.

Let sum of all the elements be S.

To find Minimum sum difference, w have to find j such
that Min{(sum - j) - j  : dp[n][j]  == true } == (sum - 2*j)
    where j varies from 0 to sum/2

The idea is, sum of S1 is j and it should be closest
to sum/2, i.e., 2*j should be closest to sum.

    0   1   2   3   4   5
0   t   f   f   f   f   f
1   t   t   f   f   f   f
5   t   t   f   f   f   t
6   t   t   f   f   f   t
11
"""
from sys import maxint

from G4G.Problems.dp.subset_sum import print_matrix_boolean


def partition_minimum_sum(array):
    array.sort()
    array = [0] + array
    sm = sum(array)
    dp = [[False for i in range(sm + 1)] for j in array]

    dp[0][0] = True

    for i in range(1, len(array)):
        for j in range(sm + 1):

            if j < array[i]:  # can't include ith element if its value is greater than target sum
                dp[i][j] = dp[i - 1][j]
            else:
                # here we choose or not choose i'th element
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - array[i]]

    # print_matrix_boolean(dp)
    n = len(array) - 1
    min_sum = maxint

    # minimising s - 2*j
    j = int(sm/2)
    while j >= 0:
        if dp[n][j]:
            # sum1 = j, other sum = sm - j
            # diff of sum1 and sum2 = (sm - j) - j = sm - 2j
            curr_diff = sm - 2*j

            if curr_diff < min_sum:
                min_sum = curr_diff

        j -= 1

    return min_sum


if __name__ == '__main__':
    print partition_minimum_sum([1, 6, 11, 5])
    print partition_minimum_sum([3, 1, 4, 2, 2, 1])
