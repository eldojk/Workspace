from random import randint
from unittest import TestCase

from DS.algos.graphs.graphs import GraphBuilder


class GraphsTestCase(TestCase):

    def setUp(self):
        self.graph_bldr = GraphBuilder(10)
        for i in range(40):
            self.graph_bldr.connect(randint(0,9), randint(0,9))
            i += 1
        self.graph = self.graph_bldr.build()

    def test_graph(self):
        self.assertIsNotNone(self.graph)
        self.graph_bldr.print_graph()