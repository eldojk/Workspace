package workspace.ws.ds.algos.graphs;

import junit.framework.TestCase;
import workspace.ws.ds.data.DiGraph;

public class StrongComponentsTest extends TestCase{
	private DiGraph graph;

	protected void setUp() {
		graph = new DiGraph(11);
		graph.addEdge(0, 1);
		graph.addEdge(1, 2);
		graph.addEdge(2, 0);
		graph.addEdge(1, 3);
		graph.addEdge(3, 4);
		graph.addEdge(4, 5);
		graph.addEdge(5, 3);
		graph.addEdge(6, 5);
		graph.addEdge(6, 7);
		graph.addEdge(7, 8);
		graph.addEdge(8, 9);
		graph.addEdge(9, 6);
		graph.addEdge(9, 10);
	}

	public void testStrongComponents() {
		StrongComponents sc = new StrongComponents(graph);
		
		int numComponents = sc.computeStronglyConnectedComponents();
		
		assertEquals(4, numComponents);
	}
}
