"""
No best/worst case. O(n2) is always taken regardless of how elements are arranged in the array
"""

LIST = [7, 8, 1, 4, 15, 44, 6, 11, 2, 21, 12]


def find_min_index(array, start_index):
    sliced_array = array[start_index:]
    min_element = sliced_array[0]
    min_index = 0

    for i in range(len(sliced_array)):
        if sliced_array[i] < min_element:
            min_element = sliced_array[i]
            min_index = i

    return min_index + start_index


def swap(array, first_index, second_index):
    temp = array[first_index]
    array[first_index] = array[second_index]
    array[second_index] = temp


def selection_sort(list_to_sort):
    for index in range(len(list_to_sort)):
        min_index = find_min_index(list_to_sort, index)
        swap(list_to_sort, index, min_index)


selection_sort(LIST)
print LIST
