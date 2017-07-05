# coding=utf-8
"""
amzn, msft

more done down
http://www.geeksforgeeks.org/find-the-row-with-maximum-number-1s/

Given a boolean 2D array, where each row is sorted. Find the row with the maximum number of 1s.
"""


def first_occurence_of_one(array, low, high):
    if high >= low:

        mid = (low + high) // 2

        if (mid == 0 or array[mid - 1] == 0) and array[mid] == 1:
            return mid

        elif array[mid] == 0:
            return first_occurence_of_one(array, mid + 1, high)

        else:
            return first_occurence_of_one(array, low, mid - 1)

    return -1


def row_with_max_ones(matrix):
    index = 0
    max_ones = 0
    c = len(matrix[0])

    for i in range(len(matrix)):
        idx = first_occurence_of_one(matrix[i], 0, c - 1)
        num_ones = c - idx

        if num_ones > max_ones and idx >= 0:
            max_ones = num_ones
            index = i

    return index


if __name__ == '__main__':
    m = [
        [0, 0, 0, 1],
        [0, 1, 1, 1],
        [1, 1, 1, 1],
        [0, 0, 0, 0]
    ]
    print row_with_max_ones(m)


"""
o(m + n) algorithm. this is better

http://www.geeksforgeeks.org/find-the-row-with-maximum-number-1s/

Step1: Get the index of first (or leftmost) 1 in the first row.

Step2: Do following for every row after the first row
…IF the element on left of previous leftmost 1 is 0, ignore this row.
…ELSE Move left until a 0 is found. Update the leftmost index to this index and max_row_index to be the current row.
"""


def row_with_max_ones_better(matrix):
    m = len(matrix)
    n = len(matrix[0])

    for i in range(n):
        if matrix[0][i] == 1:
            break

    min_k = 0
    k = 1
    while k < m:
        while matrix[k][i] == 1 and i >= 0:
            i -= 1
            min_k = k

        if i == -1:
            return k

        k += 1

    return min_k


if __name__ == '__main__':
    m = [
        [0, 0, 0, 1],
        [0, 1, 1, 1],
        [1, 1, 1, 1],
        [0, 0, 0, 0]
    ]
    print row_with_max_ones_better(m)