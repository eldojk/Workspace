"""
amzn, msft

http://www.geeksforgeeks.org/rearrange-positive-and-negative-numbers/

using merge sort without extra space
we are using this approach, because quick sort changes the relative order
of elements

more down
"""


def reverse(array, l, h):
    while l < h:
        array[l], array[h] = array[h], array[l]
        l += 1
        h -= 1


def merge(array, p, q, r):
    i = p
    j = q + 1

    while i <= q and array[i] < 0:
        i += 1
    # arr[i..q] is positive

    while j <= r and array[j] < 0:
        j += 1
    # arr[j..r] is positive

    # reverse positive part of left sub-array (arr[i..q])
    reverse(array, i, q)

    # reverse negative part of right sub-array (arr[q+1..j-1])
    reverse(array, q + 1, j - 1)

    # reverse arr[i..j-1]
    reverse(array, i, j - 1)


def segregate_positive_and_negative(array, l, r):
    if l < r:
        mid = (l + r) // 2

        segregate_positive_and_negative(array, l, mid)
        segregate_positive_and_negative(array, mid + 1, r)

        merge(array, l, mid, r)


if __name__ == '__main__':
    arr = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
    segregate_positive_and_negative(arr, 0, 8)
    print arr


"""
Just re arrange alternately positive and negative (works only when
equal nums of positive and negatives present)

find first positive element with even index and first negative with odd
index and swap them and continue that
"""


def re_arrange_positive_and_negative(array):
    n = len(array)

    if n <= 1:
        return array

    i = 0
    j = 1

    while i < n and j < n:

        while i < n:
            if array[i] > 0:
                break

            i += 2

        while j < n:
            if array[j] < 0:
                break

            j += 2

        if i < n and j < n:
            array[i], array[j] = array[j], array[i]

    return array


if __name__ == '__main__':
    print ''
    print 're arrange +ve -ve in array containing equal nums of +ves and -ves'
    print re_arrange_positive_and_negative([12, 11, -13, -5, 6, -7, -5, 3, -6, 8])
