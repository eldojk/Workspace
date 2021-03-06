# coding=utf-8
"""
msft

http://www.geeksforgeeks.org/nuts-bolts-problem-lock-key-problem/
https://kartikkukreja.wordpress.com/2013/10/29/matching-nuts-and-bolts-problem/

char nuts[] = {‘@’, ‘#’, ‘$’, ‘%’, ‘^’, ‘&’}
char bolts[] = {‘$’, ‘%’, ‘&’, ‘^’, ‘@’, ‘#’}

nuts can be compared to bolts only and bolts can be compared to nuts
"""


def partition(array, low, high, pivot):
    i = low
    j = low

    while j <= high:
        if array[j] < pivot:
            array[i], array[j] = array[j], array[i]
            j += 1
            i += 1

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
    _bolts = ['#', '$', '@', '%', '&', '^']
    match_pairs(_nuts, _bolts, 0, 5)
    print _nuts
    print _bolts
