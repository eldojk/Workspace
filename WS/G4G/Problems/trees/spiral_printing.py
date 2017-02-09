"""
Write a function to print spiral order traversal of a tree

http://www.geeksforgeeks.org/level-order-traversal-in-spiral-form/
"""
from DS.algos.graphs.binary_tree import Node
from G4G.Problems.stacks.stack import Stack


def spiral_print(root):
    s1 = Stack()
    s2 = Stack()
    s1.push(root)

    while not s1.is_empty() or not s2.is_empty():
        while not s1.is_empty():
            node = s1.pop()
            print node,

            if node.left:
                s2.push(node.left)
            if node.right:
                s2.push(node.right)

        while not s2.is_empty():
            node = s2.pop()
            print node,

            if node.right:
                s1.push(node.right)
            if node.left:
                s1.push(node.left)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

spiral_print(root)
