"""
find upper and lower elements for an element in a sorted array
"""


def bounds(array, start, end, el):
    u = array[0]
    l = array[0]

    while start < end:
        mid = (start + end) // 2

        if array[mid] == el:
            return mid - 1, mid + 1

        elif array[mid] < el:
            start = mid + 1

        else:
            end = mid - 1

        print start, end, mid

    return (start, end) if start < end else (end, start)


if __name__ == '__main__':
    print bounds([1, 3, 5, 7, 9], 0, 4, 6)
