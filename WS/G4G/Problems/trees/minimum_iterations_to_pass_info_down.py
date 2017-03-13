"""
http://www.geeksforgeeks.org/minimum-iterations-pass-information-nodes-tree/
"""


class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = []
        self.height = 0

    # comparators to sort based on height
    def __lt__(self, other):
        return self.height < other.height

    def __eq__(self, other):
        return self.height == other.height

    def __gt__(self, other):
        return self.height > other.height

    def __repr__(self):
        return self.data


def init_heights(root):
    if root is None:
        return 0

    if is_leaf(root):
        return 1

    root.height = 1 + max([init_heights(child) for child in root.children])
    return root.height


def is_leaf(node):
    return len(node.children) == 0


MAX_FOUND = 0


def min_iters_to_percolate(root, time):
    global MAX_FOUND
    if root:
        offset = 1

        if time > MAX_FOUND:
            MAX_FOUND = time

        root.children.sort(reverse=True)

        for child in root.children:
            min_iters_to_percolate(child, time + offset)
            offset += 1


if __name__ == '__main__':
    r = Node('A')
    r.children = [Node(val) for val in ['B', 'C', 'D', 'E', 'F', 'G']]

    b = r.children[0]
    b.children = [Node(val) for val in ['H', 'I', 'J']]

    e = r.children[3]
    e.children = [Node('K'), Node('L')]

    g = r.children[5]
    g.children = [Node('M')]

    h = b.children[0]
    h.children = [Node('N'), Node('O')]

    k = e.children[0]
    k.children = [Node('P')]

    l = e.children[1]
    l.children = [Node('Q')]

    q = l.children[0]
    q.children = [Node('X')]
    q.children[0].children = [Node('Y')]
    q.children[0].children[0].children = [Node('Z')]

    init_heights(r)
    min_iters_to_percolate(r, 0)
    print MAX_FOUND
