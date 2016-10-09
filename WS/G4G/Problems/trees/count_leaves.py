"""
Program to count leaf nodes in a binary tree

http://www.geeksforgeeks.org/write-a-c-program-to-get-count-of-leaf-nodes-in-a-binary-tree/
"""


def count_leaves(root):
    if root is None:
        return 0

    if root:
        if root.left is None and root.right is None:
            return 1

        return count_leaves(root.left) + count_leaves(root.right)

# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
#
# print count_leaves(root)
