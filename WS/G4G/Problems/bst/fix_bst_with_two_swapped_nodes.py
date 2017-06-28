"""
amzn, msft

http://www.geeksforgeeks.org/fix-two-swapped-nodes-of-bst/
http://www.geeksforgeeks.org/sort-an-almost-sorted-array-where-only-two-elements-are-swapped/

CHECK the link. see the two cases
"""
from G4G.Problems.bst.merge_two_balanced_bst import Node


def get_in_order_traversal(root, arr):
    if root:
        get_in_order_traversal(root.left, arr)

        arr.append(root)

        get_in_order_traversal(root.right, arr)


def find_swapped(array):
    first = None
    mid = None
    last = None

    i = 1

    while i < len(array):
        if array[i - 1].data > array[i].data:
            if first is None:
                first = array[i - 1]
                mid = array[i]

            else:
                last = array[i]

        i += 1

    if last is None:
        return first, mid

    return first, last


def fix_tree(root):
    array = []
    get_in_order_traversal(root, array)
    node1, node2 = find_swapped(array)

    tmp = node1.data
    node1.data = node2.data
    node2.data = tmp

    return root


if __name__ == '__main__':
    r = Node(10)
    r.left = Node(5)
    r.right = Node(8)
    r.left.left = Node(2)
    r.left.right = Node(20)

    r = fix_tree(r)
    print r.left.right, r.right
