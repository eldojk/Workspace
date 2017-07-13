"""
https://www.hackerearth.com/practice/math/number-theory/primality-tests/tutorial/

primes are of the form 6k+1 or 6k-1 apparently
"""


def is_prime(n):
    i = 2

    while i ** 2 <= n:
        if n % i == 0:
            return False

        i += 1

    return True
