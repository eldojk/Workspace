from DS.algos.graphs.binary_tree import Node
from Queue import Queue

class NNode(object):
    def __init__(self, data):
        self.data = data
        self.children = []

    def __repr__(self):
        return str(self.data)


def convert_to_mirror(root):
    if root is None:
        return

    left = root.left
    root.left = root.right
    root.right = left

    convert_to_mirror(root.left)
    convert_to_mirror(root.right)


if __name__ == '__main__':
    t = Node(1)
    t.left = Node(2)
    t.right = Node(3)
    t.left.left = Node(4)
    t.left.right = Node(5)
    convert_to_mirror(t)
    print t, t.left, t.right, t.right.left, t.right.right


def iterative_mirror(root):
    q = Queue()
    q.put(root)

    while not q.empty():
        node = q.get()

        l = node.left
        r = node.right

        node.left = r
        node.right = l

        if node.left:
            q.put(node.left)

        if node.right:
            q.put(node.right)


if __name__ == '__main__':
    t = Node(1)
    t.left = Node(2)
    t.right = Node(3)
    t.left.left = Node(4)
    t.left.right = Node(5)
    iterative_mirror(t)
    print t, t.left, t.right, t.right.left, t.right.right


def mirror_n_nary_tree(root):
    root.children.reverse()

    for child in root.children:
        mirror_n_nary_tree(child)


if __name__ == '__main__':
    t = NNode(1)
    t.children = [NNode(i) for i in range(2, 6)]
    t.children[3].children = [NNode(6), NNode(7)]

    mirror_n_nary_tree(t)
    print t, t.children, t.children[0].children
