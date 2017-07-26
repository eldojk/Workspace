"""
amzn

Consider an array of distinct numbers sorted in increasing order.
The array has been rotated (anti-clockwise) k number of times.
Given such an array, find the value of k.

http://www.geeksforgeeks.org/find-rotation-count-rotated-sorted-array/
"""
from G4G.Problems.arrays.array_problems import pivoted_element


def rotation_count(array):
    n = len(array)
    pivot = pivoted_element(array, 0, n - 1)

    if pivot == n - 1:
        return 0

    return pivot + 1


if __name__ == '__main__':
    print rotation_count([15, 18, 2, 3, 6, 12])