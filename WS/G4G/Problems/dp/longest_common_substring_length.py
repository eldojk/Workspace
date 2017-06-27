"""
abcde and abc -> 3

we will place abc at positions starting at 0 to 2. i.e,
abcde   abcde   abcde
abc      abc      abc

and at every step we will try to find the length of the longest common substring with the
last char as the ending character we are considering

dp(i, j) -> lcs of string 1 and string 2 when we try to match ith character of string1
to jth character of string 2

here we vary i through length of string 1 and for each of them we vary j
through length of string 2

dp(i,j) = 1 + dp(i - 1, j -1) if string1[i] == string2[j]
        = dp(i - 1, j -1) otherwise

    0   a   b   c   d   e
    0   0   0   0   0   0
a   0   1   0   0   0   0
b   0   0   2   0   0   0
c   0   0   0   3   0   0
"""
from G4G.Problems.dp.min_matrix_cost_path_to_mn import print_matrix


def longest_common_substring(s1, s2):
    dp = [[0 for i in range(len(s1) + 1)] for j in range(len(s2) + 1)]

    for i in range(1, len(s2) + 1):
        for j in range(1, len(s1) + 1):

            if s1[j - 1] == s2[i - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]

            else:
                dp[i][j] = dp[i - 1][j - 1]

    # print_matrix(dp)
    return max([max(row) for row in dp])


if __name__ == '__main__':
    print longest_common_substring('OldSite:GeeksforGeeks.org', 'NewSite:GeeksQuiz.com')
