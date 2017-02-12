"""
http://www.geeksforgeeks.org/fix-two-swapped-nodes-of-bst/

CHECK the link. see the two cases
"""
from G4G.Problems.bst.merge_two_balanced_bst import Node


class Helper(object):
    def __init__(self):
        self.array = []

    def _get_inorder(self, root):
        if root.left:
            self._get_inorder(root.left)

        node = root
        self.array.append(node)

        if root.right:
            self._get_inorder(root.right)

    def get_inorder(self, root):
        self.array = []
        self._get_inorder(root)
        return self.array

    def find_mismatches(self, array):
        m = []
        for i in range(1, len(array)):
            if array[i].data < array[i - 1].data:
                m.append(array[i - 1]) if len(m) == 0 else m.append(array[i])

        return m


def fix_tree(root):
    h = Helper()
    r = root
    in_order = h.get_inorder(r)
    mismatches = h.find_mismatches(in_order)
    node1 = mismatches[0]
    node2 = mismatches[1] if len(mismatches) > 1 else None

    # todo, fis for adjacent swapping where node2 is None
    tmp = node1.data
    node1.data = node2.data
    node2.data = tmp

    return root


if __name__ == '__main__':
    r = Node(10)
    r.left = Node(5)
    r.right = Node(8)
    r.left.left = Node(2)
    r.left.right = Node(20)

    root = fix_tree(r)
    print root
    print root.left, root.right
    print root.left.left, root.left.right
