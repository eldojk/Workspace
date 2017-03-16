"""
http://www.geeksforgeeks.org/find-sum-left-leaves-given-binary-tree/
"""
from DS.algos.graphs.binary_tree import Node
from G4G.Problems.bst.merge_two_balanced_bst import get_inorder_array
from G4G.Problems.trees.level_order_traversal import print_level_order


def get_std_tree():
    r = Node(1)
    r.left = Node(2)
    r.right = Node(3)
    r.left.left = Node(4)
    r.left.right = Node(5)
    r.right.left = Node(6)
    r.right.right = Node(7)

    return r


def is_leaf(node):
    return node.left is None and node.right is None


def is_full_node(node):
    return node.left is not None and node.right is not None


LEFT_LEAF_SUM = 0


def sum_left_leaf(root):
    global LEFT_LEAF_SUM
    if root is None:
        return

    sum_left_leaf(root.left)
    sum_left_leaf(root.right)

    if root.left:
        if is_leaf(root.left):
            LEFT_LEAF_SUM += root.left.data


if __name__ == '__main__':
    sum_left_leaf(get_std_tree())
    print LEFT_LEAF_SUM

"""
http://www.geeksforgeeks.org/expression-tree/
"""


def prod(a, b):
    return a * b


def _sum(a, b):
    return a + b


EXPS = {
    '+': _sum,
    '*': prod
}


def eval_expression_tree(root):
    if is_leaf(root):
        return root.data

    left_val = eval_expression_tree(root.left)
    right_val = eval_expression_tree(root.right)
    op = root.data
    funct = EXPS[op]
    return funct(left_val, right_val)


if __name__ == '__main__':
    print ''
    r = Node('+')
    r.left = Node(3)
    r.right = Node('*')
    r.right.left = Node('+')
    r.right.right = Node(2)
    r.right.left.left = Node(5)
    r.right.left.right = Node(9)

    print eval_expression_tree(r)


"""
http://www.geeksforgeeks.org/given-a-binary-tree-how-do-you-remove-all-the-half-nodes/
"""


def remove_half_nodes(root):
    if root is None:
        return None

    root.left = remove_half_nodes(root.left)
    root.right = remove_half_nodes(root.right)

    if not is_leaf(root) and not is_full_node(root):
        if root.left:
            return root.left

        return root.right

    return root


if __name__ == '__main__':
    print ''

    root = Node(2)
    root.left = Node(7)
    root.right = Node(5)
    root.left.right = Node(6)
    root.left.right.left = Node(1)
    root.left.right.right = Node(11)
    root.right.right = Node(9)
    root.right.right.left = Node(4)

    print get_inorder_array(root, [])
    remove_half_nodes(root)
    print get_inorder_array(root, [])


"""
http://www.geeksforgeeks.org/find-count-of-singly-subtrees/
"""


def num_single_valued(root):
    if root is None:
        return 0

    if is_leaf(root):
        return 1

    left_num = num_single_valued(root.left)
    right_num = num_single_valued(root.right)

    if left_num > 0 and right_num > 0:
        return (left_num + right_num + 1) if root.data == root.left.data == root.right.data else (left_num + right_num)

    if left_num > 0:
        return left_num if root.data != root.left.data else (left_num + 1)

    if right_num > 0:
        return right_num if root.data != root.right.data else (right_num + 1)


if __name__ == '__main__':
    print ''
    r = Node(5)
    r.left = Node(1)
    r.right = Node(5)
    r.left.left = Node(5)
    r.left.right = Node(5)
    r.right.right = Node(5)

    print num_single_valued(r)


"""
http://www.geeksforgeeks.org/remove-nodes-root-leaf-paths-length-k/

(i did it wrong, should be length, not sum)
"""


def remove_nodes_in_sum_path_lt_k(root, curr_sum, k):
    if root is None:
        return True

    if is_leaf(root):
        curr_sum += root.data
        return curr_sum > k

    left_sum_met = remove_nodes_in_sum_path_lt_k(root.left, curr_sum + root.data, k)
    right_sum_met = remove_nodes_in_sum_path_lt_k(root.right, curr_sum + root.data, k)

    if not left_sum_met:
        root.left = None

    if not right_sum_met:
        root.right = None

    return left_sum_met or right_sum_met


if __name__ == '__main__':
    print ''
    r = Node(1)
    r.left = Node(2)
    r.right = Node(3)
    r.left.left = Node(4)
    r.left.right = Node(5)
    r.right.right = Node(6)
    r.left.left.left = Node(7)
    r.right.right.left = Node(8)

    print get_inorder_array(r, [])
    remove_nodes_in_sum_path_lt_k(r, 0, 9)
    print get_inorder_array(r, [])


"""
http://www.geeksforgeeks.org/find-minimum-depth-of-a-binary-tree/
"""


def min_depth(root):
    if root is None:
        return 0

    return 1 + min(min_depth(root.left), min_depth(root.right))


if __name__ == '__main__':
    print ''
    r = Node(1)
    r.left = Node(2)
    r.right = Node(3)
    r.left.left = Node(4)
    r.left.right = Node(5)
    print min_depth(r)


"""
http://www.geeksforgeeks.org/symmetric-tree-tree-which-is-mirror-image-of-itself/
"""


def is_symmetric(root1, root2):
    if root1 is None and root2 is None:
        return True

    if root1 is None or root2 is None:
        return False

    if root1.data != root2.data:
        return False

    return is_symmetric(root1.left, root2.right) and is_symmetric(root1.right, root2.left)


if __name__ == '__main__':
    print ''
    r = Node(1)
    r.left = Node(2)
    r.right = Node(2)
    r.left.left = Node(3)
    r.left.right = Node(4)
    r.right.left = Node(4)
    r.right.right = Node(3)

    print is_symmetric(r.left, r.right)



"""
http://www.geeksforgeeks.org/construct-ancestor-matrix-from-a-given-binary-tree/
"""


def plot_ancestor_matrix(root, matrix, ancestors):
    if root:
        for ancestor in ancestors:
            matrix[ancestor.data][root.data] = 1

        ancestors.append(root)
        plot_ancestor_matrix(root.left, matrix, ancestors)
        plot_ancestor_matrix(root.right, matrix, ancestors)
        ancestors.pop()


def ancestor_matrix(root, n):
    matrix = [[0 for i in range(n)] for j in range(n)]
    ancestors = []
    plot_ancestor_matrix(root, matrix, ancestors)
    for row in matrix:
        print row


if __name__ == '__main__':
    r = Node(0)
    r.left = Node(1)
    r.right = Node(2)

    print ''
    ancestor_matrix(r, 3)

    r = Node(5)
    r.left = Node(1)
    r.right = Node(2)
    r.left.left = Node(0)
    r.left.right = Node(4)
    r.right.left = Node(3)

    print ''
    ancestor_matrix(r, 6)


"""
http://www.geeksforgeeks.org/sink-odd-nodes-binary-tree/
"""

def swap_node_vals(node1, node2):
    tmp = node1.data
    node1.data = node2.data
    node2.data = tmp


def sink(root):
    if root is None or is_leaf(root):
        return

    if root.left is not None and root.left.data % 2 == 0:
        swap_node_vals(root, root.left)
        sink(root.left)
    elif root.right is not None and root.right.data % 2 == 0:
        swap_node_vals(root, root.right)
        sink(root.right)


def sink_odd_nodes(root):
    if root is None or is_leaf(root):
        return

    sink_odd_nodes(root.left)
    sink_odd_nodes(root.right)

    if root.data % 2 != 0:
        sink(root)


if __name__ == '__main__':
    print ''
    root = Node(1)
    root.left = Node(5)
    root.right = Node(8)
    root.left.left = Node(2)
    root.left.right = Node(4)
    root.right.left = Node(9)
    root.right.right = Node(10)

    sink_odd_nodes(root)
    print_level_order(root)


"""
http://www.geeksforgeeks.org/check-if-removing-an-edge-can-divide-a-binary-tree-in-two-halves/
"""


def count_nodes(root):
    if root is None:
        return 0

    return 1 + count_nodes(root.left) + count_nodes(root.right)


TREE_DIVISIBLE_TO_HALF = False


def can_tree_be_divided_to_two_halves(root, n):
    global TREE_DIVISIBLE_TO_HALF
    if root is None:
        return 0

    l_size = can_tree_be_divided_to_two_halves(root.left, n)
    r_size = can_tree_be_divided_to_two_halves(root.right, n)
    s = 1 + l_size + r_size

    if n - s == s:
        TREE_DIVISIBLE_TO_HALF = True

    return s


if __name__ == '__main__':
    print ''
    root = Node(1)
    root.left = Node(5)
    root.right = Node(8)
    root.left.left = Node(2)
    root.right.left = Node(9)
    root.right.right = Node(10)

    can_tree_be_divided_to_two_halves(root, count_nodes(root))
    print TREE_DIVISIBLE_TO_HALF


"""
http://www.geeksforgeeks.org/maximum-difference-between-node-and-its-ancestor-in-binary-tree/
"""
from sys import maxint
MAX_DIFF_BW_NODE_AND_ANCESTOR = -maxint


def max_diff_bw_node_and_ancestor(root):
    global MAX_DIFF_BW_NODE_AND_ANCESTOR
    if root is None:
        return maxint

    l_min = max_diff_bw_node_and_ancestor(root.left)
    r_min = max_diff_bw_node_and_ancestor(root.right)

    MAX_DIFF_BW_NODE_AND_ANCESTOR = abs(root.data - min(l_min, r_min))
    return min(l_min, r_min, root.data)


if __name__ == '__main__':
    print ''
    root = Node(8)
    root.left = Node(3)
    root.right = Node(10)
    root.left.left = Node(1)
    root.left.right = Node(6)
    root.left.right.left = Node(4)
    root.left.right.right = Node(7)
    root.right.right = Node(14)
    root.right.right.left = Node(13)

    max_diff_bw_node_and_ancestor(root)
    print MAX_DIFF_BW_NODE_AND_ANCESTOR


