package workspace.ws.ds.algos.graphs;

import junit.framework.TestCase;
import workspace.ws.ds.data.Graph;

public class EulerianGraphTest extends TestCase {
	private Graph graph;

	protected void setUp() {
		graph = new Graph(5);

		graph.addEdge(0, 1);
		graph.addEdge(1, 2);
		graph.addEdge(0, 2);
		graph.addEdge(3, 0);
		graph.addEdge(3, 4);
	}

	public void testEulerianPath() {
		EulerianGraph eulerian = new EulerianGraph(graph);

		assertEquals(EulerianGraph.EULERIAN_PATH, eulerian.checkEulerian());
	}
	
	public void testEulerianCycle() {
		graph.addEdge(0, 4);
		EulerianGraph eulerian = new EulerianGraph(graph);

		assertEquals(EulerianGraph.EULERIAN_CYCLE, eulerian.checkEulerian());
	}
	
	public void testNonEulerianGraph() {
		graph.addEdge(3, 1);
		EulerianGraph eulerian = new EulerianGraph(graph);

		assertEquals(EulerianGraph.NON_EULERIAN, eulerian.checkEulerian());
	}
}
