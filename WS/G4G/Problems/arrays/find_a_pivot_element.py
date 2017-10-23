"""
amzn

pivot element in unsorted array.
all element before are less and all after are greater

http://www.geeksforgeeks.org/find-the-element-before-which-all-the-elements-are-smaller-than-it-and-after-which-all-are-greater-than-it/
"""


def find_max_so_far(array):
    res = [a for a in array]

    for i in range(1, len(array)):
        res[i] = max(
            res[i - 1],
            array[i]
        )

    return res


def find_min_till_here(array):
    res = [a for a in array]

    i = len(array) - 2
    while i >= 0:
        res[i] = min(
            res[i + 1],
            array[i]
        )

        i -= 1

    return res


def find_pivot(array):
    if len(array) <= 2:
        return None

    max_so_far = find_max_so_far(array)
    min_till_here = find_min_till_here(array)

    # 1st element can be pivot
    if min_till_here[1] > array[0]:
        return array[0]

    # last can be pivot
    i = len(array) - 1
    if max_so_far[i - 1] < array[i]:
        return array[i]

    for i in range(1, len(array) - 1):
        if max_so_far[i - 1] < array[i] < min_till_here[i + 1]:
            return array[i]

    return None


if __name__ == '__main__':
    print find_pivot([5, 1, 4, 3, 6, 8, 10, 7, 9])
