from G4G.Problems.bst.vertical_sum import Node
from G4G.Problems.trees.tree_problems2 import get_std_tree
from G4G.Problems.bst.merge_two_balanced_bst import get_inorder_array


def rm(root, k):
    if root is None:
        return None

    if root.data <= k:
        root.right = rm(root.right, k)
        return root

    else:
        return rm(root.left, k)


if __name__ == '__main__':
    r = Node(5)
    r.left = Node(3)
    r.right = Node(7)
    r.left.left = Node(1)
    r.left.right = Node(4)
    r.right.left = Node(6)
    r.right.right = Node(8)

    r = rm(r, 5)
    print get_inorder_array(r, [])