def print_nodes(root, k):
    if root is None:
        return

    if k == 0:
        print root

    print_nodes(root.left, k - 1)
    print_nodes(root.right, k - 1)


def print_at_dist_k(root, node, k):
    if root is None:
        return False, k

    if root == node:
        print_nodes(root, k)
        return True, k

    is_found_left, l_dist = print_at_dist_k(root.left, node, k)
    if is_found_left:
        if l_dist == 1:
            print root
        elif l_dist > 1:
            print_nodes(root.right, k - 2)

    is_found_right, r_dist = print_at_dist_k(root.right, node, k)
    if is_found_right:
        if r_dist == 1:
            print root
        elif r_dist > 1:
            print_nodes(root.left, k - 2)

    return (is_found_left or is_found_right), k - 1


# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
# root.right.left = Node(6)
# root.right.right = Node(7)
# root.left.right.right = Node(8)
# root.left.right.right.left = Node(9)
#
# print_at_dist_k(root, root.left, 3)
