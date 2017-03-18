"""
http://www.geeksforgeeks.org/construct-a-binary-search-tree-from-given-postorder/

For example, if the given traversal is {1, 7, 5, 50, 40, 10}, then following tree should be constructed

     10
   /   \
  5     40
 /  \      \
1    7      50
"""
from sys import maxint

from G4G.Problems.bst.merge_two_balanced_bst import get_inorder_array
from G4G.Problems.bst.vertical_sum import Node


POST_INDEX = 0


def create_tree(post_order, _min, _max):
    global POST_INDEX
    if POST_INDEX < 0:
        return None

    root = None

    key = post_order[POST_INDEX]
    if _min < key < _max:
        root = Node(key)
        POST_INDEX -= 1

        root.right = create_tree(post_order, key, _max)
        root.left = create_tree(post_order, _min, key)

    return root


def tree_from_post_order(post_order):
    global POST_INDEX
    POST_INDEX = len(post_order) - 1
    _max = maxint
    _min = -maxint
    return create_tree(post_order, _min, _max)


if __name__ == "__main__":
    r = tree_from_post_order([1, 7, 5, 50, 40, 10])
    print get_inorder_array(r, [])
