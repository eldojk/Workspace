"""
amzn

http://www.geeksforgeeks.org/check-if-a-given-binary-tree-is-complete-tree-or-not/

"""
# todo check if recursive version exists !!

from Queue import Queue

from G4G.Problems.bst.connect_nodes_at_a_level import Node


def is_full_node(node):
    return node.left is not None and node.right is not None


def is_leaf(node):
    return node.left is None and node.right is None


def is_complete(root):
    q = Queue()
    q.put(root)

    has_half_node_found = False
    while not q.empty():
        node = q.get()

        if has_half_node_found and not is_leaf(node):
            return False

        if not is_full_node(node):
            has_half_node_found = True
            if node.right:
                return False

        if node.left:
            q.put(node.left)

        if node.right:
            q.put(node.right)

    return True


r = Node(1)
r.left = Node(2)
r.right = Node(3)
r.left.left = Node(4)
r.left.right = Node(5)
r.right.left = Node(6)

print is_complete(r)
