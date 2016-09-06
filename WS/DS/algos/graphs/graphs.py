"""
Custom Graph implementation
"""


class Node(object):
    """
    This is a custom Graph node
    """
    def __init__(self, id):
        self.is_visited = False
        self.id = id
        self.distance = None
        self.predecessor = None

    def set_visited(self):
        self.is_visited = True


class GraphBuilder(object):
    """
    Build a graph using this
    """
    def __init__(self, num_vertices, graph_node=Node):
        self.is_built = False
        self.vertices = [graph_node(i) for i in range(num_vertices)]
        self._graph = {v: [] for v in self.vertices}

    def connect(self, a, b):
        """
        adds a->b connection

        :param a:
        :param b:
        :return:
        """
        if a != b:
            node_a = self.vertices[a]
            node_b = self.vertices[b]
            self._graph[node_a] = self._graph[node_a] + [node_b]
            self._graph[node_b] = self._graph[node_b] + [node_a]
            self.is_built = False

    def directional_connect(self, a, b):
        """
        adds a->b connection

        :param a:
        :param b:
        :return:
        """
        if a != b:
            node_a = self.vertices[a]
            node_b = self.vertices[b]
            self._graph[node_a] = self._graph[node_a] + [node_b]
            self.is_built = False

    def build(self):
        """
        Clean and build graph

        :return:
        """
        for v in self._graph.keys():
            # removing duplicates
            connections = self._graph[v]
            self._graph[v] = list(set(connections))

        self.is_built = True
        return self._graph

    def get_nodes_with_ids(self, ids):
        return [node for node in self._graph.keys() if node.id in ids]

    def print_graph(self):
        """
        Print the current Graph state

        :return:
        """
        if not self.is_built:
            print "Graph not built yet!"
            return

        line = ''
        line_template = '{0} : {1}\n'
        for n in self._graph.keys():
            lt = line_template.format(n.id, [_n.id for _n in self._graph[n]])
            line += lt

        print line
