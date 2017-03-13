"""
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


def get_odd_level_in_order_array(root, array, level):
    if root.left:
        get_odd_level_in_order_array(root.left, array, level + 1)

    if level % 2 != 0:
        array.append(root.data)

    if root.right:
        get_odd_level_in_order_array(root.right, array, level + 1)

    return array


def rev_using_in_order(root, in_order, level):
    if root:
        rev_using_in_order(root.left, in_order, level + 1)

        if level % 2 != 0:
            # assigning from end of in order array
            root.data = in_order.pop()

        rev_using_in_order(root.right, in_order, level + 1)


def reverse_alternate_levels_using_in_order(root):
    in_order = get_odd_level_in_order_array(root, [], 0)
    rev_using_in_order(root, in_order, 0)


"""
method 3 with one single pre order traversal
"""


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

    reverse_alternate_levels_using_in_order(r)
    print_level_order(r)

    print ''
    print ''

    r = get_test_tree()

    reverse_alternate_nodes_single_traversal(r.left, r.right, 0)
    print_level_order(r)
