# coding=utf-8
"""
http://www.geeksforgeeks.org/longest-repeating-subsequence/

Input: str = "abc"
Output: 0
There is no repeating subsequence

Input: str = "aab"
Output: 1
The two sub sequences are 'a'(first) and 'a'(second).
Note that 'b' cannot be considered as part of subsequence
as it would be at same index in both.

Input: str = "aabb"
Output: 2

Input: str = "axxxy"
Output: 2

This problem is just the modification of Longest Common Subsequence problem. The idea is to find the LCS(str, str)
where str is the input string with the restriction that when both the characters are same, they shouldn’t be on the
same index in the two strings.
"""


def longest_repeating_sub_sequence_length(string):
    n = len(string)
    lcs_dp = [[0 for i in range(n + 1)] for j in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):

            # equating last element
            if string[i - 1] == string[j - 1] and i != j:

                # 1 + lcs of last char removed from both strings
                lcs_dp[i][j] = 1 + lcs_dp[i - 1][j - 1]

            else:
                lcs_dp[i][j] = max(
                    lcs_dp[i - 1][j],  # last char removed from array1
                    lcs_dp[i][j - 1]  # last char removed from array2
                )

    # print_matrix(lcs_dp)
    return lcs_dp[n][n]


if __name__ == '__main__':
    print longest_repeating_sub_sequence_length('axxxy')
