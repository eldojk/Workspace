"""
http://www.geeksforgeeks.org/convert-binary-tree-threaded-binary-tree/
"""
from G4G.Problems.stacks.queue_using_stacks import Queue2


class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.threaded = False

    def __repr__(self):
        return str(self.data)


def populate_queue(root, q):
    if root:
        populate_queue(root.left, q)
        q.push(root)
        populate_queue(root.right, q)


def create_threaded(root, q):
    if root is None:
        return

    if root.left:
        create_threaded(root.left, q)

    q.pop()

    if root.right:
        create_threaded(root.right, q)

    else:
        root.right = q.peek()
        root.threaded = True


def threaded_tree(root):
    q = Queue2()
    populate_queue(root, q)
    create_threaded(root, q)


def left_most(root):
    if root is None:
        return None


    while root.left is not None:
        root = root.left

    return root


def in_order(root):
    if root is None:
        return

    curr = left_most(root)

    while curr is not None:
        print curr,

        if curr.threaded:
            curr = curr.right

        else:
            curr = left_most(curr.right)


def create_threaded_efficient(root):
    if root is None:
        return None

    if root.left is None and root.right is None:
        return root

    if root.left is not None:
        l = create_threaded_efficient(root.left)
        l.threaded = True
        l.right = root

    if root.right is None:
        return root

    return create_threaded_efficient(root)


if __name__ == '__main__':
    r = Node(1)
    r.left = Node(2)
    r.right = Node(3)
    r.left.left = Node(4)
    r.left.right = Node(5)
    r.right.left = Node(6)
    r.right.right = Node(7)

    threaded_tree(r)
    in_order(r)
