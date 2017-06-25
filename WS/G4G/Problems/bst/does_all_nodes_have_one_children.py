"""
http://www.geeksforgeeks.org/check-if-each-internal-node-of-a-bst-has-exactly-one-child/
pre-order traversal is given

if we go left from root as we see the next element, all subsequent elements must be on the left of root
"""
from sys import maxint

RANGE = [-maxint, maxint]


def is_one_child_bst(array):
    i = 0
    j = 1
    n = len(array)

    if n <= 2:
        return True

    for k in range(2, n):
        # Checking the relation of 1st and 2nd and updating the valid range for third by placing the first as either
        # upper limit or lower limit
        if array[i] > array[j]:
            RANGE[1] = array[i]
        else:
            RANGE[0] = array[i]

        # Checking range validity
        if RANGE[0] < array[k] < RANGE[1]:
            i += 1
            j += 1
        else:
            return False

    return True


if __name__ == '__main__':
    print is_one_child_bst([20, 10, 11, 13, 12])
