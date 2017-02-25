"""
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
