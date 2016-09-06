"""
Kosaraju algorithm
"""
from DS.algos.graphs.graphs import Node


class EnhancedNode(Node):
    def __init__(self, id):
        Node.__init__(self, id)
        self.cc = None


class StrongComponents(object):
    def __init__(self, graph):
        self.graph = graph
        self.transpose = {key: [] for key in self.graph.keys()}
        self.stack = []
        self.cc_num = 0
        self.pre_process_for_cc()

    def transpose_graph(self):
        for vertex in self.graph:
            adj_vertices = self.graph[vertex]
            for adj_v in adj_vertices:
                self.transpose[adj_v].append(vertex)

    def _dfs_initial_visit(self, vertex):
        if not vertex.is_visited:
            vertex.is_visited = True
            for adj_v in self.graph[vertex]:
                self._dfs_initial_visit(adj_v)
            self.stack.append(vertex)

    def dfs_initial(self):
        for vertex in self.graph:
            if not vertex.is_visited:
                self._dfs_initial_visit(vertex)

    def un_visit_all_vertices(self):
        for v in self.graph:
            v.is_visited = False

    def _dfs_final_visit(self, vertex):
        if not vertex.is_visited:
            vertex.is_visited = True
            vertex.cc = self.cc_num
            for v in self.transpose[vertex]:
                self._dfs_final_visit(v)

    def dfs_final(self):
        while len(self.stack) > 0:
            vertex = self.stack.pop()
            if not vertex.is_visited:
                self.cc_num += 1
                self._dfs_final_visit(vertex)

    def pre_process_for_cc(self):
        self.dfs_initial()
        self.un_visit_all_vertices()
        self.transpose_graph()
        self.dfs_final()

    def get_number_of_components(self):
        return self.cc_num
