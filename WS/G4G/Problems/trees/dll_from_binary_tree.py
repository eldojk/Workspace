"""
msft

http://www.geeksforgeeks.org/connect-leaves-doubly-linked-list/
"""
from G4G.Problems.bst.vertical_sum import Node

HEAD = None
TAIL = None


def is_leaf(root):
    return root.left is None and root.right is None


def add_to_dll(node):
    global HEAD, TAIL

    if HEAD is None:
        HEAD = node
        TAIL = HEAD
        return

    TAIL.right = node
    node.left = TAIL
    TAIL = node


def convert_to_leaf_dll(root):
    if root:
        if is_leaf(root):
            add_to_dll(root)
            return  # this return is very important, otherwise it goes to infinite loop

        convert_to_leaf_dll(root.left)
        convert_to_leaf_dll(root.right)


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)
    root.left.left.left = Node(7)
    root.left.left.right = Node(8)
    root.right.right.left = Node(9)
    root.right.right.right = Node(10)

    convert_to_leaf_dll(root)
    h = HEAD

    while h is not None:
        print h,
        h = h.right
