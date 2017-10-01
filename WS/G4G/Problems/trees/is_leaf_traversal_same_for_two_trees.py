"""
http://www.geeksforgeeks.org/check-if-leaf-traversal-of-two-binary-trees-is-same/
"""
from G4G.Problems.bst.vertical_sum import Node
from G4G.Problems.stack.stack import Stack


def is_leaf(node):
    return node.left is None and node.right is None


def is_leaf_order_same(root1, root2):
    s1 = Stack()
    s2 = Stack()

    done1 = False
    done2 = False

    val1 = None
    val2 = None

    curr1 = root1
    curr2 = root2

    while True:

        while not done1:
            if curr1:
                s1.push(curr1)
                curr1 = curr1.left
            else:
                if s1.is_empty():
                    done1 = True
                    val1 = None
                else:
                    curr1 = s1.pop()
                    val1 = curr1.data
                    if is_leaf(curr1):
                        done1 = True
                    curr1 = curr1.right

        while not done2:
            if curr2:
                s2.push(curr2)
                curr2 = curr2.left
            else:
                if s2.is_empty():
                    done2 = True
                    val2 = None
                else:
                    curr2 = s2.pop()
                    val2 = curr2.data
                    if is_leaf(curr2):
                        done2 = True
                    curr2 = curr2.right

        if done1 and done2:
            if val1 != val2:
                return False
            else:
                done1 = False
                done2 = False

        if val1 is None and val2 is None:
            return True

        if val1 is None or val2 is None:
            return False


if __name__ == '__main__':
    r1 = Node(1)
    r1.left = Node(2)
    r1.right = Node(3)
    r1.left.left = Node(4)
    r1.right.left = Node(6)
    r1.right.right = Node(7)

    r2 = Node(0)
    r2.left = Node(5)
    r2.right = Node(8)
    r2.left.right = Node(4)
    r2.right.left = Node(6)
    r2.right.right = Node(7)

    print is_leaf_order_same(r1, r2)

    r1 = Node(0)
    r1.left = Node(1)
    r1.right = Node(2)
    r1.left.left = Node(8)
    r1.left.right = Node(9)

    r2 = Node(1)
    r2.left = Node(4)
    r2.right = Node(3)
    r2.left.right = Node(8)
    r2.right.left = Node(2)
    r2.right.right = Node(9)

    print is_leaf_order_same(r1, r2)