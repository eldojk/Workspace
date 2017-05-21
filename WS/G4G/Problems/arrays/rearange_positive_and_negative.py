"""
amzn

http://www.geeksforgeeks.org/rearrange-positive-and-negative-numbers-publish/
"""


def re_arrange(array):
    i = -1

    for j in range(len(array)):
        if array[j] < 0:
            i += 1
            array[i], array[j] = array[j], array[i]

    pos = i + 1
    neg = 0

    while pos < len(array) and neg < pos and array[neg] < 0:
        array[neg], array[pos] = array[pos], array[neg]
        pos += 1
        neg += 2

    return array


if __name__ == '__main__':
    print re_arrange([-1, 2, -3, 4, 5, 6, -7, 8, 9])