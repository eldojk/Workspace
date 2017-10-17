# coding=utf-8
"""
amzn

http://www.geeksforgeeks.org/minimum-number-of-squares-whose-sum-equals-to-given-number-n/

A number can always be represented as a sum of squares of other numbers.
Note that 1 is a square and we can always break a number as (1*1 + 1*1 + 1*1 + …).
Given a number n, find the minimum number of squares that sum to X.

Examples:

Input:  n = 100
Output: 1
100 can be written as 102. Note that 100 can also be
written as 52 + 52 + 52 + 52, but this
representation requires 4 squares.

Input:  n = 6
Output: 3
"""


def min_squares(n):
    if n <= 0:
        return 0

    dp = range(n + 1)

    for i in range(4, n + 1):

        j = 1
        while j < i:
            square = j ** 2

            if square > i:
                break

            dp[i] = min(
                dp[i],
                dp[i - square] + 1
            )

            j += 1

    return dp[n]


if __name__ == '__main__':
    print min_squares(6)
