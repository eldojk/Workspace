"""
msft, amzn

http://www.geeksforgeeks.org/dynamic-programming-set-15-longest-bitonic-subsequence/
"""


def longest_increasing_sub_sequence(array):
    dp = [1 for i in array]

    for i in range(len(array)):
        for j in range(i):

            if array[j] < array[i] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1

    return dp


def longest_decreasing_sub_sequence(array):
    dp = [1 for i in array]

    for i in reversed(range(len(array))):
        for j in range(i, len(array)):

            if array[j] < array[i] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1

    return dp


def longest_bitonic_sequence_length(array):
    lis = longest_increasing_sub_sequence(array)
    lds = longest_decreasing_sub_sequence(array)

    max_found = 1

    for i in range(len(array)):
        lbs_len = lis[i] + lds[i] - 1
        max_found = max(max_found, lbs_len)

    return max_found


if __name__ == '__main__':
    print longest_bitonic_sequence_length([1, 11, 2, 10, 4, 5, 2, 1])
    print longest_bitonic_sequence_length([12, 11, 40, 5, 3, 1])
    print longest_bitonic_sequence_length([80, 60, 30, 40, 20, 10])
