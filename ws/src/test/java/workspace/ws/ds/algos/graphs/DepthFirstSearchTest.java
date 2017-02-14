package workspace.ws.ds.algos.graphs;

import junit.framework.TestCase;
import workspace.ws.ds.data.Graph;

public class DepthFirstSearchTest extends TestCase {
	private Graph graph;

	protected void setUp() {
		graph = new Graph(8);
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
	}

	public void testDFS() {
		DepthFirstSearch dfsUtil = new DepthFirstSearch(graph);

		dfsUtil.depthFirstSearch(0);

		assertEquals(graph.getVertices().size(),
				dfsUtil.getVisitedVertices().length);
	}
}
