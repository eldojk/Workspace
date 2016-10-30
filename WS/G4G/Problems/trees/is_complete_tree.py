"""
http://www.geeksforgeeks.org/check-if-a-given-binary-tree-is-complete-tree-or-not/
"""
from Queue import Queue


def is_full_node(node):
    return node.left is not None and node.right is not None


def is_complete(root):
    q = Queue()
    q.put(root)

    while not q.empty():
        node = q.get()

        if not is_full_node(node):
            if node.right:
                return False

        if node.left:
            q.put(node.left)

        if node.right:
            q.put(node.right)

    return True


# r = Node(1)
# r.left = Node(2)
# r.right = Node(3)
# r.left.left = Node(4)
#
# print is_complete(r)
