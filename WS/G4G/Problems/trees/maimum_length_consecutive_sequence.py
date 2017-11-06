"""
amzn

Return a maximum length sequence containing consecutive numbers from a binary tree. i.e.
            90
           /  \
          1   66
         /      \
        2       67
      /   \    /
     5     4  68
          /    \
        99      100
Consecutive sequence of maximum length: [66, 67, 68] of length 3.
"""


class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data)


MAX_LEN = 1
MAX_SEQUENCE = None


def save(sequence):
    global MAX_SEQUENCE
    MAX_SEQUENCE = [c for c in sequence]


"""
another approach
"""


def max_seq(root, curr):
    global MAX_LEN, MAX_SEQUENCE

    if root is None:
        return

    # dealing with curr array
    if len(curr) == 0:
        # initial case when visiting the tree root
        curr.append(root)
    else:
        if curr[-1].data == root.data - 1:
            curr.append(root)
        else:
            curr = [root]

    if MAX_LEN < len(curr):
        MAX_LEN = len(curr)
        save(curr)

    max_seq(root.left, curr)
    max_seq(root.right, curr)


if __name__ == '__main__':
    MAX_LEN = 1
    MAX_SEQUENCE = None

    r = Node(90)
    r.left = Node(1)
    r.right = Node(66)
    r.left.left = Node(2)
    r.right.right = Node(67)
    r.left.left.left = Node(5)
    r.left.left.right = Node(4)
    r.left.left.right.left = Node(99)
    r.right.right.left = Node(68)
    r.right.right.left.right = Node(100)

    max_seq(r, [])
    print MAX_SEQUENCE
