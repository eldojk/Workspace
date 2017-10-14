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


def max_consecutive_sequence(root, parent, curr_len, seq):
    global MAX_LEN

    if root is None:
        return

    if parent is None:
        max_consecutive_sequence(root.left, root, 1, [root.data])
        max_consecutive_sequence(root.right, root, 1, [root.data])

    else:

        if root.data != parent.data + 1:
            max_consecutive_sequence(root.left, root, 1, [root.data])
            max_consecutive_sequence(root.right, root, 1, [root.data])

        else:
            curr_len += 1
            seq.append(root.data)

            if MAX_LEN < curr_len:
                MAX_LEN = curr_len
                save(seq)

            max_consecutive_sequence(root.left, root, curr_len, seq)
            max_consecutive_sequence(root.right, root, curr_len, seq)


if __name__ == '__main__':
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

    max_consecutive_sequence(r, None, 0, [])
    print MAX_SEQUENCE
