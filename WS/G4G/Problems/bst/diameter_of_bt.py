"""
http://www.geeksforgeeks.org/diameter-of-a-binary-tree/

diameter is also the longest path between two nodes in a tree
"""


def calculate_diameter(root):
    if root is None:
        return 0, 0

    left_diameter, left_height = calculate_diameter(root.left)
    right_diameter, right_height = calculate_diameter(root.right)

    height = 1 + max(left_height, right_height)
    diameter = max(left_diameter, right_diameter, 1 + left_height + right_height)

    return diameter, height

# root = Node(1)
# root.left = Node(2)
# root.right = Node(5)
# root.left.left = Node(3)
# root.left.right = Node(4)
#
# print calculate_diameter(root)
