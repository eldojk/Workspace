"""
amzn

http://www.geeksforgeeks.org/dynamic-programming-set-37-boolean-parenthesization-problem/

	t	t	f	t
t	1   1   1   4
t   0   1   0   2
f   0   0   0   1
t   0   0   0   1

http://people.cs.clemson.edu/~bcdean/dp_practice/dp_9.swf
"""
from G4G.Problems.dp.min_matrix_cost_path_to_mn import print_matrix


def num_ways(operands, operators):
    T = [[0 for i in operands] for j in operands]
    F = [[0 for i in operands] for j in operands]

    for i in range(len(operands)):
        T[i][i] = 1 if operands[i] == 'T' else 0
        F[i][i] = 1 if operands[i] == 'F' else 0

    for l in range(1, len(operands)):
        for i in range(len(operands)):
            j = i + l

            if j < len(operands):
                for k in range(i, j):
                    total_ik = T[i][k] + F[i][k]
                    total_kj = T[k + 1][j] + F[k + 1][j]

                    if operators[k] == '&':
                        T[i][j] += T[i][k] * T[k + 1][j]
                        F[i][j] += total_ik * total_kj - T[i][k] * T[k + 1][j]

                    elif operators[k] == '|':
                        F[i][j] += F[i][k] * F[k + 1][j]
                        T[i][j] += total_ik * total_kj - F[i][k] * F[k + 1][j]

                    elif operators[k] == '^':
                        T[i][j] += F[i][k] * T[k + 1][j] + T[i][k] * F[k + 1][j]
                        F[i][j] += T[i][k] * T[k + 1][j] + F[i][k] * F[k + 1][j]

    # print_matrix(T)
    return T[0][len(operands) - 1]


if __name__ == '__main__':
    print num_ways('TTFT', '|&^')
