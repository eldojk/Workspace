"""
Given a binary tree, write a function that returns true if the tree satisfies below property.

For every node, data value must be equal to sum of data values in left and right children. Consider data value as 0 for
NULL children.

http://www.geeksforgeeks.org/check-for-children-sum-property-in-a-binary-tree/
"""


def is_leaf(node):
    return node.left is None and node.right is None


def is_child_sum_met(root):
    if root:
        if is_leaf(root):
            return True

        l = root.left.data if root.left else 0
        r = root.right.data if root.right else 0

        if l + r == root.data:
            return is_child_sum_met(root.left) and is_child_sum_met(root.right)

        return False

    return True

# root = Node(10)
# root.left = Node(8)
# root.right = Node(2)
# root.left.left = Node(3)
# root.left.right = Node(5)
# root.right.left = Node(2)
#
# print is_child_sum_met(root)
