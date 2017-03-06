package workspace.ws.ds.algos.graphs;

import workspace.ws.ds.data.DirectedEdge;
import workspace.ws.ds.data.EdgeWeightedDiGraph;
import junit.framework.TestCase;
import static org.junit.Assert.assertArrayEquals;

public class NumberOfEmployeesUnderEveryManagerTest extends TestCase {

	private NumberOfEmployeesUnderEveryManager util;
	private EdgeWeightedDiGraph graph;

	public void setUp() {
		graph = new EdgeWeightedDiGraph(6);
		
		graph.addEdge(new DirectedEdge(0, 2));
		graph.addEdge(new DirectedEdge(1, 2));
		graph.addEdge(new DirectedEdge(2, 5));
		graph.addEdge(new DirectedEdge(3, 4));
		graph.addEdge(new DirectedEdge(4, 5));
		graph.addEdge(new DirectedEdge(5, 5));
		
		util = new NumberOfEmployeesUnderEveryManager(graph);
	}
	
	public void testHierarchy() {
		int[] hierarchy = util.getHierarchy();
		int[] expected = new int[] {0, 0, 2, 0, 1, 5};
		
		assertArrayEquals(hierarchy, expected);
	}
}
