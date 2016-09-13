"""
In an NxN matrix, set the all elements in row and column of an element to 0 if we find an element to be zero
CTIC 180 #1.7
"""


def zero_ify(matrix, n):
    rows = set()
    cols = set()

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)

    for r in rows:
        for col in range(n):
            matrix[r][col] = 0

    for c in cols:
        for row in range(n):
            matrix[row][c] = 0

    return matrix
