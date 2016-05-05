ARRAY = [i for i in range(100) if i % 2 == 0]


def binary_search(element, array_to_search=None):
    if array_to_search:
        array = array_to_search
    else:
        array = ARRAY

    min_element = 0
    max_element = len(array)

    while min_element <= max_element:
        num = int((min_element + max_element) / 2)

        if array[num] == element:
            return array.index(element)
        elif array[num] < element:
            min_element = num + 1
        else:
            max_element = num - 1

    return None


print binary_search(24)
