"""
Connected graph. Detect cycle


"""
from DS.algos.graphs.graphs import Node


class EnhancedNode(Node):
    def __init__(self, id):
        Node.__init__(self, id)
        self.color = 0


class CycleDetector(object):
    def __init__(self, graph):
        self.graph = graph
        self.cycle_detected = False

    def dfs(self, node):
        node.is_visited = True
        for neighbour in self.graph[node]:
            if not neighbour.is_visited:
                neighbour.predecessor = node
                self.dfs(neighbour)
            elif neighbour.is_visited and node.predecessor != neighbour:
                self.cycle_detected = True

    def is_cycle_detected(self):
        node = self.graph.keys()[0]
        node.predecessor = None
        self.dfs(node)
        return self.cycle_detected
