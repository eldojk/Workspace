"""
http://www.geeksforgeeks.org/given-a-binary-tree-how-do-you-remove-all-the-half-nodes/
"""


def remove_half_nodes(root):
    if root is None:
        return None

    root.left = remove_half_nodes(root.left)
    root.right = remove_half_nodes(root.right)

    if root.left is None or root.right is None:
        if not (root.left is None and root.right is None):
            # half node
            child = root.left if root.left is not None else root.right
            temp = root
            root = None
            del temp
            return child

    return root

# root = Node(2)
# root.left = Node(7)
# root.right = Node(5)
# root.left.right = Node(6)
# root.left.right.left = Node(1)
# root.left.right.right = Node(11)
# root.right.right = Node(9)
# root.right.right.left = Node(4)
#
# r = remove_half_nodes(root)
# print r
# print r.left
# print r.right
# print r.left.left
# print r.left.right
