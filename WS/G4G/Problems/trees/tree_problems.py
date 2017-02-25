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


def convert_to_mirror(root):
    if root is None:
        return

    left = root.left
    root.left = root.right
    root.right = left

    convert_to_mirror(root.left)
    convert_to_mirror(root.right)


t = get_std_tree()
convert_to_mirror(t)
print t, t.left, t.right, t.right.left, t.right.right


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
