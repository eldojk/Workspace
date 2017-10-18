"""
amzn

http://www.geeksforgeeks.org/dynamic-programming-set-17-palindrome-partitioning/

similar to matrix chain multiplication
We try making cuts at all possible places, recursively calculate the cost for each cut and return the minimum value.
if str(m, n) is pal, then 0
else cost[m,n] = MIN( 1 + cost[m, i] + cost[i+1, n] for all i in range(m, n) )

b b	a b	a b	a
0 0 1 0 1 0 1
0 0 0 1 0 1 0
0 0 0 0 1 0 1
0 0 0 0 0 1 0
0 0 0 0 0 0 1
0 0 0 0 0 0 0
"""
from G4G.Problems.dp.min_matrix_cost_path_to_mn import print_matrix


def is_palindrome(string, i, j):
    while i < j:
        if string[i] != string[j]:
            return False

        i += 1
        j -= 1

    return True


def min_cost(string):
    n = len(string) - 1

    cost = [[0 for i in string] for j in string]

    for l in range(1, len(string)):
        for i in range(len(string)):
            j = i + l

            if j <= n:
                if is_palindrome(string, i, j):
                    cost[i][j] = 0

                else:
                    cost[i][j] = min([1 + cost[i][k] + cost[k + 1][j] for k in range(i, j)])

    return cost[0][n]


if __name__ == '__main__':
    print min_cost('bbababa')
    print min_cost('ababbbabbababa')
