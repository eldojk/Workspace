"""
http://www.geeksforgeeks.org/given-linked-list-representation-of-complete-tree-convert-it-to-linked-representation/
"""
from Queue import Queue

from G4G.Problems.bst.vertical_sum import Node


def get_node(array, index):
    if index >= len(array):
        return None

    return Node(array[index])


def create_binary_tree(array):
    root = get_node(array, 0)
    q = Queue()
    q.put(root)
    index = 0
    index += 1

    while not q.empty():
        node = q.get()

        lft = get_node(array, index)
        if lft:
            node.left = lft
            q.put(lft)
            index += 1

        rt = get_node(array, index)
        if rt:
            node.right = rt
            q.put(rt)
            index += 1

    return root

# r = create_binary_tree([1, 2, 3, 4, 5, 6, 7])
# print r
# print r.left
# print r.right
# print r.left.left
# print r.left.right
# print r.right.left
# print r.right.right