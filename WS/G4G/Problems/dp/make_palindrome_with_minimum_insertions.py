# coding=utf-8
"""
http://www.geeksforgeeks.org/dynamic-programming-set-28-minimum-insertions-to-form-a-palindrome/

ab: Number of insertions required is 1. bab
    aa: Number of insertions required is 0. aa
    abcd: Number of insertions required is 3. dcbabcd
    abcda: Number of insertions required is 2. adcbcda which is same as number of insertions in the substring bcd(Why?).
    abcde: Number of insertions required is 4. edcbabcde

minInsertions(str[l+1…..h-1]) if str[l] is equal to str[h]  => clear right?

else =>
min(minInsertions(str[l…..h-1]), minInsertions(str[l+1…..h])) + 1

why? coz, lets ley minInsertion(l, h - 1) takes k insertions to be a palindrome, assume it is abcd. so we make abc a
palindrome -> 'cbaabc'd, now we just need to add d in front of string !!! :)
so if minIns(l, h-1) = k, and minIns(l+1, h)= m, lets choose minimum of k and m since we need to minimise insertions...
i.e., either k + 1 or m +1 whichever is smaller
"""
from G4G.Problems.dp.min_matrix_cost_path_to_mn import print_matrix


def min_insertions_for_palindrome(string):
    dp = [[0 for i in string] for j in string]
    N = len(string)

    for i in range(1, N):
        dp[i - 1][i] = 0 if string[i - 1] == string[i] else 1

    for l in range(2, N):
        for i in range(N):

            j = i + l

            if j < N:

                if string[i] == string[j]:
                    dp[i][j] = dp[i + 1][j - 1]

                else:
                    dp[i][j] = 1 + min(
                        dp[i][j - 1],
                        dp[i + 1][j]
                    )

    # print_matrix(dp)
    return dp[0][N - 1]


if __name__ == '__main__':
    print min_insertions_for_palindrome('abcde')
