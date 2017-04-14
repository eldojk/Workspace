# coding=utf-8
"""
http://www.geeksforgeeks.org/count-number-of-ways-to-partition-a-set-into-k-subsets/

Input: n = 3, k = 2
Output: 3
Explanation: Let the set be {1, 2, 3}, we can partition
             it into 2 subsets in following ways
             {{1,2}, {3}},  {{1}, {2,3}},  {{1,3}, {2}}

Input: n = 3, k = 1
Output: 1
Explanation: There is only one way {{1, 2, 3}}

Let S(n, k) be total number of partitions of n elements into k sets.
S(n, k) = k*S(n-1, k) + S(n-1, k-1)

When we add a (n+1)’th element to k partitions, there are two possibilities.
1) It is added as a single element set to existing partitions, i.e, S(n, k-1)
2) It is added to all sets of every partition, i.e., k*S(n, k)
"""


def count_partitions(n, k):
    dp = [[0 for i in range(k + 1)] for j in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, k + 1):

            if j == 1 or i == j:  # base cases
                dp[i][j] = 1

            else:
                dp[i][j] = j * dp[i - 1][j] + dp[i - 1][j - 1]

    return dp[n][k]


if __name__ == '__main__':
    print count_partitions(5, 2)