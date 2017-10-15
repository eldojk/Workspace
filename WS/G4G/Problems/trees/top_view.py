"""
amzn

http://www.geeksforgeeks.org/print-nodes-top-view-binary-tree/ (tricky)
"""
from G4G.Problems.bst.vertical_sum import Node
from Queue import Queue


def top_view(root):
    if root is None:
        return

    s = {}
    q = Queue()

    q.put((root, 0))

    while not q.empty():
        item = q.get()
        node = item[0]
        hd = item[1]

        if hd not in s:
            s[hd] = node

        if node.left:
            q.put((node.left, hd - 1))

        if node.right:
            q.put((node.right, hd + 1))

    for k in sorted(s.keys()):
        print s[k],


if __name__ == '__main__':
    r = Node(1)
    r.left = Node(2)
    r.right = Node(3)
    r.left.right = Node(4)
    r.left.right.right = Node(5)
    r.left.right.right.right = Node(6)

    top_view(r)

