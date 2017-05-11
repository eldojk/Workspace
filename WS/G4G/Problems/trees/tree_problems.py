from Queue import Queue

from DS.algos.graphs.binary_tree import Node
from G4G.Problems.stacks.stack import Stack


def is_leaf(node):
    return node.left is None and node.right is None


def get_std_tree():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    return root


def get_child_sum_tree():
    root = Node(10)
    root.left = Node(8)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(5)
    root.right.left = Node(2)

    return root


def size_of_tree(root):
    if root is None:
        return 0

    return 1 + size_of_tree(root.left) + size_of_tree(root.right)


def are_tres_identical(root1, root2):
    if root1 is None and root2 is None:
        return True

    if root1 is None or root2 is None:
        return False

    if root1.data == root2.data:
        return are_tres_identical(root1.left, root2.left) and are_tres_identical(root1.right, root2.right)

    return False


def compute_depth(root):
    if root is None:
        return 0

    return 1 + max(compute_depth(root.left), compute_depth(root.right))


def delete_tree(root):
    if root is None:
        return

    delete_tree(root.left)
    delete_tree(root.right)
    print root.data, 'deleted'
    del root


def is_child_sum_property_true(root):
    if root is None:
        return True

    if root.left is None and root.right is None:
        return True

    if root.left is None:
        return root.data == root.right.data

    if root.right is None:
        return root.data == root.left.data

    is_satisfied = (root.data == root.left.data + root.right.data)
    is_children_satisfied = is_child_sum_property_true(root.left) and is_child_sum_property_true(root.right)
    return is_satisfied and is_children_satisfied


def satisfy_child_sum_property(root):
    if root is None:
        return

    satisfy_child_sum_property(root.left)
    satisfy_child_sum_property(root.right)

    left = root.left.data if root.left else 0
    right = root.right.data if root.right else 0

    if left == 0 and right == 0:
        return

    root.data = left + right


def count_leaves(root):
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return 1

    return count_leaves(root.left) + count_leaves(root.right)


def iterative_in_order(root):
    current = root
    s = Stack()
    done = False

    while not done:
        if current is not None:
            s.push(current)
            current = current.left

        else:
            if not s.is_empty():
                current = s.pop()
                print current,

                current = current.right
            else:
                done = True


print ''
t = get_std_tree()
iterative_in_order(t)
print ''


def iterative_pre_order(root):
    s = Stack()
    s.push(root)

    while not s.is_empty():
        node = s.pop()
        print node,

        if node.left:
            s.push(node.right)

        if node.right:
            s.push(node.left)


print ''
t = get_std_tree()
iterative_pre_order(t)
print ''


def iterative_post_order(root):
    s1 = Stack()
    s2 = Stack()

    s1.push(root)

    while not s1.is_empty():
        node = s1.pop()
        if node.left:
            s1.push(node.left)

        if node.right:
            s1.push(node.right)

        s2.push(node)

    while not s2.is_empty():
        print s2.pop(),


print ''
print 'iterative post order'
t = get_std_tree()
iterative_post_order(t)
print ''


def root_to_leaf_path_is_sum_k(root, k, curr_sum, curr_path):
    if root is None:
        return

    curr_sum += root.data
    curr_path.append(root)

    root_to_leaf_path_is_sum_k(root.left, k, curr_sum, curr_path)
    root_to_leaf_path_is_sum_k(root.right, k, curr_sum, curr_path)

    if is_leaf(root) and curr_sum == k:
        print curr_path

    curr_path.pop()


print ''
t = get_child_sum_tree()
root_to_leaf_path_is_sum_k(t, 21, 0, [])
root_to_leaf_path_is_sum_k(t, 23, 0, [])
root_to_leaf_path_is_sum_k(t, 14, 0, [])

"""
amzn

http://www.geeksforgeeks.org/check-if-a-binary-tree-is-subtree-of-another-binary-tree/
"""


def is_same_tree(root1, root2):
    if root1 is None and root2 is None:
        return True

    if root1 is None or root2 is None:
        return False

    if root1.data != root2.data:
        return False

    return is_same_tree(root1.left, root2.left) and is_same_tree(root1.right, root2.right)


def is_subtree(root1, root2):
    if root1:
        if root1.data == root2.data:
            return is_same_tree(root1, root2)

        is_found_left = is_subtree(root1.left, root2)
        is_found_right = is_subtree(root1.right, root2)

        return is_found_left or is_found_right


if __name__ == '__main__':
    print ''
    root1 = Node(26)
    root1.left = Node(10)
    root1.right = Node(3)
    root1.left.left = Node(4)
    root1.left.right = Node(6)
    root1.left.left.right = Node(30)
    root1.right.right = Node(3)

    root2 = Node(10)
    root2.left = Node(4)
    root2.right = Node(6)
    root2.left.right = Node(30)

    print is_subtree(root1, root2)

"""
http://www.geeksforgeeks.org/construct-binary-tree-from-inorder-traversal/
"""


def find_max_index(array, start, end):
    _max = array[start]
    max_index = start
    while start <= end:
        if array[start] > _max:
            _max = array[start]
            max_index = start

        start += 1

    return max_index


def special_binary_tree_from_inorder(array, start, end):
    if start > end:
        return None

    max_index = find_max_index(array, start, end)
    root = Node(array[max_index])
    root.left = special_binary_tree_from_inorder(array, start, max_index - 1)
    root.right = special_binary_tree_from_inorder(array, max_index + 1, end)

    return root


if __name__ == '__main__':
    print ''
    ar = [5, 10, 40, 30, 28]
    r = special_binary_tree_from_inorder(ar, 0, 4)

    print r
    print r.left, r.right
    print r.left.left, r.right.right

"""
amzn

http://www.geeksforgeeks.org/construct-a-special-tree-from-given-preorder-traversal/
"""

INDEX = 0


def get_spl_binary_tree_from_pre_order(pre_order, preLN):
    global INDEX
    if INDEX >= len(pre_order):
        return None

    root = Node(pre_order[INDEX])
    is_a_leaf = preLN[INDEX] == 'L'
    INDEX += 1

    if is_a_leaf:
        return root

    root.left = get_spl_binary_tree_from_pre_order(pre_order, preLN)
    root.right = get_spl_binary_tree_from_pre_order(pre_order, preLN)
    return root


if __name__ == '__main__':
    print ''
    pre_order = [10, 30, 20, 5, 15]
    preLN = ['N', 'N', 'L', 'L', 'L']

    r = get_spl_binary_tree_from_pre_order(pre_order, preLN)

    print r
    print r.left, r.right
    print r.left.left, r.left.right

"""
http://www.geeksforgeeks.org/reverse-level-order-traversal/
"""


def reverse_level_order(root):
    q = Queue()
    s = Stack()

    q.put(root)

    while not q.empty():
        node = q.get()

        s.push(node)

        if node.right:
            q.put(node.right)

        if node.left:
            q.put(node.left)

    return s


def print_reverse_level_order(stack):
    while not stack.is_empty():
        print stack.pop(),


if __name__ == '__main__':
    print ''
    r = get_std_tree()
    print_reverse_level_order(reverse_level_order(r))
    print ''

"""
http://www.geeksforgeeks.org/linked-complete-binary-tree-its-creation/
"""


def create_linked_binary_tree(array):
    q = Queue()
    i = 0
    root = Node(array[i])
    q.put(root)
    max_index = len(array) - 1
    i += 1

    while not q.empty():
        node = q.get()

        if i <= max_index:
            node.left = Node(array[i])
            i += 1
            q.put(node.left)

        if i <= max_index:
            node.right = Node(array[i])
            i += 1
            q.put(node.right)

    return root


if __name__ == '__main__':
    print ''
    root = create_linked_binary_tree([1, 2, 3, 4, 5])
    print root, root.left, root.right, root.left.left, root.left.right

"""
http://www.geeksforgeeks.org/foldable-binary-trees/
"""


def is_foldable_binary_tree(root):
    if root is None:
        return True

    return is_foldable_bt(root.left, root.right)


def is_foldable_bt(root1, root2):
    """
    check if trees are structural mirrors of each other

    :param root1:
    :param root2:
    :return:
    """
    if root1 is None and root2 is None:
        return True

    if root1 is None or root2 is None:
        return False

    return is_foldable_bt(root1.left, root2.right) and is_foldable_bt(root1.right, root2.left)


if __name__ == '__main__':
    print ''

    root = Node(10)
    root.left = Node(7)
    root.right = Node(15)
    root.left.right = Node(9)

    print is_foldable_binary_tree(root)

    root.right.left = Node(11)

    print is_foldable_binary_tree(root)

"""
http://www.geeksforgeeks.org/difference-between-sums-of-odd-and-even-levels/
"""


def diff_bw_sum_of_odd_and_even_levels(root):
    q = Queue()
    q.put((root, 1))
    level_sum = {}

    while not q.empty():
        el = q.get()
        node = el[0]
        level = el[1]
        level_sum[level] = node.data if level_sum.get(level) is None else level_sum[level] + node.data

        if node.left:
            q.put((node.left, level + 1))
        if node.right:
            q.put((node.right, level + 1))

    levels = level_sum.keys()

    odd_sum = 0
    even_sum = 0
    for l in levels:
        if l % 2 == 0:
            even_sum += level_sum[l]
        else:
            odd_sum += level_sum[l]

    print abs(odd_sum - even_sum)


if __name__ == '__main__':
    print ''

    root = Node(5)

    root.left = Node(2)
    root.right = Node(6)

    root.left.left = Node(1)
    root.left.right = Node(4)

    root.left.right.left = Node(3)

    root.right.right = Node(8)
    root.right.right.left = Node(7)
    root.right.right.right = Node(9)

    diff_bw_sum_of_odd_and_even_levels(root)

"""
http://www.geeksforgeeks.org/find-depth-of-the-deepest-odd-level-node/
"""

DEEPEST_LEVEL = 0
DEEPEST_NODE = None


def deepest_odd_level_node(root, level):
    global DEEPEST_LEVEL, DEEPEST_NODE

    if root:
        if is_leaf(root):
            if level > DEEPEST_LEVEL and level % 2 != 0:
                DEEPEST_LEVEL = level
                DEEPEST_NODE = root

        deepest_odd_level_node(root.left, level + 1)
        deepest_odd_level_node(root.right, level + 1)


if __name__ == '__main__':
    print ''

    root = Node(1)

    root.left = Node(2)
    root.right = Node(3)

    root.left.left = Node(4)

    root.right.left = Node(5)
    root.right.right = Node(6)

    root.right.left.right = Node(7)
    root.right.left.right.left = Node(9)

    root.right.right.right = Node(8)
    root.right.right.right.right = Node(10)
    root.right.right.right.right.left = Node(11)

    deepest_odd_level_node(root, 1)
    print DEEPEST_NODE

"""
http://www.geeksforgeeks.org/check-leaves-level/
"""

LEAF_LEVEL_FOUND = -1


def check_all_leaves_at_same_level(root, level):
    global LEAF_LEVEL_FOUND

    if root:
        if is_leaf(root):
            if LEAF_LEVEL_FOUND != -1 and LEAF_LEVEL_FOUND != level:
                return False
            elif LEAF_LEVEL_FOUND == -1:
                LEAF_LEVEL_FOUND = level
                return True

        left_check = check_all_leaves_at_same_level(root.left, level + 1)
        right_check = check_all_leaves_at_same_level(root.right, level + 1)

        return left_check and right_check

    return True


if __name__ == '__main__':
    print ''
    root = Node(1)

    root.left = Node(2)
    root.right = Node(3)

    root.left.left = Node(4)

    print check_all_leaves_at_same_level(root, 0)

    root.right.right = Node(6)

    print check_all_leaves_at_same_level(root, 0)

"""
http://www.geeksforgeeks.org/print-left-view-binary-tree/
"""


def left_view(root, level, lv):
    if root:
        if level >= len(lv):
            lv.append(root)

        left_view(root.left, level + 1, lv)
        left_view(root.right, level + 1, lv)


def print_left_view(root):
    # using array to keep track of level bcoz hash is too mainstream :p
    lv = []
    left_view(root, 0, lv)
    print lv


if __name__ == '__main__':
    root = Node(12)

    root.left = Node(10)
    root.right = Node(30)

    root.right.left = Node(25)
    root.right.right = Node(40)

    print_left_view(root)

"""
http://www.geeksforgeeks.org/deepest-left-leaf-node-in-a-binary-tree/
"""

DEEPEST_LEFT_LEAF = None
DEEPEST_LEFT_LEAF_LEVEL = -1


def _find_deepest_left_leaf(root, level, is_came_left):
    global DEEPEST_LEFT_LEAF, DEEPEST_LEFT_LEAF_LEVEL
    if root:
        if is_leaf(root) and is_came_left:
            if DEEPEST_LEFT_LEAF_LEVEL < level:
                DEEPEST_LEFT_LEAF_LEVEL = level
                DEEPEST_LEFT_LEAF = root

        _find_deepest_left_leaf(root.left, level + 1, True)
        _find_deepest_left_leaf(root.right, level + 1, False)


def find_deepest_left_leaf(root):
    _find_deepest_left_leaf(root, 0, True)
    return DEEPEST_LEFT_LEAF


if __name__ == '__main__':
    print ''
    root = Node(1)

    root.left = Node(2)
    root.right = Node(3)

    root.left.left = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)

    root.right.left.right = Node(7)
    root.right.left.right.left = Node(9)

    root.right.right.right = Node(8)
    root.right.right.right.right = Node(10)

    print find_deepest_left_leaf(root)

"""
http://www.geeksforgeeks.org/sum-numbers-formed-root-leaf-paths/
"""

SUM_ROOT_TO_LEAF = 0


def sum_of_all_number_formed_by_root_to_leaf_paths(root, curr_sum):
    global SUM_ROOT_TO_LEAF
    if root:
        curr_sum = curr_sum * 10 + root.data
        if is_leaf(root):
            SUM_ROOT_TO_LEAF += curr_sum

        sum_of_all_number_formed_by_root_to_leaf_paths(root.left, curr_sum)
        sum_of_all_number_formed_by_root_to_leaf_paths(root.right, curr_sum)


if __name__ == '__main__':
    print ''
    root = Node(6)

    root.left = Node(3)
    root.right = Node(5)

    root.left.left = Node(2)
    root.left.right = Node(5)
    root.right.right = Node(4)

    root.left.right.left = Node(7)
    root.left.right.right = Node(4)

    sum_of_all_number_formed_by_root_to_leaf_paths(root, 0)
    print SUM_ROOT_TO_LEAF


"""
http://www.geeksforgeeks.org/print-nodes-dont-sibling-binary-tree/
"""


def print_nodes_without_sibling(root):
    if root:
        if is_leaf(root):
            return

        if root.left is not None and root.right is None:
            print root.left,

        if root.right is not None and root.left is None:
            print root.right,

        print_nodes_without_sibling(root.left)
        print_nodes_without_sibling(root.right)


if __name__ == '__main__':
    print ''
    root = Node(1)

    root.left = Node(2)
    root.right = Node(3)

    root.left.right = Node(4)
    root.right.left = Node(5)

    root.right.left.left = Node(6)

    print_nodes_without_sibling(root)


"""
amzn

http://www.geeksforgeeks.org/check-two-nodes-cousins-binary-tree/
"""


def find_parents(root, nodes, parents, parent, level):
    if root:
        for i in range(len(nodes)):
            if nodes[i] == root.data:
                parents[i][0] = parent
                parents[i][1] = level

        find_parents(root.left, nodes, parents, root, level + 1)
        find_parents(root.right, nodes, parents, root, level + 1)


def are_nodes_cousins(root, n1, n2):
    parents = [[None, 0], [None, 0]]
    find_parents(root, [n1, n2], parents, None, 0)
    return parents[0][0] != parents[1][0] and parents[0][1] == parents[1][1]


if __name__ == '__main__':
    print ''
    print ''
    r = get_std_tree()
    r.right.left = Node(6)
    r.right.right = Node(7)

    print are_nodes_cousins(r, 4, 6)
    print are_nodes_cousins(r, 4, 5)
    print are_nodes_cousins(r, 4, 3)