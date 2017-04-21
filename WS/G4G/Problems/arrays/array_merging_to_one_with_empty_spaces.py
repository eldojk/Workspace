"""
amzn

2 sorted arrays of size m and n (m > n) are given. There are n empty spaces at the
end of the array1. Make the array1 consisting/merging the elements from both
the arrays and store it in array1
"""


def merge_with_empty_spaces(array1, array2):
    i = len(array1) - len(array2) - 1
    j = len(array2) - 1

    k = len(array1) - 1

    while k >= 0 and i >= 0 and j >= 0:
        if array1[i] > array2[j]:
            array1[k] = array1[i]
            i -= 1
        else:
            array1[k] = array2[j]
            j -= 1

        k -= 1

    while i >= 0:
        array1[k] = array1[i]
        i -= 1
        k -= 1

    while j >= 0:
        array1[k] = array2[j]
        j -= 1
        k -= 1

    return array1


if __name__ == '__main__':
    print merge_with_empty_spaces(
        [3, 8, 9, None, None, None],
        [4, 7, 11]
    )