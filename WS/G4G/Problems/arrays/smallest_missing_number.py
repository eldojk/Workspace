# coding=utf-8
"""
amzn

http://www.geeksforgeeks.org/find-the-first-missing-number/

Given a sorted array of n distinct integers where each integer is in the range from 0 to m-1 and m > n.
Find the smallest number that is missing from the array.

Examples
Input: {0, 1, 2, 6, 9}, n = 5, m = 10
Output: 3

Input: {4, 5, 10, 11}, n = 4, m = 12
Output: 0

Input: {0, 1, 2, 3}, n = 4, m = 5
Output: 4

Input: {0, 1, 2, 3, 4, 5, 6, 7, 10}, n = 9, m = 11
Output: 8

…1) If the first element is not same as its index then return first index
…2) Else get the middle index say mid
…………a) If arr[mid] greater than mid then the required element lies in left half.
…………b) Else the required element lies in right half.
"""


def find_missing(array, l, h):
    if l > h:
        return h + 1

    if l != array[l]:
        return l

    mid = (l + h) // 2

    if array[mid] == mid:
        return find_missing(array, mid + 1, h)

    return find_missing(array, l, h)


if __name__ == '__main__':
    print find_missing([0, 1, 2, 6, 9], 0, 4)
    print find_missing([4, 5, 10, 11], 0, 3)