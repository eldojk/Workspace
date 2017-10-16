"""
amzn

#tricky
http://www.geeksforgeeks.org/length-of-the-longest-arithmatic-progression-in-a-sorted-array/
^ read the explanation
"""


def length_of_longest_ap(array):
    n = len(array)

    if n <= 2:
        return n

    dp = [[0 for i in range(n)] for j in range(n)]
    max_length = 2

    # Base case, if n-1th element is the last element in ap, then length is 2
    # Read the link to understand
    for i in range(n):
        dp[i][n - 1] = 2

    j = n - 2
    while j >= 1:

        # search i and k for this j
        i = j - 1
        k = j + 1

        while i >= 0 and k < n:

            if array[i] + array[k] < array[j] * 2:
                k += 1

            elif array[i] + array[k] > array[j] * 2:
                i -= 1

            else:
                # found
                dp[i][j] = dp[j][k] + 1
                max_length = max(max_length, dp[i][j])

                i -= 1
                k += 1

        # If the loop was stopped due to k becoming n - 1
        while i >= 0:
            dp[i][j] = 2
            i -= 1

        j -= 1

    return max_length


if __name__ == '__main__':
    print length_of_longest_ap([1, 7, 10, 13, 14, 19])
    print length_of_longest_ap([1, 7, 10, 15, 27, 29])
    print length_of_longest_ap([2, 4, 6, 8, 10])
