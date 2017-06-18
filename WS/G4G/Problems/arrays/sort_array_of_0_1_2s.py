"""
amzn, msft

(dutch national flag problem) - single scan algorithm
http://www.geeksforgeeks.org/sort-an-array-of-0s-1s-and-2s/
"""


def swap(array, i, j):
    tmp = array[i]
    array[i] = array[j]
    array[j] = tmp


def sort_array(array):
    lo = 0
    hi = len(array) - 1
    mid = 0

    while mid <= hi:
        value = array[mid]

        if value == 0:
            swap(array, lo, mid)
            lo += 1
            mid += 1

        elif value == 1:
            mid += 1

        else:
            swap(array, mid, hi)
            hi -= 1

    return array


if __name__ == '__main__':
    print sort_array([0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1])
