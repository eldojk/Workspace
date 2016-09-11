"""
Finding the nth fibonacci number

F(n) = F(n-1) + F(n-2)
i.e. nth fibonacci number is the sum of the n-1th and n-2th numbers. So we need to know the previous two fibonacci
numbers to compute the current number
"""


def fibonacci_number(n):
    if n <= 1:
        return n

    p2 = 0
    p1 = 1
    fib = None
    for i in range(2, n + 1):
        fib = p2 + p1
        p2 = p1
        p1 = fib

    return fib
