"""
amzn

http://www.geeksforgeeks.org/ceiling-in-a-sorted-array/

ceiling is the next element after floor. so just find floor and do
floor + 1

more down
"""


def ceiling(array, low, high, x):
    if high < low:
        return -1

    if x <= array[low]:
        return low

    if x > array[high]:
        return -1

    mid = (low + high) // 2

    if array[mid] == x:
        return mid

    elif array[mid] < x:
        if mid + 1 <= high and array[mid + 1] >= x:
            return mid + 1

        else:
            return ceiling(array, mid + 1, high, x)

    else:
        if mid - 1 >= low and array[mid - 1] <= x:
            return mid

        else:
            return ceiling(array, low, mid - 1, x)


if __name__ == '__main__':
    print ceiling([1, 2, 8, 10, 10, 12, 19], 0, 6, 14)


def floor(array, low, high, x):
    if low > high:
        return -1

    if x >= array[high]:
        return high

    mid = (low + high) // 2

    if array[mid] == x:
        return mid

    if mid > 0 and array[mid - 1] <= x and x < array[mid]:
        return mid - 1

    if x < array[mid]:
        return floor(array, low, mid - 1, x)

    return floor(array, mid + 1, high, x)


if __name__ == '__main__':
    print floor([1, 2, 8, 10, 12, 19], 0, 5, 14)


"""
another attempt. tried something. looks like it works
"""


def binary_search(array, i, j, x, mid):
    if i > j:
        return -1, mid

    mid = (i + j) // 2

    if array[mid] == x:
        return mid, mid

    elif array[mid] < x:
        return binary_search(array, mid + 1, j, x, mid)

    return binary_search(array, i, mid - 1, x, mid)


def floor_binary_search(array, i, j, x):
    res, mid = binary_search(array, i, j, x, 0)

    if res == -1:
        if array[0] > x:
            return -1

        elif array[j] < x:
            return j

        else:
            if array[mid] < x:
                return mid

            return mid - 1

    return res


if __name__ == '__main__':
    print ''
    print 'floor bs'
    print floor_binary_search([1, 2, 8, 10, 12, 19], 0, 5, 14)
    print floor_binary_search([1, 2, 8, 10, 12, 19], 0, 5, 22)
    print floor_binary_search([1, 2, 8, 10, 12, 19], 0, 5, -1)
    print floor_binary_search([1, 2, 8, 10, 12, 19], 0, 5, 7)
    print floor_binary_search([1, 2, 8, 10, 12, 19], 0, 5, 11)
    print floor_binary_search([1, 2, 8, 10, 12, 19], 0, 5, 12)
