"""
amzn

https://discuss.codechef.com/questions/1489/find-median-in-an-unsorted-array-without-sorting-it
"""


def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            # increment index of smaller element
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1


def selection(array, left, right, k):
    while True:
        pivot = partition(array, left, right)
        ln = pivot - left + 1

        if k == ln:
            return array[pivot]

        elif k < ln:
            right = pivot - 1

        else:
            k -= ln
            left = pivot + 1


if __name__ == '__main__':
    print selection([6, 7, 8, 1, 2, 3, 4, 5, 9, 10], 0, 9, 5)
