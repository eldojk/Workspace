"""
http://www.geeksforgeeks.org/find-pair-root-leaf-path-sum-equals-roots-data/
"""
from G4G.Problems.bst.vertical_sum import Node


def root_to_leaf_pair_with_sum_k(root, st, k):
    if root:
        if k - root.data in st:
            print k - root.data, root.data

        st.add(root.data)
        root_to_leaf_pair_with_sum_k(root.left, st, k)
        root_to_leaf_pair_with_sum_k(root.right, st, k)
        st.remove(root.data)


if __name__ == '__main__':
    r = Node(8)
    r.left = Node(5)
    r.right = Node(4)
    r.left.left = Node(9)
    r.left.right = Node(7)
    r.right.right = Node(11)
    r.right.right.left = Node(3)
    r.left.right.left = Node(1)
    r.left.right.right = Node(12)

    root_to_leaf_pair_with_sum_k(r, set([]), 8)