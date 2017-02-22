package workspace.ws.ds.algos.graphs;

import junit.framework.TestCase;
import workspace.ws.ds.data.Edge;
import workspace.ws.ds.data.EdgeWeightedGraph;

public class CycleInUndirectedGraphTest extends TestCase {
	private EdgeWeightedGraph graph;

	protected void setUp() {
		graph = new EdgeWeightedGraph(3);
		
		graph.addEdge(new Edge(0, 1, 1));
		graph.addEdge(new Edge(1, 2, 1));
	}

	public void testCycleExists() {
		graph.addEdge(new Edge(2, 0, 1));
		CycleInUndirectedGraph cycleDetector = new CycleInUndirectedGraph(graph);
		
		assertTrue(cycleDetector.detectCycle());
	}
	
	public void testCycleDoesNotExist() {
		CycleInUndirectedGraph cycleDetector = new CycleInUndirectedGraph(graph);
		
		assertFalse(cycleDetector.detectCycle());
	}
}
