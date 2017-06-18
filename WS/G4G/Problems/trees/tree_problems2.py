"""
amzn

http://www.geeksforgeeks.org/find-sum-left-leaves-given-binary-tree/
"""
from DS.algos.graphs.binary_tree import Node
from G4G.Problems.bst.merge_two_balanced_bst import get_inorder_array
from G4G.Problems.trees.level_order_traversal import print_level_order
from Queue import Queue


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
amzn

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
amzn

http://www.geeksforgeeks.org/find-minimum-depth-of-a-binary-tree/
"""


def min_depth(root):
    if root is None:
        return 0

    return 1 + min(min_depth(root.left), min_depth(root.right))


if __name__ == '__main__':
    print ''
    print 'min depth',
    r = Node(1)
    r.left = Node(2)
    r.right = Node(3)
    r.left.left = Node(4)
    r.left.right = Node(5)
    print min_depth(r)


"""
amzn

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
amzn

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
amzn

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


"""
http://www.geeksforgeeks.org/print-binary-tree-2-dimensions/
"""


def print_tree_in_2d(root, level):
    if root:
        print_tree_in_2d(root.right, level + 1)

        for i in range(level):
            print ' ',
        print root

        print_tree_in_2d(root.left, level + 1)


if __name__ == '__main__':
    r = get_std_tree()
    print ''
    print_tree_in_2d(r, 0)


"""
amzn

http://www.geeksforgeeks.org/construct-a-binary-tree-from-postorder-and-inorder/
"""


def search(array, s, e, el):
    for i in range(s, e + 1):
        if array[i] == el:
            return i

    return -1


PO_INDEX = None


def build_tree_from_po_and_io(po, io, start, end):
    global PO_INDEX
    if start > end:
        return None

    key = po[PO_INDEX]
    node = Node(key)
    PO_INDEX -= 1

    if start == end:
        return node

    in_idx = search(io, start, end, key)

    # start from right
    node.right = build_tree_from_po_and_io(po, io, in_idx + 1, end)
    node.left = build_tree_from_po_and_io(po, io, start, in_idx - 1)

    return node


def build_tree_from_post_order_and_inorder(post_order, in_order):
    global PO_INDEX
    PO_INDEX = len(post_order) - 1
    return build_tree_from_po_and_io(post_order, in_order, 0, len(post_order) - 1)


if __name__ == '__main__':
    r = build_tree_from_post_order_and_inorder([8, 4, 5, 2, 6, 7, 3, 1], [4, 8, 2, 5, 1, 6, 3, 7])
    print get_inorder_array(r, [])


"""
http://www.geeksforgeeks.org/find-largest-subtree-having-identical-left-and-right-subtrees/
"""


def is_sequence_same(l, r):
    if len(l) != len(r):
        return False

    for i in range(len(l)):
        if l[i] != r[i]:
            return False

    return True

LARGEST_SAME_SEQ = None


def largest_subtree_with_identical_l_and_r(root):
    global LARGEST_SAME_SEQ
    if root is None:
        return []

    l = largest_subtree_with_identical_l_and_r(root.left)
    r = largest_subtree_with_identical_l_and_r(root.right)

    if is_sequence_same(l, r):
        LARGEST_SAME_SEQ = l + [root.data] + r

    return l + [root.data] + r


if __name__ == '__main__':
    print ''

    r = Node(50)
    r.left = Node(10)
    r.right = Node(60)
    r.left.left = Node(5)
    r.left.right = Node(20)
    r.right.left = Node(70)
    r.right.right = Node(70)
    r.right.left.left = Node(65)
    r.right.left.right = Node(80)
    r.right.right.left = Node(65)
    r.right.right.right = Node(80)

    largest_subtree_with_identical_l_and_r(r)
    print LARGEST_SAME_SEQ, len(LARGEST_SAME_SEQ)


"""
http://www.geeksforgeeks.org/print-nodes-binary-tree-k-leaves/
"""


def print_nodes_with_k_elements(root, k):
    if root is None:
        return 0

    left_count = print_nodes_with_k_elements(root.left, k)
    right_count = print_nodes_with_k_elements(root.right, k)

    if left_count + right_count + 1 == k:
        print root,

    return left_count + right_count + 1


if __name__ == '__main__':
    print ''
    t = get_std_tree()
    print_nodes_with_k_elements(t, 3)
    print ''


"""
http://www.geeksforgeeks.org/subtree-given-sum-binary-tree/
"""


def subtree_with_sum_exists(root, k):
    if root is None:
        return 0, False

    left_sum, left_exists = subtree_with_sum_exists(root.left, k)
    right_sum, right_exists = subtree_with_sum_exists(root.right, k)

    root_sum = left_sum + right_sum + root.data

    if root_sum == k:
        return root_sum, True

    return root_sum, (left_exists or right_exists)


if __name__ == '__main__':
    print ''
    t = get_std_tree()
    print subtree_with_sum_exists(t, 11)


"""
http://www.geeksforgeeks.org/convert-tree-forest-even-nodes/
"""


class NNode(object):
    def __init__(self, data):
        self.data = data
        self.children = []

    def __repr__(self):
        return str(self.data)


TO_REMOVE = 0


def num_paths_to_remove_for_even_forest(root):
    global TO_REMOVE
    if root is None:
        return 0

    child_sizes = []
    for child in root.children:
        size = num_paths_to_remove_for_even_forest(child)
        child_sizes.append(size)

    for size in child_sizes:
        if size > 0 and size % 2 == 0:
            TO_REMOVE += 1

    return 1 + sum(child_sizes)


if __name__ == '__main__':
    print ''
    r = NNode(1)
    r.children = [NNode(2), NNode(3), NNode(4)]
    r.children[0].children = [NNode(5)]
    r.children[0].children[0].children = [NNode(9), NNode(10)]
    r.children[1].children = [NNode(6)]
    r.children[2].children = [NNode(7), NNode(8)]

    num_paths_to_remove_for_even_forest(r)
    print TO_REMOVE


"""
http://www.geeksforgeeks.org/check-if-a-given-binary-tree-is-heap/

Just one level order traversal of the given binary tree would be sufficient to check both the properties of binary heap
To check Complete binary tree property: Just check no NON NULL value should proceed,once any NULL value is inserted into
the queue.
Checking the other property of binary heap is very easy, while inserting the children of a node , just check that they
both are less than or greater than the parent.
"""


def is_tree_heap(root):
    q = Queue()
    q.put(root)

    null_found = False
    while not q.empty():
        node = q.get()

        if node.left:
            if null_found:
                return False
            if node.left.data < node.data:
                return False

            q.put(node.left)
        else:
            if not null_found:
                null_found = True

        if node.right:
            if null_found:
                return False
            if node.right.data < node.data:
                return False

            q.put(node.right)
        else:
            if not null_found:
                null_found = True

    return True


if __name__ == '__main__':
    print ''
    t = get_std_tree()
    print is_tree_heap(t)
    t.left.left.right = Node(9)
    print is_tree_heap(t)
    t.left.left.left = Node(8)
    print is_tree_heap(t)


"""
http://www.geeksforgeeks.org/tree-isomorphism-problem/
"""


def is_isomorphic(root1, root2):
    if root1 is None and root2 is None:
        return True

    if root1 is None or root2 is None:
        return False

    return is_isomorphic(root1.left, root2.left) and is_isomorphic(root1.right, root2.right)


if __name__ == '__main__':
    print ''
    print is_isomorphic(get_std_tree(), get_std_tree())


"""
http://tech-queries.blogspot.in/2010/04/quasi-isomorphic-trees.html
"""


def is_quasi_isomorphic(root1, root2):
    if root1 is None and root2 is None:
        return True

    if root1 is None or root2 is None:
        return False

    return (is_isomorphic(root1.left, root2.left) and is_isomorphic(root1.right, root2.right)) or \
           (is_isomorphic(root1.left, root2.right) and is_isomorphic(root1.right, root2.left))


if __name__ == '__main__':
    print ''
    print is_isomorphic(get_std_tree(), get_std_tree())


"""
min root to leaf path
"""


def min_path(root):
    if is_leaf(root):
        return 0

    l_min = maxint
    if root.left:
        l_min = min_path(root.left)

    r_min = maxint
    if root.right:
        r_min = min_path(root.right)

    return 1 + min(l_min, r_min)


if __name__ == '__main__':
    print ''
    r = Node(1)
    r.left = Node(2)
    r.right = Node(3)
    r.right.left = Node(4)

    print min_path(r)


"""
http://www.geeksforgeeks.org/check-if-two-nodes-are-on-same-path-in-a-tree/
"""

N1_TIME = -1
N1_IN_TIME = -1
N2_TIME = -1
N2_IN_TIME = -1
TIMER = 0


def check_nodes_are_on_same_path(root, n1, n2):
    global N1_TIME, N2_TIME, TIMER, N2_IN_TIME, N1_IN_TIME

    if root:
        TIMER += 1
        if root.data == n1:
            N1_IN_TIME = TIMER
        elif root.data == n2:
            N2_IN_TIME = TIMER

        check_nodes_are_on_same_path(root.left, n1, n2)
        check_nodes_are_on_same_path(root.right, n1, n2)

        TIMER += 1
        if root.data == n1:
            N1_TIME = TIMER
        elif root.data == n2:
            N2_TIME = TIMER


if __name__ == '__main__':
    r = get_std_tree()
    check_nodes_are_on_same_path(r, 1, 4)
    print (N1_IN_TIME < N2_IN_TIME and N1_TIME > N2_TIME) or \
          (N2_IN_TIME < N1_IN_TIME and N2_TIME > N1_TIME)


"""
Given a binary tree, sum all the root to leaf nodes and return the sum.

Ex:
          1
        /   \
      2      3
    /   \       \
   4     6       7

here ans: 124 + 126 + 137 = 387
"""


def get_num_represented_by_stack(stack):
    copy_stack = [i for i in stack]
    total = 0
    n = 1

    while len(copy_stack) != 0:
        total += copy_stack.pop().data * n
        n *= 10

    return total


SUM_REPRESENTED_BY_R_TO_S_PATHS = 0


def sum_of_all_root_to_leaf_representations(root, stack):
    global SUM_REPRESENTED_BY_R_TO_S_PATHS
    if root:
        stack.append(root)

        sum_of_all_root_to_leaf_representations(root.left, stack)
        sum_of_all_root_to_leaf_representations(root.right, stack)

        if is_leaf(root):
            num = get_num_represented_by_stack(stack)
            SUM_REPRESENTED_BY_R_TO_S_PATHS += num

        stack.pop()


if __name__ == '__main__':
    print ''
    r = Node(1)
    r.left = Node(2)
    r.right = Node(3)
    r.left.left = Node(4)
    r.left.right = Node(6)
    r.right.right = Node(7)

    sum_of_all_root_to_leaf_representations(r, [])
    print SUM_REPRESENTED_BY_R_TO_S_PATHS


"""
amzn

http://www.geeksforgeeks.org/longest-consecutive-sequence-binary-tree/
"""


LCSSL = 1


def longest_consecutive_sub_sequence_length(root, curr_len):
    global LCSSL

    if curr_len > LCSSL:
        LCSSL = curr_len

    if root.left:
        if root.left.data == root.data + 1:
            longest_consecutive_sub_sequence_length(root.left, curr_len + 1)
        else:
            longest_consecutive_sub_sequence_length(root.left, 1)

    if root.right:
        if root.right.data == root.data + 1:
            longest_consecutive_sub_sequence_length(root.right, curr_len + 1)
        else:
            longest_consecutive_sub_sequence_length(root.right, 1)


if __name__ == '__main__':
    print ''
    r = Node(6)
    r.right = Node(9)
    r.right.left = Node(7)
    r.right.right = Node(10)
    r.right.right.right = Node(11)

    longest_consecutive_sub_sequence_length(r, 1)
    print LCSSL

    LCSSL = 1

    r = Node(1)
    r.left = Node(2)
    r.right = Node(4)
    r.left.left = Node(3)
    r.right.left = Node(5)
    r.right.right = Node(6)
    r.right.right.left = Node(7)

    longest_consecutive_sub_sequence_length(r, 1)
    print LCSSL


"""
msft

https://www.careercup.com/question?id=5769792860454912
"""


def left_most_node_at_level(root, level):
    if level == 0:
        return root

    if root.left is None and root.right is None:
        return None

    if root.left:
        return left_most_node_at_level(root.left, level - 1)

    return left_most_node_at_level(root.right, level - 1)


if __name__ == '__main__':
    print ''
    print 'left most node at level'

    r = get_std_tree()
    print left_most_node_at_level(r, 2)
    print left_most_node_at_level(r, 1)


