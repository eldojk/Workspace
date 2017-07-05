"""
amzn, msft

http://www.geeksforgeeks.org/a-boolean-matrix-question/

1) Create two temporary arrays row[M] and col[N]. Initialize all values of row[] and col[] as 0.
2) Traverse the input matrix mat[M][N]. If you see an entry mat[i][j] as true, then mark row[i] and col[j] as true.
3) Traverse the input matrix mat[M][N] again. For each entry mat[i][j], check the values of row[i] and col[j].
If any of the two values (row[i] or col[j]) is true, then mark mat[i][j] as true.
"""
from G4G.Problems.dp.min_matrix_cost_path_to_mn import print_matrix


def set_matrix(matrix):
    ro = [False for i in matrix]
    col = [False for j in matrix[0]]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):

            if matrix[i][j] == 1:
                ro[i] = True
                col[j] = True

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if ro[i] or col[j]:
                matrix[i][j] = 1

    return matrix


def set_matrix_constant_extra_space(matrix):
    r_flag = False
    c_flag = False

    for i in range(len(matrix)):
        if matrix[i][0] == 1:
            c_flag = True
            break

    for j in range(len(matrix[0])):
        if matrix[0][j] == 1:
            r_flag = True
            break

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):

            if matrix[i][j] == 1:
                matrix[0][j] = 1
                matrix[i][0] = 1

    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):

            if matrix[i][0] == 1 or matrix[0][j] == 1:
                matrix[i][j] = 1

    if r_flag:
        for i in range(len(matrix[0])):
            matrix[0][i] = 1

    if c_flag:
        for i in range(len(matrix)):
            matrix[i][0] = 1

    return matrix


if __name__ == '__main__':
    m = [
        [1, 0, 0, 1],
        [0, 0, 1, 0],
        [0, 0, 0, 0]
    ]

    set_matrix(m)
    print_matrix(m)

    print ''

    m = [
        [1, 0, 0, 1],
        [0, 0, 1, 0],
        [0, 0, 0, 0]
    ]
    set_matrix_constant_extra_space(m)
    print_matrix(m)