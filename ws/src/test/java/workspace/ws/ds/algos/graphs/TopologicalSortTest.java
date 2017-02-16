package workspace.ws.ds.algos.graphs;

import junit.framework.TestCase;
import workspace.ws.ds.data.DiGraph;
import workspace.ws.ds.data.Stack;

public class TopologicalSortTest extends TestCase{
	private DiGraph graph;

	protected void setUp() {
		graph = new DiGraph(7);
		graph.addEdge(0, 1);
		graph.addEdge(0, 5);
		graph.addEdge(0, 2);
		graph.addEdge(6, 0);
		graph.addEdge(5, 2);
		graph.addEdge(3, 5);
		graph.addEdge(3, 2);
		graph.addEdge(3, 4);
		graph.addEdge(3, 6);
		graph.addEdge(6, 4);
		graph.addEdge(1, 4);
	}

	public void testTopologicalSort() {
		TopologicalSort ts = new TopologicalSort(graph);
		
		Stack topology = ts.getTopologicalSortedOrder();
		
		assertEquals(3, topology.pop());
		assertEquals(6, topology.pop());
		assertEquals(0, topology.pop());
		assertEquals(5, topology.pop());
		assertEquals(2, topology.pop());
		assertEquals(1, topology.pop());
		assertEquals(4, topology.pop());
		assertTrue(topology.isEmpty());
	}
}
