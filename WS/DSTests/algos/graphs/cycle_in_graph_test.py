from unittest import TestCase

from DS.algos.graphs.cycle_in_graph import CycleDetector
from DS.algos.graphs.graphs import GraphBuilder


class CycleDetectionTest(TestCase):
    def setUp(self):
        self.graph_builder = GraphBuilder(5)
        self.graph_builder.connect(1, 0)
        self.graph_builder.connect(2, 0)
        self.graph_builder.connect(0, 3)
        self.graph_builder.connect(3, 4)
        self.graph = self.graph_builder.build()

    def test_cycle(self):
        cd = CycleDetector(self.graph)
        self.assertEqual(cd.is_cycle_detected(), False)

    def test_cycle_exist(self):
        self.graph_builder.connect(1, 2)
        self.graph = self.graph_builder.build()
        cd = CycleDetector(self.graph)
        self.assertEqual(cd.is_cycle_detected(), True)
