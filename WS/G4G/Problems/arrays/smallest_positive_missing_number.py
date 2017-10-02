"""
amzn

#tricky
http://www.geeksforgeeks.org/find-the-smallest-positive-number-missing-from-an-unsorted-array/

(Assuming array contains positive only. handling negatives is in the link
To handle negatives, just segregate +ve and -ve nums in O(n) and consider only
the positive section in the segregated array)

traverse from 0 to n - 1, let x be array[i].
To indicate that x is present make, array[x] = -array[x].
One second traversal of array from left to right, find the first positive number index
"""


def find_smallest_positive_missing_number(array):
    n = len(array)

    for i in range(n):
        x = array[i]

        if 0 <= x < n:
            array[x] = -array[x]

    missing = None

    for i in range(1, n):
        if array[i] > 0:
            missing = i
            break

    return missing


if __name__ == '__main__':
    print find_smallest_positive_missing_number([2, 3, 7, 6, 8])
    print find_smallest_positive_missing_number([2, 3, 7, 6, 8, 1, 15])
