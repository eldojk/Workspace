from unittest import TestCase

from DS.algos.graphs.graphs import GraphBuilder
from G4G.Problems.graphs.reachablity import is_reachable


class ConnectedComponentsTestCase(TestCase):
    def setUp(self):
        self.graph_builder = GraphBuilder(11)
        self.graph_builder.directional_connect(0, 1)
        self.graph_builder.directional_connect(1, 2)
        self.graph_builder.directional_connect(2, 0)
        self.graph_builder.directional_connect(1, 3)
        self.graph_builder.directional_connect(3, 4)
        self.graph_builder.directional_connect(4, 5)
        self.graph_builder.directional_connect(5, 3)
        self.graph_builder.directional_connect(6, 5)
        self.graph_builder.directional_connect(6, 7)
        self.graph_builder.directional_connect(7, 8)
        self.graph_builder.directional_connect(8, 9)
        self.graph_builder.directional_connect(9, 6)
        self.graph_builder.directional_connect(9, 10)
        self.graph = self.graph_builder.build()

    def test_reachablity(self):
        nodes = self.graph_builder.get_nodes_with_ids([0, 5])
        node1 = nodes[0] if nodes[0].id == 0 else nodes[1]
        node2 = nodes[0] if nodes[0].id == 5 else nodes[1]

        self.assertTrue(is_reachable(node1, node2, self.graph))

    def test_reachablity_unreachable(self):
        nodes = self.graph_builder.get_nodes_with_ids([0, 6])
        node1 = nodes[0] if nodes[0].id == 0 else nodes[1]
        node2 = nodes[0] if nodes[0].id == 6 else nodes[1]

        self.assertFalse(is_reachable(node1, node2, self.graph))