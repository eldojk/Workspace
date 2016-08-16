"""
Given root of binary search tree and K as input, find K-th largest element in BST.
"""
from operator import lt


class KthLargestElement(object):
    def __init__(self, bst):
        self.bst = bst
        self.prev = self.bst.root
        self.n = 1
        self.k = None
        self.kth_largest_node = None

    def custom_reverse_inorder(self, node):
        if node:
            self.custom_reverse_inorder(node.right)

            if lt(node, self.prev):
                self.n += 1

            self.prev = node

            if self.n == self.k:
                self.kth_largest_node = node

            self.custom_reverse_inorder(node.left)

    def get_kth_largest_node(self, k):
        self.__init__(self.bst)
        self.k = k
        self.custom_reverse_inorder(self.bst.root)

        return self.kth_largest_node
