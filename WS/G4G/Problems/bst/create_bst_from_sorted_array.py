"""
[1, 2, 3, 4, 5]
"""


class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data)


def create_bst(array, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    val = array[mid]
    root = Node(val)

    root.left = create_bst(array, start, mid - 1)
    root.right = create_bst(array, mid + 1, end)

    return root

# r = create_bst([1, 2, 3, 4, 5], 0, 4)
# print r
# print  r.left
# print  r.right
# print  r.left.left
# print r.left.right
# print r.right.left
# print r.right.right
