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
    root = Node(8)
    root.left = Node(5)
    root.right = Node(4)
    root.left.left = Node(9)
    root.left.right = Node(7)
    root.right.right = Node(11)
    root.right.right.left = Node(3)
    root.left.right.left = Node(1)
    root.left.right.right = Node(12)

    root_to_leaf_pair_with_sum_k(root, set([]), 8)