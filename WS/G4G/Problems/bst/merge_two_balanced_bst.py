"""
http://www.geeksforgeeks.org/merge-two-balanced-binary-search-trees/
"""
from G4G.Problems.bst.create_bst_from_sorted_array import create_bst


class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data)


def get_inorder_array(root, array):
    if root.left:
        get_inorder_array(root.left, array)

    array.append(root.data)

    if root.right:
        get_inorder_array(root.right, array)

    return array


def merge_arrays(array1, array2):
    m = len(array1)
    n = len(array2)
    array = [0 for i in range(m + n)]

    i = 0
    j = 0

    while i < m and j < n:
        if array1[i] <= array2[j]:
            array[i + j] = array1[i]
            i += 1
        else:
            array[i + j] = array2[j]
            j += 1

    while i < m:
        array[i + j] = array1[i]
        i += 1

    while j < n:
        array[i + j] = array2[j]
        j += 1

    return array


def merge_bsts(root1, root2):
    array1 = get_inorder_array(root1, [])
    array2 = get_inorder_array(root2, [])
    print array1
    print array2

    array = merge_arrays(array1, array2)

    return create_bst(array, 0, len(array) - 1)


if __name__ == '__main__':
    r1 = create_bst([1, 2, 3, 4, 5], 0, 4)
    r2 = create_bst([2, 4, 6, 8, 9], 0, 4)
    r = merge_bsts(r1, r2)
    arr = get_inorder_array(r, [])
    print arr
