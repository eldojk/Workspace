"""
If a sum from root to leaf is found, print that path
"""

# todo: this could be wrong


from vertical_sum import Node


def print_sum(root, sm):
    if root is None:
        return sm == 0

    else:
        lf = print_sum(root.left, sm - root.data)
        if lf:
            print root.data
            return True

        rf = print_sum(root.right, sm - root.data)
        if rf:
            print root.data
            return True

        return False


r = Node(1)
r.left = Node(2)
r.right = Node(3)
r.left.left = Node(1)
r.right.right = Node(4)

print_sum(r, 8)
