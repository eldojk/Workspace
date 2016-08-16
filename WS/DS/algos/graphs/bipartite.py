"""
Bi-partite or two coloring

We will use boolean values as there are only 2 colors
"""
from Queue import Queue

from DS.algos.graphs.graphs import Node


class EnhancedNode(Node):
    def __init__(self, id):
        Node.__init__(self, id)
        self.color = None


class BiPartiteChecker(object):
    def __init__(self, graph):
        self.graph = graph
        self.is_bipartite = None
        self.bfs_process(self.graph.keys()[0])

    def bfs_process(self, node):
        queue = Queue()
        node.color = True
        queue.put(node)

        while not queue.empty():
            node = queue.get()

            for neighbour in self.graph[node]:
                if not neighbour.is_visited:
                    # If uncolored, color the neighbour
                    if neighbour.color is None:
                        neighbour.color = not node.color
                    # If colored, check if the complementary color is used
                    elif neighbour.color == node.color:
                        self.is_bipartite = False
                        break
                    queue.put(neighbour)

            node.is_visited = True

            # If bipartite case found, break
            if self.is_bipartite is not None:
                break

        # If this variable is still none, it means the graph is bipartite
        if self.is_bipartite is None:
            self.is_bipartite = True

    def is_graph_bipartite(self):
        return self.is_bipartite
