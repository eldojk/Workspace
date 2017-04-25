"""
amzn

http://www.geeksforgeeks.org/ceiling-in-a-sorted-array/
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