"""
http://www.geeksforgeeks.org/print-matrix-diagonal-pattern/

print indices in this order
00
01	10
20	11	02
12	21
22
"""


def get_indices(i, j, rev=False):
    indices = []
    limit = j - i
    k = 0

    while k <= limit:
        indices.append((i + k, j - k))
        k += 1

    if rev:
        indices.reverse()

    return indices


def print_diagonal(matrix, m):
    flag = False

    print matrix[0][0],

    for j in range(1, m):

        for tup in get_indices(0, j, rev=flag):
            p = tup[0]
            q = tup[1]
            print matrix[p][q],

        flag = not flag

    for i in range(1, m - 1):

        for tup in get_indices(i, m - 1, rev=flag):
            p = tup[0]
            q = tup[1]
            print matrix[p][q],

        flag = not flag

    print matrix[m - 1][m - 1]


if __name__ == '__main__':
    mt = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print_diagonal(mt, 3)

    mt = [
        [1,  2,  3,  10],
        [4,  5,  6,  11],
        [7,  8,  9,  12],
        [13, 14, 15, 16]
    ]

    print_diagonal(mt, 4)