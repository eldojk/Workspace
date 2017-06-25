"""
amzn, smsg

http://www.geeksforgeeks.org/search-an-element-in-a-sorted-and-pivoted-array/

) Find middle point mid = (l + h)/2
2) If key is present at middle point, return mid.
3) Else If arr[l..mid] is sorted
    a) If key to be searched lies in range from arr[l]
       to arr[mid], recur for arr[l..mid].
    b) Else recur for arr[mid+1..r]
4) Else (arr[mid+1..r] must be sorted)
    a) If key to be searched lies in range from arr[mid+1]
       to arr[r], recur for arr[mid+1..r].
    b) Else recur for arr[l..mid]
"""

#todo or just find the pivot element and proceed using that info


def search_in_sorted_rotated_array(array, low, high, key):
    if low > high:
        return None

    mid = (low + high) // 2

    if array[mid] == key:
        return mid

    # if array low to mid is sorted
    if array[low] <= array[mid]:
        if array[low] <= key <= array[mid]:
            return search_in_sorted_rotated_array(array, low, mid - 1, key)

        return search_in_sorted_rotated_array(array, mid + 1, high, key)

    else:
        if array[mid] <= key <= array[high]:
            return search_in_sorted_rotated_array(array, mid + 1, high, key)

        return search_in_sorted_rotated_array(array, low, mid - 1, key)


if __name__ == '__main__':
    print search_in_sorted_rotated_array([4, 5, 6, 7, 8, 9, 1, 2, 3], 0, 8, 6)
