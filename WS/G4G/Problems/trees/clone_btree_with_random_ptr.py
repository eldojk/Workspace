"""
http://www.geeksforgeeks.org/clone-binary-tree-random-pointers/
"""
class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.random = None

    def __repr__(self):
        return str(self.data)


def clone_trees_and_fill_dict(tree, dict):
    if tree is None:
        return None, dict

    root = Node(tree.data)
    dict[tree] = root

    root.left, dict = clone_trees_and_fill_dict(tree.left, dict)
    root.right, dict = clone_trees_and_fill_dict(tree.right, dict)

    return root, dict


def traverse_and_update_random_ptr(tree, clone, dict):
    if tree:
        clone.random = dict[tree.random]

        traverse_and_update_random_ptr(tree.left, clone.left, dict)
        traverse_and_update_random_ptr(tree.right, clone.right, dict)


def clone_tree(tree):
    clone, dict = clone_trees_and_fill_dict(tree, {})
    traverse_and_update_random_ptr(tree, clone, dict)

    return clone


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.random = root.right
    root.left.random = root
    root.right.random = root.left

    clone = clone_tree(root)
    print root, root.left, root.right
    print root.random, root.left.random, root.right.random
