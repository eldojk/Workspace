"""
http://www.geeksforgeeks.org/minimum-number-swaps-required-sort-array/
"""
def comparator(p1, p2):
    if p1[0] < p2[0]:
        return -1
    elif p1[0] > p2[0]:
        return 1

    return 0


def min_swaps(array):
    arr_pos = [(array[i], i) for i in range(len(array))]

    arr_pos.sort(cmp=comparator)

    visited = [False for i in array]

    swaps = 0
    for i in range(len(arr_pos)):
        # already swapped and corrected or already present at correct pos
        if visited[i] or arr_pos[i][1] == i:
            continue

        cycle_size = 0
        j = i
        while not visited[j]:
            visited[j] = True

            j = arr_pos[j][1]
            cycle_size += 1

        swaps += (cycle_size - 1)

    return swaps


if __name__ == '__main__':
    print min_swaps([4, 3, 2, 1, 5])
    print min_swaps([2, 4, 5, 1, 3])
    print min_swaps([4, 3, 2, 1])
    print min_swaps([1, 5, 4, 3, 2])