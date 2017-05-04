"""
https://www.hackerearth.com/practice/math/number-theory/primality-tests/tutorial/
"""


def is_prime(n):
    i = 2

    while i ** 2 <= n:
        if n % i == 0:
            return False

    return True
