"""
http://www.geeksforgeeks.org/binary-tree-to-binary-search-tree-conversion/
get_inorder, sort it, do inorder of original tree and write values
"""

from G4G.Problems.bst.merge_two_balanced_bst import get_inorder_array, Node

IDX = 0


def write_values(root, in_order):
    global IDX
    if root:
        write_values(root.left, in_order)

        root.data = in_order[IDX]
        IDX += 1

        write_values(root.right, in_order)


def convert_to_bst(root):
    global IDX
    in_order = get_inorder_array(root, [])
    in_order.sort()
    IDX = 0
    write_values(root, in_order)
    return root


if __name__ == '__main__':
    r = Node(10)
    r.left = Node(2)
    r.right = Node(7)
    r.left.left = Node(8)
    r.left.right = Node(4)

    rt = convert_to_bst(r)
    print get_inorder_array(rt, [])
