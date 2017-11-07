"""
amzn

http://qa.geeksforgeeks.org/5597/reduce-the-given-number-to-1-in-minimum-steps
Given a number n, we can do any of these three ops:
- subtract 1
- divide by 2
- divide by 3
using a combination of these ops, reduce the number to 1 by using the least ops

if the sub problem computing this, min_steps(i) => lets say min_steps(j) is optimal for j < i, then we know that
min_steps(i) = 1 + min_steps(j)
"""


def min_steps_memoized(n, dp):
    if n == 1:
        return 0

    if dp[n] != -1:
        return dp[n]

    res = 1 + min_steps_memoized(n - 1, dp)

    if n % 2 == 0:
        res = min(
            res,
            1 + min_steps_memoized(n / 2, dp)
        )

    if n % 3 == 0:
        res = min(
            res,
            1 + min_steps_memoized(n / 3, dp)
        )

    dp[n] = res
    return res


def min_steps_to_1_memo(n):
    dp = [-1 for i in range(n + 1)]
    return min_steps_memoized(n, dp)


if __name__ == '__main__':
    print min_steps_to_1_memo(5)
