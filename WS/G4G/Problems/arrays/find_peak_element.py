"""
amzn

#tricky
http://www.geeksforgeeks.org/find-a-peak-in-a-given-array/

We can use Divide and Conquer to find a peak in O(Logn) time. The idea is Binary Search based, we compare middle element
with its neighbors. If middle element is not smaller than any of its neighbors, then we return it. If the middle element
is smaller than the its left neighbor, then there is always a peak in left half (Why? take few examples). If the middle
element is smaller than the its right neighbor, then there is always a peak in right half (due to same reason as
left half)
"""


def peak_element(array, lo, hi, n):
    mid = (lo + hi) // 2

    # determine if mid is a peak
    if (mid == 0 or array[mid - 1] <= array[mid]) and (mid == n - 1 or array[mid + 1] <= array[mid]):
        return mid

    elif mid > 0 and array[mid - 1] > array[mid]:
        return peak_element(array, lo, mid - 1, n)

    else:
        return peak_element(array, mid + 1, hi, n)


def find_peak(array):
    n = len(array)

    return peak_element(array, 0, n - 1, n)


if __name__ == '__main__':
    print find_peak([1, 3, 20, 4, 1, 0])
