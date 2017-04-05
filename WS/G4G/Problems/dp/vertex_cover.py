# coding=utf-8
"""
http://www.geeksforgeeks.org/vertex-cover-problem-set-2-dynamic-programming-solution-tree/

A vertex cover of an undirected graph is a subset of its vertices such that for every edge (u, v) of the graph, either
‘u’ or ‘v’ is in vertex cover. Although the name is Vertex Cover, the set covers all edges of the given graph.

1) Root is part of vertex cover: In this case root covers all children edges. We recursively calculate size of vertex
covers for left and right subtrees and add 1 to the result (for root).

2) Root is not part of vertex cover: In this case, both children of root must be included in vertex cover to cover all
root to children edges. We recursively calculate size of vertex covers of all grandchildren and number of children to
the result (for two children of root).
"""
class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.vc = None

    def __repr__(self):
        return str(self.data)


def vertex_cover(root):
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return 0

    if root.vc is not None:
        return root.vc

    # include root in vc
    size_including_root = 1 + vertex_cover(root.left) + vertex_cover(root.right)

    # exclude root in vc, then left and right if exists has to be in vc
    size_excluding_root = 0

    if root.left:
        size_excluding_root += 1 + vertex_cover(root.left.left) + vertex_cover(root.left.right)

    if root.right:
        size_excluding_root += 1 + vertex_cover(root.right.left) + vertex_cover(root.right.right)

    # memoize
    root.vc = min(size_excluding_root, size_including_root)

    return root.vc


if __name__ == '__main__':
    r = Node(10)
    r.left = Node(20)
    r.right = Node(30)
    r.left.left = Node(40)
    r.left.right = Node(50)
    r.right.right = Node(60)
    r.left.right.left = Node(70)
    r.left.right.right = Node(80)

    print vertex_cover(r)