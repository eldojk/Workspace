"""
http://www.geeksforgeeks.org/construct-tree-from-ancestor-matrix/
"""
from G4G.Problems.bst.merge_two_balanced_bst import get_inorder_array
from G4G.Problems.bst.vertical_sum import Node


def create_level_map(matrix):
    level_map = {}
    for col in range(len(matrix)):
        count_of_ones = 0
        for row in range(len(matrix)):
            if matrix[row][col] == 1:
                count_of_ones += 1

        level_map[count_of_ones] = [col] if level_map.get(count_of_ones) is None else level_map[count_of_ones] + [col]

    print level_map
    return level_map


def tree_from_ancestor_matrix(matrix):
    nodes = [Node(i) for i in range(len(matrix))]
    used = [False for i in range(len(matrix))]
    level_map = create_level_map(matrix)

    root = nodes[level_map[0][0]]

    for level in sorted(level_map.keys()):

        for node in level_map[level]:

            next_level_nodes = level_map.get(level + 1, [])

            for child in next_level_nodes:
                if used[child]:
                    continue
                # if node is ancestor of child, then node is parent

                parent_node = nodes[node]
                child_node = nodes[child]

                if parent_node.left is None:
                    parent_node.left = child_node
                    used[child] = True
                elif parent_node.right is None:
                    parent_node.right = child_node
                    used[child] = True

    return root


if __name__ == '__main__':
    m = [
        [0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 1, 0],
        [0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 0]
    ]
    r = tree_from_ancestor_matrix(m)
    print get_inorder_array(r, [])
