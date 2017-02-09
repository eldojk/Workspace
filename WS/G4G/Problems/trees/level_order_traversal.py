"""
Level order traversal

http://www.geeksforgeeks.org/level-order-tree-traversal/

{Updated to indicate level wise printing}
"""
from Queue import Queue

from G4G.Problems.bst.vertical_sum import Node


def print_level_order(root):
    q = Queue()
    q.put((root, 0))
    current_level = 0

    while not q.empty():
        item = q.get()
        node = item[0]
        level = item[1]

        if level != current_level:
            print ''
            current_level = level

        print node,

        if node.left:
            q.put((node.left, current_level + 1))
        if node.right:
            q.put((node.right, current_level + 1))


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print_level_order(root)