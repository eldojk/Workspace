"""
Find last non zero digit of factorial

"""


def get_last_non_zero_digit(n1, n2):
    prod = n1 * n2
    while prod % 10 == 0:
        prod /= 10

    return prod % 10


def last_non_zero_digit(n):

    i = 1
    last_digit = 1

    while i <= n:
        last_digit = get_last_non_zero_digit(last_digit, i)
        i += 1

    return last_digit


if __name__ == '__main__':
    print last_non_zero_digit(12)
