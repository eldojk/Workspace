# coding=utf-8
"""
amzn

#tricky
http://www.geeksforgeeks.org/find-the-element-that-appears-once-in-a-sorted-array/

All elements before the required have first occurrence at even index (0, 2, ..) and next occurrence at odd index
(1, 3, …). And all elements after the required element have first occurrence at odd index and next occurrence at
even index.

1) Find the middle index, say ‘mid’.

2) If ‘mid’ is even, then compare arr[mid] and arr[mid + 1]. If both are same, then the required element after ‘mid’
else before mid.

3) If ‘mid’ is odd, then compare arr[mid] and arr[mid – 1]. If both are same, then the required element after ‘mid’
else before mid.
"""


def find_single_occurring_element(array, lo, hi):
    if lo > hi:
        return None

    if lo == hi:
        return array[lo]

    mid = (lo + hi) // 2

    if mid % 2 == 0:
        if array[mid] == array[mid + 1]:
            return find_single_occurring_element(array, mid + 2, hi)

        else:
            return find_single_occurring_element(array, lo, mid)

    else:

        if array[mid] == array[mid - 1]:
            return find_single_occurring_element(array, mid + 1, hi)

        else:
            return find_single_occurring_element(array, lo, mid - 1)


if __name__ == '__main__':
    print find_single_occurring_element([1, 1, 2, 4, 4, 5, 5, 6, 6], 0, 8)