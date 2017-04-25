"""
amzn

http://www.geeksforgeeks.org/print-elements-sorted-order-row-column-wise-sorted-matrix/
"""


def get_matrix_to_single_array(matrix):
    array = []
    for i in range(len(matrix)):
        arr = matrix[i]
        array.extend(arr)

    return array


def copy(array, aux):
    for i in range(len(array)):
        array[i] = aux[i]


def merge(array, aux, p, q, r, n):
    # optimisation that makes this run in n2lgn instead of n2lgn2
    if (q - p) < n:
        # bcoz this is already sorted
        return

    i = p
    j = q + 1
    k = i

    while i <= q and j <= r:
        if array[i] <= array[j]:
            aux[k] = array[i]
            i += 1
            k += 1
        else:
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


def merge_k_sorted_arrays(array, aux, p, r, n):
    if p < r:
        mid = (p + r) // 2
        merge_k_sorted_arrays(array, aux, p, mid, n)
        merge_k_sorted_arrays(array, aux, mid + 1, r, n)
        merge(array, aux, p, mid, r, n)


def sort_matrix(array):
    array_representation = get_matrix_to_single_array(array)
    print array_representation
    aux = [el for el in array_representation]

    merge_k_sorted_arrays(array_representation, aux, 0, len(array_representation) - 1, len(array) - 1)
    print array_representation


if __name__ == '__main__':
    m = [[10, 20, 30, 40],
         [15, 25, 35, 45],
         [27, 29, 37, 48],
         [32, 33, 39, 50]]
    sort_matrix(m)