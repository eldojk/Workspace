"""
n!

It is assumed that the values are positive integers
"""


def iterative_factorial(number):
    factorial = 1
    i = 1

    while i <= number:
        factorial = factorial * i
        i += 1

    return factorial


def recursive_factorial(number):
    # base case
    if number <= 1:
        return 1

    # recursive case
    return number * recursive_factorial(number - 1)
