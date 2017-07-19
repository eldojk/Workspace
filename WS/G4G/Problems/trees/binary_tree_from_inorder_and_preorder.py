"""
amzn, msft

http://www.geeksforgeeks.org/construct-tree-from-given-inorder-and-preorder-traversal/

Inorder sequence: D B E A F C
Preorder sequence: A B D E C F

more questions underneath
"""
from G4G.Problems.bst.vertical_sum import Node


def search(root_val, inorder, start, end):
    for i in range(start, end + 1):
        if inorder[i] == root_val:
            return i

    return None


pre_index = 0


def convert(preorder, inorder, start, end):
    global pre_index
    if start > end:
        return None

    root_val = preorder[pre_index]
    pre_index += 1
    root = Node(root_val)
    in_index = search(root_val, inorder, start, end)

    root.left = convert(preorder, inorder, start, in_index - 1)
    root.right = convert(preorder, inorder, in_index + 1, end)

    return root


if __name__ == '__main__':
    root = convert(['A', 'B', 'D', 'E', 'C', 'F'], ['D', 'B', 'E', 'A', 'F', 'C'], 0, 5)
    print root,
    print root.left,
    print root.right,
    print root.left.left,
    print root.left.right,
    print root.right.left


"""
amzn

Given preorder and inorder traversal of a binary tree, print preoder and inorder of the tree
after modifying it such
that each node stores the sum of its left and right subtree. (without building tree)
"""


def create_sum_tree_traversals(preorder, inorder, start, end):
    global pre_index
    if start > end:
        return 0

    root_val = preorder[pre_index]
    idx_root = pre_index

    pre_index += 1
    in_index = search(root_val, inorder, start, end)
    idx_root_in = in_index

    left = create_sum_tree_traversals(preorder, inorder, start, in_index - 1)
    right = create_sum_tree_traversals(preorder, inorder, in_index + 1, end)

    preorder[idx_root] = left + right
    inorder[idx_root_in] = left + right

    return root_val + left + right


if __name__ == '__main__':
    pre_index = 0
    ino = [8, -2, -4, 10, 7, 6, 5]
    pre = [10, -2, 8, -4, 6, 7, 5]

    create_sum_tree_traversals(pre, ino, 0, 6)
    print ino
    print pre
