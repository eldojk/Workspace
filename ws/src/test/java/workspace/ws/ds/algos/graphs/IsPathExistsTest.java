package workspace.ws.ds.algos.graphs;

import junit.framework.TestCase;
import workspace.ws.ds.data.Graph;

public class IsPathExistsTest extends TestCase {
	private Graph graph;

	protected void setUp() {
		graph = new Graph();
		graph.initializeVertices(10);
		graph.addEdge(0, 1);
		graph.addEdge(0, 7);
		graph.addEdge(0, 2);
		graph.addEdge(2, 3);
		graph.addEdge(2, 7);
		graph.addEdge(1, 3);
		graph.addEdge(1, 4);
		graph.addEdge(3, 4);
		graph.addEdge(4, 5);
		graph.addEdge(5, 6);
		graph.addEdge(7, 6);
		graph.addEdge(8, 9);
	}

	public void testPathExists() {
		IsPathExists pathChecker = new IsPathExists(graph);
		
		assertTrue(pathChecker.doesPathExist(0, 7));
		assertFalse(pathChecker.doesPathExist(1, 9));
	}
}
