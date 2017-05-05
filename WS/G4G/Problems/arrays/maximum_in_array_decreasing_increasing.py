"""
amzn

http://www.geeksforgeeks.org/find-the-maximum-element-in-an-array-which-is-first-increasing-and-then-decreasing/

We can modify the standard Binary Search algorithm for the given type of arrays.
i) If the mid element is greater than both of its adjacent elements, then mid is the maximum.
ii) If mid element is greater than its next element and smaller than the previous element then maximum lies on left side
 of mid. Example array: {3, 50, 10, 9, 7, 6}
iii) If mid element is smaller than its next element and greater than the previous element then maximum lies on right side of mid. Example array: {2, 4, 6, 8, 10, 3, 1}
"""


def find_maximum(array, lo, hi):
    # Base Case: Only one element is present in arr[low..high]
    if lo == hi:
        return array[lo]

    #  If there are two elements and first is greater then the first element is maximum
    if hi == lo + 1 and array[lo] >= array[hi]:
        return array[lo]

    #  If there are two elements and second is greater then the second element is maximum
    if hi == lo + 1 and array[lo] < array[hi]:
        return array[hi]

    mid = (lo + hi) // 2

    if array[mid - 1] < array[mid] > array[mid + 1]:
        return array[mid]

    if array[mid - 1] > array[mid] > array[mid + 1]:
        return find_maximum(array, lo, mid - 1)

    else:
        return find_maximum(array, mid + 1, hi)


if __name__ == '__main__':
    print find_maximum([1, 3, 50, 10, 9, 7, 6], 0, 6)