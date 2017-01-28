"""
Insertion sort repeatedly swaps an element with its predecessor until its higher.
"""

def swap(li, index1, index2):
    temp = li[index1]
    li[index1] = li[index2]
    li[index2] = temp


def insertion_sort(unsorted_list):
    n = len(unsorted_list)

    for i in range(n):
        j = i
        while j > 0:
            if unsorted_list[j] < unsorted_list[j-1]:
                swap(unsorted_list, j, j - 1)
            else:
                break
            j -= 1

    return unsorted_list

