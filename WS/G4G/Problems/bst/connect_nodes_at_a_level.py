"""
amzn

http://www.geeksforgeeks.org/connect-nodes-at-same-level/
Write a function to connect all the adjacent nodes at the same level in a binary tree.

Input Tree
       A
      / \
     B   C
    / \   \
   D   E   F


Output Tree
       A--->NULL
      / \
     B-->C-->NULL
    / \   \
   D-->E-->F-->NULL
"""
from Queue import Queue


class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.nxt = None

    def __repr__(self):
        return str(self.data)


def bfs_with_levels(root):
    q = Queue()
    q2 = Queue()
    q.put((root, 0))
    q2.put((root, 0))

    while not q.empty():
        node_info = q.get()
        node = node_info[0]
        level = node_info[1]

        if node.left:
            q.put((node.left, level + 1))
            q2.put((node.left, level + 1))

        if node.right:
            q.put((node.right, level + 1))
            q2.put((node.right, level + 1))

    return q2


def connect_nodes_at_levels(queue):
    left = queue.get()

    while not queue.empty():
        right = queue.get()

        if left[1] == right[1]:
            print 'connecting {0} and {1}'.format(left[0], right[0])
            left[0].nxt = right[0]

        left = right


def connect_nodes(root):
    queue = bfs_with_levels(root)
    connect_nodes_at_levels(queue)


if __name__=='__main__':
    root = Node('A')
    root.left = Node('B')
    root.right = Node('C')
    root.left.left = Node('D')
    root.left.right = Node('E')
    root.right.right = Node('F')

    connect_nodes(root)
    print root.left.nxt
    print root.left.left.nxt
    print root.left.right.nxt


"""
amzn

using constant extra space

http://www.geeksforgeeks.org/connect-nodes-at-same-level-with-o1-extra-space/
"""


def get_next_right(node):
    tmp = node.nxt

    while tmp is not None:
        if tmp.left:
            return tmp.left

        elif tmp.right:
            return tmp.right

        else:
            tmp = tmp.nxt

    return None


def connect_with_constant_space(root):
    if root is None:
        return

    p = root

    while p is not None:

        q = p

        while q is not None:

            if q.left:
                if q.right:
                    q.left.nxt = q.right

                else:
                    q.left.nxt = get_next_right(q)

            if q.right:
                q.right.nxt = get_next_right(q)

            q = q.nxt

        if p.left:
            p = p.left

        elif p.right:
            p = p.right

        else:
            p = get_next_right(p)


if __name__=='__main__':
    root = Node('A')
    root.left = Node('B')
    root.right = Node('C')
    root.left.left = Node('D')
    root.left.right = Node('E')
    root.right.right = Node('F')

    print ''
    connect_with_constant_space(root)
    print root.left.nxt
    print root.left.left.nxt
    print root.left.right.nxt
