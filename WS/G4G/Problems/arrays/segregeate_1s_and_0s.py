"""
In an array with just 1s and 0s.segregate them to zeroes first, followed by ones in one traversal
"""


def segregate(array):
    i = 0
    j = len(array) - 1

    while i < j:
        if array[i] == 0:
            i += 1

        if array[j] == 1:
            j -= 1

        if array[i] > array[j]:
            array[i] = 0
            array[j] = 1

    return array

# print segregate([0, 1, 0, 0, 1, 1, 0, 0, 1])
