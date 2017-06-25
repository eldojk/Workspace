"""
Given a binary tree, output a linked list containing nodes at each level
"""


class LevelLL(object):
    def __init__(self, root):
        self.root = root
        self.dict = {}
        self.dfs_with_level_append(self.root, 0)

    def append_at_level(self, node, level):
        if node is None:
            return

        self.dict[level] = [node] if self.dict.get(level) is None else self.dict[level] + [node]

    def dfs_with_level_append(self, root, level):
        if root is None:
            return

        self.append_at_level(root, level)
        self.dfs_with_level_append(root.left, level + 1)
        self.dfs_with_level_append(root.right, level + 1)

    def get_ll(self):
        return self.dict


# if __name__=='__main__':
#     root = Node(0)
#     root.left = Node(1)
#     root.right = Node(2)
#     root.left.left = Node(3)
#     root.left.right = Node(4)
#     root.right.left = Node(5)
#     root.right.right = Node(6)
#
#     ll_maker = LevelLL(root)
#     print ll_maker.get_ll()