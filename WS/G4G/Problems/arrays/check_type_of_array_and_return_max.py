"""
amzn

http://www.geeksforgeeks.org/type-array-maximum-element/

43215
"""


def is_ascending(array, n):
    prev = array[0]
    for i in range(1, n):
        if prev >= array[i]:
            return False

        prev = array[i]

    return True


def is_descending(array, n):
    prev = array[0]
    for i in range(1, n):
        if prev <= array[i]:
            return False

        prev = array[i]

    return True


def check_type(array):
    n = len(array)

    if n < 2:
        return 'Undecidable'

    first = array[0]
    last = array[n - 1]

    if first < last:
        # ascending or descending rotated

        if is_ascending(array, n):
            return 'Ascending'

        else:
            return 'Descending rotated'

    else:

        # descending or ascending rotated

        if is_descending(array, n):
            return 'Descending'

        else:
            return 'Ascending rotated'


if __name__ == '__main__':
    print check_type([4, 5, 6, 1, 2, 3])
    print check_type([6, 1, 2, 3, 4, 5])
    print check_type([2, 1, 7, 5, 4, 3])
    print check_type([1, 2, 3, 4, 5, 8])
    print check_type([9, 5, 4, 3, 2, 1])