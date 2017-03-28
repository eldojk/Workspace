"""
12345
+**-

Given an expression number of different ways to evaluate the expression.
Exp. 1+2*3, can be evaluated as (1+2)*3 or 1+(2*3)
Later he asked me to find out all the possible answers as well.

	1	2	3	4	5
1	1	1	2	5	8
2		1	1	2	5
3			1	1	2
4				1	1
5					1


num_ways[1,j] = sum(num[i,k] * num[k+1,j] for all k in (i,j))

"""
from G4G.Problems.dp.min_matrix_cost_path_to_mn import print_matrix


def num_ways_to_parenthesize(string):
    operands = [string[i] for i in range(len(string)) if i%2 == 0]
    operators = [string[i] for i in range(len(string)) if i%2 != 0]

    dp = [[1 for i in operands] for j in operands]

    for l in range(2, len(operands)):
        for i in range(len(operands)):

            j = i + l

            if j < len(operands):
                dp[i][j] = sum(
                    [dp[i][k] * dp[k + 1][j] for k in range(i, j)]
                )

    print_matrix(dp)
    return dp[0][len(operands) - 1]


if __name__ == '__main__':
    print num_ways_to_parenthesize('1+2*3*4-5+9')
