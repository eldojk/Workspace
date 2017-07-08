from DS.algos.graphs.bst import BST


def print_nodes_in_range(root, rang):
    if root is None:
        return

    if root.key > rang[0]:
        print_nodes_in_range(root.left, rang)

    if rang[0] <= root.key <= rang[1]:
        print root.key

    if root.key < rang[1]:
        print_nodes_in_range(root.right, rang)


if __name__ == '__main__':
    bst = BST()
    bst.add(20)
    bst.add(8)
    bst.add(22)
    bst.add(4)
    bst.add(12)

    root = bst.root
    print_nodes_in_range(root, (10, 22))
