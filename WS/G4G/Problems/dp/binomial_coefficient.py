"""
http://www.geeksforgeeks.org/dynamic-programming-set-9-binomial-coefficient/

A binomial coefficient C(n, k) also gives the number of ways, disregarding order, that k objects can be chosen from
among n objects; more formally, the number of k-element subsets (or k-combinations) of an n-element set.

C(n, k) = C(n-1, k-1) + C(n-1, k)
C(n, 0) = C(n, n) = 1

    0   1   2
0   1   x   x
1   1   1   x
2   1   2   1
3   1   3   3
4   1   4   6
"""
from G4G.Problems.dp.min_matrix_cost_path_to_mn import print_matrix


def binomial_coefficient(n, k):
    bc = [range(k+1) for i in range(n + 1)]

    for i in range(min(n, k) + 1):
        bc[i][i] = 1

    for i in range(n + 1):
        bc[i][0] = 1

    for i in range(n + 1):
        for j in range(k + 1):

            if j < i and j != 0:

                bc[i][j] = bc[i-1][j-1] + bc[i-1][j]

    return bc[n][k]


if __name__ == '__main__':
    print binomial_coefficient(4, 2)
    print binomial_coefficient(5, 2)