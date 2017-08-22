"""
http://www.geeksforgeeks.org/print-all-n-digit-numbers-whose-sum-of-digits-equals-to-given-sum/
"""


def print_num(num):
    s = map(str, num)
    print ''.join(s),


def find_nums(n, k, num, idx):
    if k < 0 or idx > n:
        return

    if idx == n:
        if k == 0:
            print_num(num)

        return

    for i in range(10):
        num[idx] = i
        find_nums(n, k - i, num, idx + 1)


def find_n_digits_nums_with_sum(n, k):
    num = [0 for i in range(n)]

    for i in range(1, 10):
        num[0] = i
        find_nums(n, k - i, num, 1)


if __name__ == '__main__':
    find_n_digits_nums_with_sum(3, 10)
    print ''
    print ''
    find_n_digits_nums_with_sum(2, 3)
