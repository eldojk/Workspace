"""
http://www.geeksforgeeks.org/find-maximum-dot-product-two-arrays-insertion-0s/

Given two arrays of positive integers of size m and n where m > n. We need to maximize the dot product by inserting
zeros in the second array but we cannot disturb the order of elements.

Examples:

Input : A[] = {2, 3 , 1, 7, 8}
        B[] = {3, 6, 7}
Output : 107
Explanation : We get maximum dot product after
inserting 0 at first and third positions in
second array.
Maximum Dot Product : = A[i] * B[j]
2*0 + 3*3 + 1*0 + 7*6 + 8*7 = 107

Input : A[] = {1, 2, 3, 6, 1, 4}
        B[] = {4, 5, 1}
Output : 46
	0	2	3	1	7	8
0	0	0	0	0	0	0
3	0	6	9	9	21	24
6	0	6	24	24	51	77
7	0	6	24	31	73	107
"""
from G4G.Problems.dp.min_matrix_cost_path_to_mn import print_matrix


def max_product(array1, array2):
    dp = [[0 for i in range(len(array1) + 1)] for j in range(len(array2) + 1)]

    for i in range(1, len(array2) + 1):
        for j in range(1, len(array1) + 1):

            if j < i:
                dp[i][j] = dp[i - 1][j]  # can't use j * i if j is at a higher index than i

            else:

                dp[i][j] = max(
                    dp[i - 1][j - 1] + array1[j - 1] * array2[i - 1],  # include i * j and the value before (i-1)*(j-1)
                    dp[i][j - 1]  # not include
                )

    # print_matrix(dp)
    return dp[len(array2)][len(array1)]


if __name__ == '__main__':
    print max_product([2, 3, 1, 7, 8], [3, 6, 7])
