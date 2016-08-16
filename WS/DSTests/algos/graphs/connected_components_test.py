from unittest import TestCase

from DS.algos.graphs.connected_components import EnhancedNode, ConnectedComponents
from DS.algos.graphs.graphs import GraphBuilder


class BipartiteTestCase(TestCase):
    def setUp(self):
        self.graph_builder = GraphBuilder(13, graph_node=EnhancedNode)
        self.graph_builder.connect(0, 1)
        self.graph_builder.connect(0, 2)
        self.graph_builder.connect(0, 6)
        self.graph_builder.connect(0, 5)
        self.graph_builder.connect(5, 3)
        self.graph_builder.connect(5, 4)
        self.graph_builder.connect(3, 4)
        self.graph_builder.connect(7, 8)
        self.graph_builder.connect(9, 10)
        self.graph_builder.connect(9, 11)
        self.graph_builder.connect(9, 12)
        self.graph_builder.connect(11, 12)
        self.graph = self.graph_builder.build()

    def test_connected_components(self):
        cc = ConnectedComponents(self.graph)

        nodes = self.graph_builder.get_nodes_with_ids([0, 1])
        self.assertTrue(cc.is_connected(nodes[0], nodes[1]))

        nodes = self.graph_builder.get_nodes_with_ids([0, 7])
        self.assertFalse(cc.is_connected(nodes[0], nodes[1]))

        nodes = self.graph_builder.get_nodes_with_ids([0, 3])
        self.assertTrue(cc.is_connected(nodes[0], nodes[1]))

        nodes = self.graph_builder.get_nodes_with_ids([10, 12])
        self.assertTrue(cc.is_connected(nodes[0], nodes[1]))

        nodes = self.graph_builder.get_nodes_with_ids([6, 11])
        self.assertFalse(cc.is_connected(nodes[0], nodes[1]))