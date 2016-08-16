"""
Pre-process and find connected components in a graph using DFS. Answer questions like is u connected to v in constant
time.

An array is better than this implementation
"""
from DS.algos.graphs.graphs import Node


class EnhancedNode(Node):
    def __init__(self, id):
        Node.__init__(self, id)
        self.cc = None


class ConnectedComponents(object):
    def __init__(self, graph):
        self.graph = graph
        self.count = 0
        self.process_graph()

    def dfs(self, node):
        node.is_visited = True
        node.cc = self.count
        for neighbour in self.graph[node]:
            if not neighbour.is_visited:
                self.dfs(neighbour)

    def process_graph(self):
        _count = 0
        for node in self.graph.keys():
            node.cc = _count
            _count += 1

        for node in self.graph.keys():
            if not node.is_visited:
                self.dfs(node)
                self.count += 1

    def is_connected(self, node1, node2):
        return node1.cc == node2.cc
