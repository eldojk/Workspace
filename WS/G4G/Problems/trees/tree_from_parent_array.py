"""
amzn, msft

http://www.geeksforgeeks.org/construct-a-binary-tree-from-parent-array-representation/

Input: parent[] = {1, 5, 5, 2, 2, -1, 3}
Output: root of below tree
          5
        /  \
       1    2
      /    / \
     0    3   4
         /
        6
"""
from G4G.Problems.bst.merge_two_balanced_bst import get_inorder_array
from G4G.Problems.bst.vertical_sum import Node


def make_child(node, parent):
    if parent.left is None:
        parent.left = node
    else:
        parent.right = node


def get_tree_from_parent_array(array):
    root = None
    nodes = [Node(i) for i in range(len(array))]

    for i in range(len(array)):
        node = nodes[i]
        parent_index = array[i]
        if parent_index != -1:
            parent = nodes[parent_index]
            make_child(node, parent)
        else:
            root = node

    return root


if __name__ == '__main__':
    r = Node(5)
    r.left = Node(1)
    r.right = Node(2)
    r.left.left = Node(0)
    r.right.left = Node(3)
    r.right.right = Node(4)
    r.right.left.left = Node(6)

    print get_inorder_array(r, [])

    root = get_tree_from_parent_array([1, 5, 5, 2, 2, -1, 3])

    print get_inorder_array(root, [])
