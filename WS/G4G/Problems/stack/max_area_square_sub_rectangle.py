"""
msft

http://www.geeksforgeeks.org/maximum-size-rectangle-binary-sub-matrix-1s/
"""
from G4G.Problems.stack.largest_area_under_histogram import find_largest_area


def find_largest_rectangle(matrix):
    # re using the histogram question
    result = find_largest_area(matrix[0])

    for i in range(1, len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                matrix[i][j] += matrix[i - 1][j]

        result = max(result, find_largest_area(matrix[i]))

    return result


if __name__ == '__main__':
    m = [
        [0, 1, 1, 0],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 0, 0]
    ]

    print find_largest_rectangle(m)


