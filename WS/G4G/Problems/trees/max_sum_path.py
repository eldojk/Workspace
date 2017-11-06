"""
amzn

this is less confusing the geeks4geeks implementation

http://www.geeksforgeeks.org/find-maximum-path-sum-in-a-binary-tree/

https://leetcode.com/problems/binary-tree-maximum-path-sum/#/solutions
"""
from G4G.Problems.bst.vertical_sum import Node
from sys import maxint


MAX_VAL = -maxint


def max_sum_path(root):
    global MAX_VAL
    if root is None:
        return 0

    l_sum = max(0, max_sum_path(root.left))
    r_sum = max(0, max_sum_path(root.right))

    # update max seen so far, l_sum = 0 means l_sum not considered
    MAX_VAL = max(MAX_VAL, l_sum + r_sum + root.data)

    # for parent use only one path. i.e. biggest path
    return max(l_sum, r_sum) + root.data


if __name__ == '__main__':
    r = Node(10)
    r.left = Node(2)
    r.right = Node(10)
    r.left.left = Node(20)
    r.left.right = Node(1)
    r.right.right = Node(-25)
    r.right.right.left = Node(3)
    r.right.right.right = Node(4)

    max_sum_path(r)
    print MAX_VAL


"""
attempting some stuff
"""


MAX_SUM = -maxint
MSP = []


def print_max_sum_path(root, curr, curr_sum):
    global MAX_SUM, MSP

    if root is None:
        return

    is_appended = True

    if len(curr) == 0:
        curr.append(root.data)
        curr_sum = root.data
    else:
        # applying max contiguous sum logic
        if curr_sum + root.data > root.data:
            curr.append(root.data)
            curr_sum += root.data
        else:
            is_appended = False
            curr = [root.data]
            curr_sum = root.data

    if curr_sum > MAX_SUM:
        MAX_SUM = curr_sum
        MSP = [e for e in curr]

    print_max_sum_path(root.left, curr, curr_sum)
    print_max_sum_path(root.right, curr, curr_sum)

    if is_appended:
        curr.pop()


if __name__ == '__main__':
    r = Node(10)
    r.left = Node(2)
    r.right = Node(10)
    r.left.left = Node(20)
    r.left.right = Node(1)
    r.right.right = Node(-25)
    r.right.right.left = Node(3)
    r.right.right.right = Node(4)
    r.right.right.right.right = Node(49)

    print_max_sum_path(r, [], 0)
    print MSP
