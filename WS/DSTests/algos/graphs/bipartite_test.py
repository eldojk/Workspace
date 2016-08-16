from unittest import TestCase

from DS.algos.graphs.bipartite import EnhancedNode, BiPartiteChecker
from DS.algos.graphs.graphs import GraphBuilder


class BipartiteTestCase(TestCase):
    def setUp(self):
        self.graph_builder = GraphBuilder(6, graph_node=EnhancedNode)
        self.graph_builder.connect(0, 4)
        self.graph_builder.connect(0, 5)
        self.graph_builder.connect(1, 3)
        self.graph_builder.connect(2, 4)
        self.graph = self.graph_builder.build()

    def test_bipartite(self):
        bp_checker = BiPartiteChecker(self.graph)
        self.assertTrue(bp_checker.is_graph_bipartite())

    def test_bipartite_another(self):
        self.graph_builder.connect(0, 1)
        self.graph = self.graph_builder.build()
        bp_checker = BiPartiteChecker(self.graph)
        self.assertTrue(bp_checker.is_graph_bipartite())

    def test_non_bipartite(self):
        self.graph_builder.connect(0, 1)
        self.graph_builder.connect(0, 3)
        self.graph = self.graph_builder.build()
        bp_checker = BiPartiteChecker(self.graph)
        self.assertFalse(bp_checker.is_graph_bipartite())
