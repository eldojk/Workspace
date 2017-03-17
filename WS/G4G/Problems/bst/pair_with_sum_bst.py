"""
http://www.geeksforgeeks.org/find-a-pair-with-given-sum-in-bst/
"""
from G4G.Problems.bst.vertical_sum import Node
from G4G.Problems.stacks.stack import Stack


def is_sum_pair_present(root, target):
    s1 = Stack()
    s2 = Stack()

    done1 = False
    done2 = False

    val1 = None
    val2 = None

    curr1 = root
    curr2 = root

    while True:

        # in order
        while not done1:
            if curr1:
                s1.push(curr1)
                curr1 = curr1.left
            else:
                if s1.is_empty():
                    done1 = True
                else:
                    curr1 = s1.pop()
                    val1 = curr1.data
                    curr1 = curr1.right
                    done1 = True

        # reverse in order
        while not done2:
            if curr2:
                s2.push(curr2)
                curr2 = curr2.right
            else:
                if s2.is_empty():
                    done2 = True
                else:
                    curr2 = s2.pop()
                    val2 = curr2.data
                    curr2 = curr2.left
                    done2 = True

        # val1 != val2 makes sure that two of same values are not added
        if val1 != val2 and val1 + val2 == target:
            print 'pair found: {0} and {1}'.format(val1, val2)
            return True

        elif val1 + val2 < target:
            done1 = False

        elif val1 + val2 > target:
            done2 = False

        if val2 <= val1:
            return False


if __name__ == '__main__':
    r = Node(15)
    r.left = Node(10)
    r.right = Node(20)
    r.left.left = Node(8)
    r.left.right = Node(12)
    r.right.left = Node(16)
    r.right.right = Node(25)

    print is_sum_pair_present(r, 33)
