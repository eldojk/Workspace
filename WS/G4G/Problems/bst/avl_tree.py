"""
AVL TREE
"""
from G4G.Problems.trees.level_order_traversal import print_level_order


class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 0

    def __repr__(self):
        return str(self.data)


class AVLTree(object):
    def __init__(self):
        self.root = None

    def height(self, node):
        if node:
            return node.height

        return -1

    def left_rotate(self, node):
        """
             A (2)                B (1)
            / \                  / \
        (-1)  B (1)   ->    (0) A   C (0)
             / \               / \
          (-1)  C (0)       (-1)(-1)

        :param node:
        :return:
        """
        A = node
        B = node.right

        A.right = B.left
        B.left = A

        A.height = max(self.height(A.left), self.height(A.right)) + 1
        B.height = max(self.height(B.left), self.height(B.right)) + 1

        return B

    def right_rotate(self, node):
        """
            (2) A                  B (1)
               / \                / \
          (1) B  (-1)   ->   (0) C   A (0)
             / \                    / \
        (0) C   (-1)             (-1)  (-1)

        :param node:
        :return:
        """
        A = node
        B = node.left

        A.left = B.right
        B.right = A

        A.height = max(self.height(A.left), self.height(A.right)) + 1
        B.height = max(self.height(B.left), self.height(B.right)) + 1

        return B

    def _insert(self, key, t):
        if t is None:
            t = Node(key)

        elif key < self.root.data:
            t.left = self._insert(key, t.left)

            if self.height(t.left) - self.height(t.right) >= 2:
                if key < t.left.data:
                    # key was inserted to left of t.left (need right rotate to balance)
                    t = self.right_rotate(t)
                else:
                    # key was inserted to right of t.left (need left + right to balance)
                    t.left = self.left_rotate(t.left)
                    t = self.right_rotate(t)

        elif key > self.root.data:
            t.right = self._insert(key, t.right)

            if self.height(t.right) - self.height(t.left) >= 2:
                if key > t.right.data:
                    # key was inserted to right of t.right (need left rotate to balance)
                    t = self.left_rotate(t)
                else:
                    # key was inserted to left of t.right (need right + left to balance)
                    t.right = self.right_rotate(t.right)
                    t = self.left_rotate(t)

        t.height = 1 + max(self.height(t.left), self.height(t.right))

        return t

    def insert(self, key):
        """
        Insert key to AVL tree

        :param key:
        :return:
        """
        self.root = self._insert(key, self.root)


if __name__ == '__main__':
    tree = AVLTree()
    tree.insert(1)
    tree.insert(2)
    tree.insert(3)
    tree.insert(4)
    tree.insert(5)
    tree.insert(6)
    tree.insert(7)

    print_level_order(tree.root)