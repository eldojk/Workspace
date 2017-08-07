"""
amzn

Using Morris Traversal, we can traverse the tree without using stack and recursion.
Although the tree is modified through the traversal, it is reverted back to its original shape after the completion.
Unlike Stack based traversal, no extra space is required for this traversal.

Constructed binary tree is
               1
             /   \
            2      3
          /  \
        4     5
"""
from DS.algos.graphs.binary_tree import Node


def morris_traversal(root):
    if root is None:
        return

    while root is not None:

        if root.left is None:
            print root,
            root = root.right

        else:
            pre = root.left

            while pre.right is not None and pre.right != root:
                pre = pre.right

            if pre.right is None:
                pre.right = root
                root = root.left

            else:
                pre.right = None
                print root,
                root = root.right


if __name__ == '__main__':
    r = Node(1)
    r.left = Node(2)
    r.right = Node(3)
    r.left.left = Node(4)
    r.left.right = Node(5)
    morris_traversal(r)
