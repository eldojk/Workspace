"""
amzn msft

http://www.geeksforgeeks.org/print-a-given-matrix-in-spiral-form/
(this is not zig zag printing)
"""


def spiral_print(matrix):
    m = len(matrix)
    n = len(matrix[0])
    k = 0
    l = 0

    while k < m and l < n:

        # Print the first row from the remaining rows
        i = l
        while i < n:
            print matrix[k][i],
            i += 1

        k += 1

        # Print the last column from the remaining columns
        i = k
        while i < m:
            print matrix[i][n - 1],
            i += 1

        n -= 1

        # Print the last row from the remaining rows
        if k < m:
            i = n - 1
            while i >= l:
                print matrix[m - 1][i],
                i -= 1

            m -= 1

        # Print the first column from the remaining columns
        i = m - 1
        if l < n:
            while i >= k:
                print matrix[i][l],
                i -= 1

            l += 1


if __name__ == '__main__':
    m = [
        [1,  2,  3,  4,  5,  6],
        [7,  8,  9,  10, 11, 12],
        [13, 14, 15, 16, 17, 18]
    ]
    spiral_print(m)





