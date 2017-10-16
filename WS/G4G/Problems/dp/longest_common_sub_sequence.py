"""
amzn, msft

http://www.geeksforgeeks.org/dynamic-programming-set-4-longest-common-subsequence/

		A	B	C	D	G	H
	0	0	0	0	0	0	0
A	0	1	1	1	1	1	1
E	0	1	1	1	1	1	1
D	0	1	1	1	2	2	2
F	0	1	1	1	2	2	2
H	0	1	1	1	2	2	3
R	0	1	1	1	2	2	3

it can be:
if last elements of both strings are equal:
    - lcs of both strings with the last char removed from them + 1
    (i.e, abc and afc with c being considered, it will be lcs of
    ab and af + 1 for the c in each string)

    - last char not equal, ABCDGH, AEDFHR will be the max of last char
    removed from either of them and the other one intact
    ie. max of [ABCDG and AEDFHR] and [ABCDGH and AEDFH] = max of AD and ADH
"""
from G4G.Problems.dp.min_matrix_cost_path_to_mn import print_matrix


def lcs_length(array1, array2):
    lcs_dp = [[0 for i in range(len(array1) + 1)] for j in range(len(array2) + 1)]

    for i in range(1, len(array2) + 1):
        for j in range(1, len(array1) + 1):

            # equating last element
            if array2[i - 1] == array1[j - 1]:

                # 1 + lcs of last char removed from both strings
                lcs_dp[i][j] = 1 + lcs_dp[i - 1][j - 1]

            else:
                lcs_dp[i][j] = max(
                    lcs_dp[i - 1][j],  # last char removed from array1
                    lcs_dp[i][j - 1]  # last char removed from array2
                )

    # print_matrix(lcs_dp)
    return lcs_dp[len(array2)][len(array1)]


if __name__ == '__main__':
    print lcs_length('ABCDGH', 'AEDFHR')


def lcs_memo(a, b, i, j, dp):
    if i == 0 or j == 0:
        return 0

    if dp[i][j] != -1:
        return dp[i][j]

    if a[i - 1] == b[j - 1]:
        dp[i][j] = 1 + lcs_memo(a, b, i - 1, j - 1, dp)

    else:
        dp[i][j] = max(
            lcs_memo(a, b, i - 1, j, dp),
            lcs_memo(a, b, i, j - 1, dp)
        )

    return dp[i][j]


if __name__ == '__main__':
    _dp = [[-1 for i in range(7)] for j in range(7)]

    print lcs_memo('ABCDGH', 'AEDFHR', 6, 6, _dp)
