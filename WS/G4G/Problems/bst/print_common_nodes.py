"""
amzn

http://www.geeksforgeeks.org/print-common-nodes-in-two-binary-search-trees/
"""
from G4G.Problems.bst.vertical_sum import Node
from G4G.Problems.stacks.stack import Stack


def print_common_nodes(root1, root2):
    s1 = Stack()
    s2 = Stack()

    while True:
        # push left nodes of trees to stack
        if root1:
            s1.push(root1)
            root1 = root1.left

        elif root2:
            s2.push(root2)
            root2 = root2.left

        elif not s1.is_empty() and not s2.is_empty():
            root1 = s1.peek()
            root2 = s2.peek()

            if root1.data == root2.data:
                # found match, check next in both trees
                print root1.data,
                s1.pop()
                s2.pop()

                root1 = root1.right
                root2 = root2.right

            elif root1.data < root2.data:
                # move to next node in first tree
                s1.pop()
                root1 = root1.right

                # set this to none or in the next iteration it gets
                # pushed to s2 again
                root2 = None

            else:
                s2.pop()
                root2 = root2.right
                root1 = None

        else:
            break


if __name__ == '__main__':
    r1 = Node(5)
    r1.left = Node(1)
    r1.right = Node(10)
    r1.left.left = Node(0)
    r1.left.right = Node(4)
    r1.right.left = Node(7)
    r1.right.left.right = Node(9)

    r2 = Node(10)
    r2.left = Node(7)
    r2.right = Node(20)
    r2.left.left = Node(4)
    r2.left.right = Node(9)

    print_common_nodes(r1, r2)
