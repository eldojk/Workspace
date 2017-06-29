# coding=utf-8
"""
http://www.geeksforgeeks.org/remove-bst-keys-outside-the-given-range/
https://kartikkukreja.wordpress.com/2013/10/29/matching-nuts-and-bolts-problem/

char nuts[] = {‘@’, ‘#’, ‘$’, ‘%’, ‘^’, ‘&’}
char bolts[] = {‘$’, ‘%’, ‘&’, ‘^’, ‘@’, ‘#’}
"""


def partition(array, low, high, pivot):
    i = low
    j = low

    while j < high:
        if array[j] < pivot:
            array[i], array[j] = array[j], array[i]
            j += 1
            i += 1

        elif array[j] == pivot:
            # moving pivot to end, so if i ever reach pivot index, it won't swap anything
            array[high], array[j] = array[j], array[high]
            j += 1

        else:
            j += 1

    array[i], array[high] = array[high], array[i]
    return i


def match_pairs(nuts, bolts, low, high):
    if low < high:
        mid = (low + high) // 2

        pivot_idx = partition(nuts, low, high, bolts[high])

        partition(bolts, low, high, nuts[pivot_idx])

        match_pairs(nuts, bolts, low, mid - 1)
        match_pairs(nuts, bolts, mid + 1, high)


if __name__ == '__main__':
    _nuts = ['@', '#', '$', '%', '^', '&']
    _bolts = ['@', '#', '$', '%', '^', '&']
    match_pairs(_nuts, _bolts, 0, 5)
    print _nuts
    print _bolts
