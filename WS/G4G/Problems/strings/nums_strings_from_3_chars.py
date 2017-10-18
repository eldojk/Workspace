# coding=utf-8
"""
amzn

Given 3 characters a, b, c, find the number of strings of length n that can be formed from these 3 characters
given that; we can use ‘a’ as many times as we want, ‘b’ maximum once, and ‘c’ maximum twice.
"""


def dp(n, a, b, c):
    if n == 0:
        return 1

    res = dp(n - 1, a, b, c)
    if b != 0:
        res += dp(n - 1, a, b - 1, c)

    if c != 0:
        res += dp(n - 1, a, b, c - 1)

    return res


def num_strings(n):
    if n == 0:
        return 0

    return dp(n, n, 1, 2)


if __name__ == '__main__':
    print num_strings(2)
    print ''


"""
PRINT 'EM
"""


def print_strings(n, a, b, c, curr):
    if n == 0:
        print ''.join(curr),
        return

    curr.append('a')
    print_strings(n - 1, a, b, c, curr)
    curr.pop()

    if b != 0:
        curr.append('b')
        print_strings(n - 1, a, b - 1, c, curr)
        curr.pop()

    if c != 0:
        curr.append('c')
        print_strings(n - 1, a, b, c - 1, curr)
        curr.pop()


if __name__ == '__main__':
    print_strings(3, 2, 2, 1, [])
