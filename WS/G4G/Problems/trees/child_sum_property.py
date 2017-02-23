"""
Given a binary tree, write a function that returns true if the tree satisfies below property.

For every node, data value must be equal to sum of data values in left and right children. Consider data value as 0 for
NULL children.

http://www.geeksforgeeks.org/check-for-children-sum-property-in-a-binary-tree/
"""
from G4G.Problems.bst.vertical_sum import Node
from G4G.Problems.trees.level_order_traversal import print_level_order


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


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(8)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(5)
    root.right.left = Node(2)

    print is_child_sum_met(root)


"""
http://www.geeksforgeeks.org/convert-an-arbitrary-binary-tree-to-a-tree-that-holds-children-sum-property/
"""


def increment_children(root, diff):
    if root.left:
        root.left.data += diff
        increment_children(root.left, diff)
    elif root.right:
        root.right.data += diff
        increment_children(root.right, diff)


def convert_to_child_sum_tree(root):
    if root is None or is_leaf(root):
        return
    else:
        convert_to_child_sum_tree(root.left)
        convert_to_child_sum_tree(root.right)

        children_sum = 0
        if root.left:
            children_sum += root.left.data

        if root.right:
            children_sum += root.right.data

        if children_sum > root.data:
            root.data = children_sum

        if children_sum < root.data:
            increment_children(root, root.data - children_sum)


if __name__ == '__main__':
    root = Node(50)
    root.left = Node(7)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(5)
    root.right.left = Node(1)
    root.right.right = Node(30)

    convert_to_child_sum_tree(root)
    print_level_order(root)
