"""
amzn

http://www.geeksforgeeks.org/print-matrix-diagonal-pattern/
http://www.geeksforgeeks.org/zigzag-or-diagonal-traversal-of-matrix/

print indices in this order
00
01	10
20	11	02
12	21
22
"""


def print_single_diagonal(matrix, i, j, flag=True):
    if i == j:
        print matrix[i][j],
        return

    mi = s = min(i, j)
    mx = l = max(i, j)

    while s <= mx and l >= mi:

        if flag:
            print matrix[s][l],

        else:
            print matrix[l][s],

        s += 1
        l -= 1


def print_diagonally(matrix):
    n = len(matrix) - 1
    i = 0
    j = 0
    flag = True

    while j <= n:
        print_single_diagonal(matrix, i, j, flag)
        j += 1
        flag = not flag

    j = n
    i = 1

    while i <= n:
        print_single_diagonal(matrix, i, j, flag)
        i += 1
        flag = not flag


if __name__ == '__main__':
    print ''
    mt = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print_diagonally(mt)

    print ''

    mt = [
        [1, 2, 3, 10],
        [4, 5, 6, 11],
        [7, 8, 9, 12],
        [13, 14, 15, 16]
    ]

    print_diagonally(mt)


