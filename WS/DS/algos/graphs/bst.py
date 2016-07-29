"""
BST
l
"""
from operator import lt, eq, gt


class Node(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

        # number of nodes in the tree rooted at this node
        self.size = 1

        # number of nodes less than this node
        self.rank = 0

    def __lt__(self, other):
        """
        Key is assumed to be integers/float. To use with other data types as keys,
        extend this class and over-ride __lt__ implementation with the custom code

        :param other:
        :return:
        """
        return self.key < other.key

    def __gt__(self, other):
        """
        Key is assumed to be integers/float. To use with other data types as keys,
        extend this class and over-ride __gt__ implementation with the custom code

        :param other:
        :return:
        """
        return self.key > other.key

    def __eq__(self, other):
        """
        Key is assumed to be integers/float. To use with other data types as keys,
        extend this class and over-ride __eq__ implementation with the custom code

        :param other:
        :return:
        """
        return self.key == other.key

    def has_right_subtree(self):
        return self.right is not None

    def has_left_subtree(self):
        return self.left is not None

    def is_leaf_node(self):
        return not (self.has_left_subtree() or self.has_right_subtree())

    def has_right_and_left_children(self):
        return self.has_left_subtree() and self.has_right_subtree()

    def has_only_one_child_tree(self):
        if self.left is None:
            return self.right is not None

        return self.right is None

    def rank_plus(self, num):
        """
        Increment rank of all nodes rooted at this node by num

        :param num:
        :return:
        """

        self.rank += num

        if self.left is not None:
            self.left.rank_plus(num)

        if self.right is not None:
            self.right.rank_plus(num)

    def increment_rank_on_right_subtree(self, num):
        """
        Increment the ranks of this node and its right subtree by num

        :param num:
        :return:
        """
        self.rank += num

        if self.right is not None:
            self.right.rank_plus(num)

    def min_value(self):
        """
        Min node in the tree rooted here

        :return:
        """
        if not self.left:
            return self

        return self.left.min_value()

    def insert(self, node):
        """
        Insert Node to the tree rooted here

        :param node:
        :return:
        """
        if lt(node, self):
            if self.left is None:
                self.left = node
            else:
                self.left.insert(node)

            # if we are inserting on the left subtree, then the node and its right subtree nodes,
            # should increment their ranks by one as they are all larger.
            self.increment_rank_on_right_subtree(1)

        else:
            if self.right is None:
                self.right = node
            else:
                self.right.insert(node)

        self.size += 1

    def search(self, node):
        """
        Search if node with same key exist

        :param node:
        :return:
        """
        if eq(node, self):
            return self

        elif lt(node, self):
            return self.left.search(node) if self.left is not None else None

        return self.right.search(node) if self.right is not None else None


class BST(object):
    def __init__(self):
        self.root = None

    def add(self, key):
        if self.root is None:
            self.root = Node(key)

        else:
            self.root.insert(Node(key))

    def delete(self, root, node):
        if root is None:
            return None

        root.size -= 1
        if lt(node, root):
            # Delete from left subtree
            root.left = self.delete(root.left, node)
            root.increment_rank_on_right_subtree(-1)

        elif gt(node, root):
            # Delete from right subtreee
            root.right = self.delete(root.right, node)

        else:
            # Delete the node currently at 'root'
            if root.left is None:
                root = root.right

            elif root.right is None:
                root = root.left

            else:
                successor = root.right.min_value()
                root.key = successor.key
                root.right = self.delete(root.right, successor)

        return root

    def remove(self, key):
        node = Node(key)
        self.root = self.delete(self.root, node)

    def search(self, key):
        node = Node(key)
        return self.root.search(node)
