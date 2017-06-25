"""
more done down

http://www.geeksforgeeks.org/reverse-alternate-levels-binary-tree/
"""
from G4G.Problems.bst.vertical_sum import Node
from G4G.Problems.trees.level_order_traversal import print_level_order


def get_test_tree():
    root = Node('a')

    root.left = Node('b')
    root.right = Node('c')

    root.left.left = Node('d')
    root.left.right = Node('e')
    root.right.left = Node('f')
    root.right.right = Node('g')

    root.left.left.left = Node('h')
    root.left.left.right = Node('i')
    root.left.right.left = Node('j')
    root.left.right.right = Node('k')
    root.right.left.left = Node('l')
    root.right.left.right = Node('m')
    root.right.right.left = Node('n')
    root.right.right.right = Node('o')

    return root

def reverse_alternate_nodes_single_traversal(root1, root2, level):
    if root1 is None or root2 is None:
        return

    if level % 2 == 0:
        tmp = root1.data
        root1.data = root2.data
        root2.data = tmp

    reverse_alternate_nodes_single_traversal(root1.left, root2.right, level + 1)
    reverse_alternate_nodes_single_traversal(root1.right, root2.left, level + 1)


if __name__ == '__main__':
    r = get_test_tree()

    reverse_alternate_nodes_single_traversal(r.left, r.right, 0)
    print_level_order(r)
