"""
amzn

http://www.geeksforgeeks.org/maximum-sum-such-that-no-two-elements-are-adjacent/

M(i) = max(arr[i] + M(i-2), M(i-1))
where M(i) is the maximum sum where i is the last element of the sub sequence
"""


def maximum_sum_non_adjacent(array):
    dp = [el for el in array]

    dp[1] = max(array[0], array[1])

    current_max_sum = dp[1]

    for i in range(2, len(array)):
        dp[i] = max(
            array[i] + dp[i - 2],
            dp[i - 1]
        )

        current_max_sum = max(dp[i], current_max_sum)

    return current_max_sum


if __name__ == '__main__':
    print maximum_sum_non_adjacent([5, 5, 10, 100, 10, 5])
    print maximum_sum_non_adjacent([1, 2, 3])
    print maximum_sum_non_adjacent([1, 20, 3])