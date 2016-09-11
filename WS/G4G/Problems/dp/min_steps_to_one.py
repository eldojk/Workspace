"""
Given a number n, we can do any of these three ops:
- subtract 1
- divide by 2
- divide by 3
using a combination of these ops, reduce the number to 1 by using the least ops

if the sub problem computing this, min_steps(i) => lets say min_steps(j) is optimal for j < i, then we know that
min_steps(i) = 1 + min_steps(j)
"""
from sys import maxint


def min_steps_to_n(n):
    if n == 1:
        return 0

    min_steps_arr = [0, 0] + [maxint for i in range(n)]  # [1, maxint, maxint ....] of length n

    for i in range(2, n + 1):
        min_steps_arr[i] = min_steps_arr[i - 1] + 1

        if i % 2 == 0:
            min_steps_arr[i] = min(min_steps_arr[i], 1 + min_steps_arr[i / 2])

        if i % 3 == 0:
            min_steps_arr[i] = min(min_steps_arr[i], 1 + min_steps_arr[i / 3])

    return min_steps_arr[n]
