# coding=utf-8
"""
amzn


http://www.geeksforgeeks.org/search-in-row-wise-and-column-wise-sorted-matrix/

1) Start with top right element
2) Loop: compare this element e with x
….i) if they are equal then return its position
…ii) e < x then move it to left (if out of bound of matrix then break return false) ..
iii) e > x then move it to down (if out of bound of matrix then break return false)
3) repeat the i), ii) and iii) till you find element or returned false
"""


def search(matrix, element):
    i = 0
    j = len(matrix) - 1

    while i < len(matrix) and j >= 0:
        x = matrix[i][j]

        if element == x:
            return 'found'

        elif element < x:
            j -= 1

        else:
            i += 1

    return 'Not found'


if __name__ == '__main__':
    m = [
        [10, 20, 30, 40],
        [15, 25, 35, 45],
        [27, 29, 37, 48],
        [32, 33, 39, 50]
    ]
    print search(m, 29)