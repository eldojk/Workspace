"""
Level order traversal

http://www.geeksforgeeks.org/level-order-tree-traversal/
"""
from Queue import Queue

from G4G.Problems.bst.vertical_sum import Node


def print_level_order(root):
    q = Queue()
    q.put(root)

    while not q.empty():
        node = q.get()
        print node

        if node.left:
            q.put(node.left)
        if node.right:
            q.put(node.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print_level_order(root)