from unittest import TestCase

from DS.algos.graphs.graphs import GraphBuilder
from DS.algos.graphs.strongly_connected_components import EnhancedNode, StrongComponents


class ConnectedComponentsTestCase(TestCase):
    def setUp(self):
        self.graph_builder = GraphBuilder(5, graph_node=EnhancedNode)
        self.graph_builder.directional_connect(1, 0)
        self.graph_builder.directional_connect(0, 2)
        self.graph_builder.directional_connect(2, 1)
        self.graph_builder.directional_connect(0, 3)
        self.graph_builder.directional_connect(3, 4)
        self.graph = self.graph_builder.build()

        self.graph_builder = GraphBuilder(11, graph_node=EnhancedNode)
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
        self.graph2 = self.graph_builder.build()

    def test_connected_components(self):
        cc = StrongComponents(self.graph)
        self.assertEqual(3, cc.get_number_of_components())

        cc = StrongComponents(self.graph2)
        self.assertEqual(4, cc.get_number_of_components())
