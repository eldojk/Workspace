package workspace.ws.ds.algos.graphs;

import junit.framework.TestCase;
import workspace.ws.ds.data.Graph;

public class ConnectedComponentsTest extends TestCase {
	private Graph graph;

	protected void setUp() {
		graph = new Graph(13);
		graph.addEdge(0, 1);
		graph.addEdge(0, 2);
		graph.addEdge(0, 5);
		graph.addEdge(0, 6);
		graph.addEdge(5, 3);
		graph.addEdge(3, 4);
		graph.addEdge(5, 4);
		graph.addEdge(7, 8);
		graph.addEdge(9, 10);
		graph.addEdge(9, 12);
		graph.addEdge(9, 11);
		graph.addEdge(11, 12);
	}

	public void testComponentCount() {
		ConnectedComponents cc = new ConnectedComponents(graph);

		assertEquals(3, cc.getNumberOfComponents());
	}
	
	public void testComponentId() {
		ConnectedComponents cc = new ConnectedComponents(graph);

		assertEquals(0, cc.getComponentId(5));
	}
	
	public void testComponentConnectivity() {
		ConnectedComponents cc = new ConnectedComponents(graph);

		assertTrue(cc.isConnected(3, 1));
	}
}
