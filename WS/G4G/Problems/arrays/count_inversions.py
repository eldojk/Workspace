# coding=utf-8
"""
http://www.geeksforgeeks.org/counting-inversions/

Inversion Count for an array indicates – how far (or close) the array is from being sorted. I
f array is already sorted then inversion count is 0. If array is sorted in reverse order that inversion count is the
maximum.
Formally speaking, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j

Example:
The sequence 2, 4, 1, 3, 5 has three inversions (2, 1), (4, 1), (4, 3).
"""

INV_COUNT = 0


def copy(array, aux):
    for i in range(len(array)):
        array[i] = aux[i]


def _count_invs(array, aux, p, q, r):
    global INV_COUNT
    i = p
    j = q + 1
    k = i

    while i <= q and j <= r:
        if array[i] <= array[j]:
            aux[k] = array[i]
            i += 1
            k += 1
        else:
            INV_COUNT += (q - i + 1)
            aux[k] = array[j]
            j += 1
            k += 1

    while i <= q:
        aux[k] = array[i]
        i += 1
        k += 1

    while j <= r:
        aux[k] = array[j]
        j += 1
        k += 1

    copy(array, aux)


def split(array, aux, i, j):
    if i < j:
        mid = (i + j) // 2
        split(array, aux, i, mid)
        split(array, aux, mid + 1, j)
        _count_invs(array, aux, i, mid, j)


def count_inversions(array):
    global INV_COUNT
    aux = [el for el in array]
    split(array, aux, 0, len(array) - 1)
    return INV_COUNT


if __name__=='__main__':
    print count_inversions([2, 4, 1, 3, 5])