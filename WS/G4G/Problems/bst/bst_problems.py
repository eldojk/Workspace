from G4G.Problems.bst.merge_two_balanced_bst import get_inorder_array, Node

"""
http://www.geeksforgeeks.org/convert-bst-to-a-binary-tree/

Given a Binary Search Tree (BST), convert it to a Binary Tree such that every key of the original BST is changed to key
plus sum of all greater keys in BST.

Input: Root of following BST
              5
            /   \
           2     13

Output: The given BST is converted to following Binary Tree
              18
            /   \
          20     13
"""

sm = 0


def convert(root):
    global sm

    if root.right:
        convert(root.right)

    root.data += sm
    sm = root.data

    if root.left:
        convert(root.left)

    return root


r = Node(5)
r.left = Node(2)
r.right = Node(13)
print get_inorder_array(r, [])
root = convert(r)
print get_inorder_array(root, [])
