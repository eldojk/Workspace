"""
http://www.geeksforgeeks.org/count-even-length-binary-sequences-with-same-sum-of-first-and-second-half-bits/

Examples:

Input:  n = 1
Output: 2
There are 2 sequences of length 2*n, the
sequences are 00 and 11

Input:  n = 2
Output: 2
There are 6 sequences of length 2*n, the
sequences are 0101, 0110, 1010, 1001, 0000
and 1111

1) First and last bits are same, remaining n-1 bits on both sides should also have the same sum.
2) First bit is 1 and last bit is 0, sum of remaining n-1 bits on left side should be 1 less than the sum n-1 bits on
right side.
2) First bit is 0 and last bit is 1, sum of remaining n-1 bits on left side should be 1 more than the sum n-1 bits on
right side.
"""

MEMO = None


def count_sequence(n, diff):
    """
    count of all sequences

    :param n:
    :param diff: diff of left sum and right sum
    :return:
    """
    global MEMO

    if n == 1 and diff == 0:
        return 2

    if n == 1 and abs(diff) == 1:
        return 1

    # since diff can be negative we add n to it
    if MEMO[n][n + diff] != -1:
        return MEMO[n][n + diff]
    # count for:
    # left and right bits equal (both being 1 and 0 -> 2 cases,
    # left is 1 and right is 0
    # right is 1 and left is zero
    MEMO[n][n + diff] = 2 * count_sequence(n - 1, diff) + \
                        count_sequence(n - 1, diff - 1) + \
                        count_sequence(n - 1, diff + 1)

    return MEMO[n][n + diff]


def count_sequences_with_sum_on_left_and_right_equal(n):
    global MEMO
    MEMO = [[-1 for i in range(n + 1)] for j in range(2 * n + 1)]

    return count_sequence(n, 0)


if __name__ == '__main__':
    print count_sequences_with_sum_on_left_and_right_equal(2)
