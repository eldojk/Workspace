"""
http://www.geeksforgeeks.org/find-height-of-a-special-binary-tree-whose-leaf-nodes-are-connected/
"""
from G4G.Problems.bst.vertical_sum import Node


def is_dll_leaf(node):
    if node.left is None:
        return node.right.left == node

    if node.right is None:
        return node.left.right == node

    return node.left.right == node and node.right.left == node


def height(root):
    if root is None:
        return 0

    if is_dll_leaf(root):
        return 1

    return 1 + max(height(root.left), height(root.right))


if __name__ == '__main__':
    r = Node(1)
    r.left = Node(2)
    r.right = Node(3)
    r.left.left = Node(4)
    r.left.right = Node(5)
    r.left.left.left = Node(6)

    r.left.left.left.right = r.left.right
    r.left.right.left = r.left.left.left

    r.left.right.right = r.right
    r.right.left = r.left.right

    print height(r)