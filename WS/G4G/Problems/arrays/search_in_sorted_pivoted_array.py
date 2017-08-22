"""
amzn, smsg

http://www.geeksforgeeks.org/search-an-element-in-a-sorted-and-pivoted-array/

"""
from G4G.Problems.arrays.array_problems import pivoted_element


def binary_search(array, l, h, key):
    if h < l:
        return -1

    mid = (l + h) // 2

    if array[mid] == key:
        return mid

    elif array[mid] < key:
        return binary_search(array, mid + 1, h, key)

    else:
        return binary_search(array, l, mid - 1, key)


def search_in_sorted_rotated_array(array, low, high, key):
    piv = pivoted_element(array, low, high)

    if piv == -1:
        # sorted array
        return binary_search(array, low, high, key)

    elif piv == 0:
        return 0 if array[0] == key else binary_search(array, 1, high, key)

    if array[0] <= key <= array[piv]:
        return binary_search(array, 0, piv, key)

    return binary_search(array, piv + 1, high, key)


if __name__ == '__main__':
    print search_in_sorted_rotated_array([4, 5, 6, 7, 8, 9, 1, 2, 3], 0, 8, 6)
