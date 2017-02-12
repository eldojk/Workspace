"""
http://www.geeksforgeeks.org/construct-tree-from-given-inorder-and-preorder-traversal/

Inorder sequence: D B E A F C
Preorder sequence: A B D E C F
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

# root = convert(['A', 'B', 'D', 'E', 'C', 'F'], ['D', 'B', 'E', 'A', 'F', 'C'], 0, 5)
# print root
# print root.left
# print root.right
# print root.left.left
# print root.left.right
# print root.right.left
