"""
http://www.geeksforgeeks.org/find-sum-left-leaves-given-binary-tree/
"""
from DS.algos.graphs.binary_tree import Node
from G4G.Problems.bst.merge_two_balanced_bst import get_inorder_array


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























































