"""
http://www.geeksforgeeks.org/given-a-binary-tree-print-out-all-of-its-root-to-leaf-paths-one-per-line/
"""


def is_leaf(node):
    return node.left is None and node.right is None


def print_all_paths(root, arr):
    if root:
        arr.append(root)

        print_all_paths(root.left, arr)
        print_all_paths(root.right, arr)

        if is_leaf(root):
            print " ".join(map(str, arr))

        arr.pop()

# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
# root.right.left = Node(6)
# root.right.right = Node(7)
#
#
# print_all_paths(root, [])
