"""
Recursion
"""
from __future__ import division


def power(x, n):
    # base case 1
    if n == 0:
        return 1;

    # iterative case
    if n > 0:
        return x * power(x, n - 1)

    if n < 0:
        n = (n * -1)
        pwr = power(x, n)
        return 1 / pwr
