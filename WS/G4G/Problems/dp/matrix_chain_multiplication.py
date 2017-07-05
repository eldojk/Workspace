"""
amzn, msft

Substring model:

DP(i, j) = cost of multiplying matrices across i through j
DP(i, j) = MIN( DP(i, k) + DP(k+1, j) + Cost_of_multiplying these two subsets)

	0	1	2	3
0	0	36	84	124
1		0	72	132
2			0	120
3				0

"""


def calc_cost(matrices, i, k, j):
    if i == j:
        return 0

    p = matrices[i][0]
    q = matrices[k][1]
    r = matrices[j][1]

    return p * q * r


def minimum_value_of_chain_multiplication(matrices):
    cost = [[100000 for i in range(len(matrices))] for j in range(len(matrices))]

    # Cost of multiplying matrix to itself is initialized to zero
    for i in range(len(matrices)):
        cost[i][i] = 0

    max_index = len(matrices) - 1

    for l in range(1, len(matrices)):
        for i in range(len(matrices)):

            j = i + l

            if j <= max_index:
                # cost of multiplying matrices i through j = cost of i through k + cost of k + 1 through j
                # + cost of multiplying the above to results for all k between i and j
                cost[i][j] = min([cost[i][k] + cost[k + 1][j] + calc_cost(matrices, i, k, j) for k in range(i, j)])

    return cost[0][max_index]


if __name__ == '__main__':
    print minimum_value_of_chain_multiplication([(2, 3), (3, 6), (6, 4), (4, 5)])
