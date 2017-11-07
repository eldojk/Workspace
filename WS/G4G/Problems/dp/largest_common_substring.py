"""
amzn

http://algorithms.tutorialhorizon.com/dynamic-programming-longest-common-substring/#attachment_1507

Largest common substring

Base Cases: If any of the string is null then LCS will be 0.
Check if ith character in one string A is equal to jth character in string B

Case 1: both characters are same
LCS[i][j] = 1 + LCS[i-1][j-1] (add 1 to the result and remove the last
character from both the strings and check the result for the smaller string.)

Case 2: both characters are not same.
LCS[i][j] = 0

At the end, traverse the matrix and find the maximum element in it,
This will the length of Longest Common Substring.
"""


def largest_common_substring(str1, str2):
    m = len(str1)
    n = len(str2)

    dp = [[0 for i in range(n + 1)] for j in range(m + 1)]

    max_len = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):

            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
                max_len = max(
                    max_len,
                    dp[i][j]
                )

    return max_len


if __name__ == '__main__':
    print largest_common_substring('tutorialhorizon',
                                   'dynamictutorialProgramming')
