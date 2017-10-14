"""
http://www.geeksforgeeks.org/find-pair-root-leaf-path-sum-equals-roots-data/
"""
from G4G.Problems.bst.vertical_sum import Node


def find_pair(root, hm, r_data):
    if root:
        if hm.get(r_data - root.data):
            print 'YES', root.data, r_data - root.data
            return

        hm[root.data] = True
        find_pair(root.left, hm, r_data)
        find_pair(root.right, hm, r_data)
        hm[root.data] = False


if __name__ == '__main__':
    r = Node(8)
    r.left = Node(5)
    r.right = Node(4)
    r.left.left = Node(9)
    r.left.right = Node(7)
    r.right.right = Node(11)
    r.left.right.right = Node(12)
    r.left.right.left = Node(1)

    find_pair(r, {}, r.data)
