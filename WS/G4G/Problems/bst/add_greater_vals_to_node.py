"""
amzn

http://www.geeksforgeeks.org/add-greater-values-every-node-given-bst/
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
from G4G.Problems.bst.merge_two_balanced_bst import get_inorder_array
from G4G.Problems.bst.vertical_sum import Node


CURR_VAL = 0


def add_greater_vals(root):
    global CURR_VAL

    if root is None:
        return

    add_greater_vals(root.right)

    root.data += CURR_VAL
    CURR_VAL = root.data

    add_greater_vals(root.left)


if __name__ == '__main__':
    r = Node(50)
    r.left = Node(30)
    r.right = Node(70)
    r.left.left = Node(20)
    r.left.right = Node(40)
    r.right.left = Node(60)
    r.right.right = Node(80)

    add_greater_vals(r)

    print get_inorder_array(r, [])
