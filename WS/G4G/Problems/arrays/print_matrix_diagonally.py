"""
http://www.geeksforgeeks.org/print-matrix-diagonal-pattern/
http://www.geeksforgeeks.org/zigzag-or-diagonal-traversal-of-matrix/

print indices in this order
00
01	10
20	11	02
12	21
22
"""


def print_diag(matrix, m, i, j, is_rev):
    limit = max(i, j) + 1

    if is_rev:
        a = j
        b = i
        while a < limit and b >= 0:
            print matrix[a][b],
            a += 1
            b -= 1

        return

    while i >= 0 and j < limit:
        print matrix[i][j],
        i -= 1
        j += 1


def print_diagonal(matrix, m):
    if m <= 0:
        return

    i = 0
    j = 0

    flag = True
    while i < m:
        flag = not flag
        print_diag(matrix, m, i, j, flag)
        i += 1

    i -= 1
    j += 1
    while j < m:
        flag = not flag
        print_diag(matrix, m, i, j, flag)
        j += 1


if __name__ == '__main__':
    mt = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print_diagonal(mt, 3)

    print ''

    mt = [
        [1,  2,  3,  10],
        [4,  5,  6,  11],
        [7,  8,  9,  12],
        [13, 14, 15, 16]
    ]

    print_diagonal(mt, 4)
