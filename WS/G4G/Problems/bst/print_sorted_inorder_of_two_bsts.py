"""
amzn

http://www.geeksforgeeks.org/merge-two-bsts-with-limited-extra-space/
"""
from G4G.Problems.bst.vertical_sum import Node
from G4G.Problems.stacks.stack import Stack


def print_merged(root1, root2):
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
                    curr1 = curr1.right
                    done1 = True

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
                    curr2 = curr2.right
                    done2 = True

        if val1 is not None and val2 is not None:
            if val1 < val2:
                print val1,
                done1 = False

            else:
                print val2,
                done2 = False

        if val1 is None and val2 is None:
            break

        if val1 is None:
            print val2,
            done2 = False

        if val2 is None:
            print val1,
            done1 = False


if __name__ == '__main__':
    r1 = Node(3)
    r1.left = Node(1)
    r1.left.left = Node(0)
    r1.left.right = Node(2)
    r1.right = Node(5)

    r2 = Node(4)
    r2.left = Node(2)
    r2.right = Node(6)
    r2.right.right = Node(7)

    print_merged(r1, r2)