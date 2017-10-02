"""
amzn

Only works with square matrices - this is O(1) extra space
http://www.geeksforgeeks.org/rotate-ring-matrix-anticlockwise-k-elements/
"""


def get_rotated_coordinate(i, j, i_min, i_max, j_min, j_max, k):
    while k > 0:
        while j == j_min and i > i_min and k > 0:
            k -= 1
            i -= 1

        while i == i_min and j < j_max and k > 0:
            k -= 1
            j += 1

        while j == j_max and i < i_max and k > 0:
            k -= 1
            i += 1

        while i == i_max and j > j_min and k > 0:
            k -= 1
            j -= 1

    return i, j


def fix_k(m, n, k):
    max_rots = (2 * (m + n)) - 4

    return k % max_rots


def get_element_count(i_min, i_max, j_min, j_max):
    r = i_max - i_min + 1
    c = j_max - j_min + 1

    return (2 * (r + c)) - 4


def rotate_matrix(matrix, m, n, k):
    k = fix_k(m, n, k)

    i = j = i_min = j_min = 0
    i_max = m - 1
    j_max = n - 1

    while i_min < i_max and j_min < j_max:

        num = get_element_count(i_min, i_max, j_min, j_max)
        val = matrix[i][j]

        start_i = i
        start_j = j
        while num > 0:
            a, b = get_rotated_coordinate(i, j, i_min, i_max, j_min, j_max, k)
            temp = matrix[a][b]
            matrix[a][b] = val
            val = temp
            num -= 1
            i = a
            j = b

            if i == start_i and j == start_j:
                i = start_i + 1
                j = start_j
                start_i += 1
                val = matrix[i][j]

        i_min += 1
        i_max -= 1
        j_min += 1
        j_max -= 1
        i = i_min
        j = j_min

    return matrix


if __name__ == '__main__':
    m = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]

    mm = rotate_matrix(m, 4, 4, 3)

    print ''
    for x in mm:
        for a in x:
            print a,
        print ''
