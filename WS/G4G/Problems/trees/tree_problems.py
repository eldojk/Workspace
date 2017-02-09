from DS.algos.graphs.binary_tree import Node


def get_std_tree():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    return root


def get_child_sum_tree():
    root = Node(10)
    root.left = Node(8)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(5)
    root.right.left = Node(2)

    return root


def size_of_tree(root):
    if root is None:
        return 0

    return 1 + size_of_tree(root.left) + size_of_tree(root.right)


def are_tres_identical(root1, root2):
    if root1 is None and root2 is None:
        return True

    if root1 is None or root2 is None:
        return False

    if root1.data == root2.data:
        return are_tres_identical(root1.left, root2.left) and are_tres_identical(root1.right, root2.right)

    return False


def compute_depth(root):
    if root is None:
        return 0

    return 1 + max(compute_depth(root.left), compute_depth(root.right))


def delete_tree(root):
    if root is None:
        return

    delete_tree(root.left)
    delete_tree(root.right)
    print root.data, 'deleted'
    del root


def is_child_sum_property_true(root):
    if root is None:
        return True

    if root.left is None and root.right is None:
        return True

    if root.left is None:
        return root.data == root.right.data

    if root.right is None:
        return root.data == root.left.data

    is_satisfied = (root.data == root.left.data + root.right.data)
    is_children_satisfied = is_child_sum_property_true(root.left) and is_child_sum_property_true(root.right)
    return is_satisfied and is_children_satisfied


def satisfy_child_sum_property(root):
    if root is None:
        return

    satisfy_child_sum_property(root.left)
    satisfy_child_sum_property(root.right)

    left = root.left.data if root.left else 0
    right = root.right.data if root.right else 0

    if left == 0 and right == 0:
        return

    root.data = left + right


def count_leaves(root):
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return 1

    return count_leaves(root.left) + count_leaves(root.right)


def convert_to_mirror(root):
    if root is None:
        return

    left = root.left
    root.left = root.right
    root.right = left

    convert_to_mirror(root.left)
    convert_to_mirror(root.right)

t = get_std_tree()
convert_to_mirror(t)
print t, t.left, t.right, t.right.left, t.right.right
