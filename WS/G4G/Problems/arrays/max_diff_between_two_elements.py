"""
msft

http://www.geeksforgeeks.org/maximum-difference-between-two-elements/

Given an array arr[] of integers, find out the difference between any two elements
such that larger element appears after the smaller number in arr[].

Examples: If array is [2, 3, 10, 6, 4, 8, 1] then returned value should be 8
(Diff between 10 and 2). If array is [7, 9, 5, 6, 3, 2] then returned value should be
2 (Diff between 7 and 9)
"""


def find_max_diff(array):
    i = 1
    min_el = array[0]
    max_diff = array[1] - array[0]

    while i < len(array):
        if array[i] - min_el > max_diff:
            max_diff = array[i] - min_el

        if array[i] < min_el:
            min_el = array[i]

        i += 1

    return max_diff


if __name__ == '__main__':
    print find_max_diff([2, 3, 10, 6, 4, 8, 1])
    print find_max_diff([7, 9, 5, 6, 3, 2])
