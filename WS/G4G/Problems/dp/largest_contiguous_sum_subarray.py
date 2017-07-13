"""
msft, amzn

http://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
"""


def largest_contiguous_sum(array):
    dp = [i for i in array]

    max_sum = dp[0]
    for i in range(1, len(array)):
        dp[i] = max(
            dp[i - 1] + array[i],
            array[i]
        )

        max_sum = max(max_sum, dp[i])

    return max_sum


if __name__ == '__main__':
    print largest_contiguous_sum([-2, -3, 4, -1, -2, 1, 5, -3])