"""
amzn

http://www.geeksforgeeks.org/find-the-row-with-maximum-number-1s/\

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


if  __name__ == '__main__':
    m = [
        [0, 0, 0, 1],
        [0, 1, 1, 1],
        [1, 1, 1, 1],
        [0, 0, 0, 0]
    ]
    print row_with_max_ones(m)
