# coding=utf-8
"""
http://www.geeksforgeeks.org/total-number-of-non-decreasing-numbers-with-n-digits/

Let count ending with digit ‘d’ and length n be count(n, d)
count(n, d) = ∑ (count(n-1, i)) where i varies from 0 to d
Total count = ∑ count(n-1, d) where d varies from 0 to n-1
"""


def count_of_numbers(n):
    dp = [[0 for length in range(n + 1)] for ending_digit in range(10)]

    # of length 1
    for ending_digit in range(10):
        dp[ending_digit][1] = 1

    for digit in range(10):
        for length in range(2, n + 1):

            for x in range(digit + 1):
                dp[digit][length] += dp[x][length - 1]

    # count all possible ending digits
    count = 0
    for ending_digit in range(10):
        count += dp[ending_digit][n]

    return count


if __name__ == '__main__':
    print count_of_numbers(3)
