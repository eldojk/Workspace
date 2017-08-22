"""
amzn

http://www.geeksforgeeks.org/find-a-sorted-subsequence-of-size-3-in-linear-time/

Input:  arr[] = {12, 11, 10, 5, 6, 2, 30}
Output: 5, 6, 30

Input:  arr[] = {1, 2, 3, 4}
Output: 1, 2, 3 OR 1, 2, 4 OR 2, 3, 4

Input:  arr[] = {4, 3, 2, 1}
Output: No such triplet

1) Create an auxiliary array smaller[0..n-1]. smaller[i] should store the index of a number
which is smaller than arr[i] and is on left side of arr[i]. smaller[i] should contain -1 if
there is no such element.
2) Create another auxiliary array greater[0..n-1]. greater[i] should store the index of a
number which is greater than arr[i] and is on right side of arr[i]. greater[i] should
contain -1 if there is no such element.
3) Finally traverse both smaller[] and greater[] and find the index i for which both
smaller[i] and greater[i] are not -1.
"""


def get_lesser_items_on_left(array):
    res = [-1 for i in array]

    min_idx = 0
    for i in range(1, len(array)):
        if array[i] <= array[min_idx]:
            min_idx = i
        else:
            res[i] = min_idx

    return res


def get_grtr_items_on_right(array):
    res = [-1 for i in array]

    n = len(array)
    max_idx = n - 1

    for i in reversed(range(n - 2)):
        if array[i] >= array[max_idx]:
            max_idx = i
        else:
            res[i] = max_idx

    return res


def find_sorted_triplet(array):
    if len(array) <= 2:
        print 'Not possible'
        return

    l_array = get_lesser_items_on_left(array)
    r_array = get_grtr_items_on_right(array)

    for i in range(len(array)):
        if l_array[i] != -1 and r_array[i] != -1:
            l = l_array[i]
            r = r_array[i]
            print array[l], array[i], array[r]
            return

    print 'Not possible'


if __name__ == '__main__':
    find_sorted_triplet([12, 11, 10, 5, 6, 2, 30])
    find_sorted_triplet([1, 2, 3, 4])
    find_sorted_triplet([4, 3, 2, 1])
