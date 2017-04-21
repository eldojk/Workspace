"""
amzn

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


if __name__ == '__main__':
    m = [
        [1, 0, 0, 1],
        [0, 0, 1, 0],
        [0, 0, 0, 0]
    ]

    set_matrix(m)
    print_matrix(m)