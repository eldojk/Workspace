"""
amzn, msft

http://www.geeksforgeeks.org/check-for-identical-bsts-without-building-the-trees/
"""
# todo check code
from sys import maxint

MAX_INT = maxint
MIN_INT = -maxint


def is_same_bst_check(array1, array2, n, i, j, _min, _max):
    # get first element satisfying the limits in both arrays
    while i < n:
        if _min < array1[i] < _max:
            break
        i += 1

    while j < n:
        if _min < array2[j] < _max:
            break
        j += 1

    # reached end of array, i.e. both i and j are leaves
    if i == n and j == n:
        return True

    # one of i and j reached n or the first element to the right
    # satisfying range is not equal
    if (i == n or j == n) or (array1[i] != array2[j]):
        return False

    # recurse for left and right subtrees adjusting range
    return is_same_bst_check(array1, array2, n, i + 1, j + 1, _min, array1[i]) \
           and is_same_bst_check(array1, array2, n, i + 1, j + 1, array2[j], _max)


def is_same_bst(array1, array2, n):
    return is_same_bst_check(array1, array2, n, 0, 0, MIN_INT, MAX_INT)


if __name__ == '__main__':
    print is_same_bst([2, 4, 1, 3], [2, 4, 3, 1], 4)
    print is_same_bst([8, 3, 6, 1, 4, 7, 10, 14, 13], [8, 10, 14, 3, 6, 4, 1, 7, 13], 9)
