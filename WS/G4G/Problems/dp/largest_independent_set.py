"""
http://www.geeksforgeeks.org/largest-independent-set-problem/

Let LIS(X) indicates size of largest independent set of a tree with root X.

     LIS(X) = MAX { (1 + sum of LIS for all grandchildren of X),
                     (sum of LIS for all children of X) }
The idea is simple, there are two possibilities for every node X, either X is a member of the set or not a member.
If X is a member, then the value of LIS(X) is 1 plus LIS of all grandchildren. If X is not a member, then the value is
sum of LIS of all children.
"""
from sys import maxint


class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.lis = -maxint


def lis(root):
    if root is None:
        return 0

    # if already found, don't compute again
    if root.lis > 0:
        return root.lis

    lis_excluding_root = lis(root.left) + lis(root.right)

    lis_including_root = 1
    if root.left:
        lis_including_root += lis(root.left.left) + lis(root.left.right)
    if root.right:
        lis_including_root += lis(root.right.left) + lis(root.right.right)

    # memoizing
    root.lis = max(lis_including_root, lis_excluding_root)

    return root.lis


if __name__ == '__main__':
    r = Node(10)
    r.left = Node(20)
    r.right = Node(30)
    r.left.left = Node(40)
    r.left.right = Node(50)
    r.right.right = Node(60)
    r.left.right.left = Node(70)
    r.left.right.right =Node(80)

    print lis(r)