package workspace.ws.ds.algos.graphs;

import junit.framework.TestCase;
import workspace.ws.ds.data.DiGraph;

public class CycleInDirectedGraphTest extends TestCase{
	private DiGraph digraph;
	
	public void setUp() {
		digraph = new DiGraph(6);
		digraph.addEdge(0, 1);
		digraph.addEdge(1, 2);
		digraph.addEdge(0, 2);
		digraph.addEdge(3, 0);
		digraph.addEdge(3, 4);
		digraph.addEdge(4, 5);
		digraph.addEdge(5, 3);
	}
	
	public void testCycle() {
		CycleInDirectedGraph util = new CycleInDirectedGraph(digraph);
		assertTrue(util.isCyclePresent());
	}
}
