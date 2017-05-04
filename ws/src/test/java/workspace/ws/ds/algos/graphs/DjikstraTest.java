package workspace.ws.ds.algos.graphs;

import workspace.ws.ds.data.DirectedEdge;
import workspace.ws.ds.data.EdgeWeightedDiGraph;
import junit.framework.TestCase;

public class DjikstraTest extends TestCase{
	private EdgeWeightedDiGraph graph;
	
	public void setUp() {
		graph = new EdgeWeightedDiGraph(8);
		graph.addEdge(new DirectedEdge(0, 1, 5));
		graph.addEdge(new DirectedEdge(0, 4, 9));
		graph.addEdge(new DirectedEdge(0, 7, 8));
		graph.addEdge(new DirectedEdge(1, 2, 12));
		graph.addEdge(new DirectedEdge(1, 3, 15));
		graph.addEdge(new DirectedEdge(1, 7, 4));
		graph.addEdge(new DirectedEdge(2, 3, 3));
		graph.addEdge(new DirectedEdge(2, 6, 11));
		graph.addEdge(new DirectedEdge(3, 6, 9));
		graph.addEdge(new DirectedEdge(4, 5, 4));
		graph.addEdge(new DirectedEdge(4, 6, 20));
		graph.addEdge(new DirectedEdge(4, 7, 5));
		graph.addEdge(new DirectedEdge(5, 2, 1));
		graph.addEdge(new DirectedEdge(5, 6, 13));
		graph.addEdge(new DirectedEdge(7, 5, 6));
		graph.addEdge(new DirectedEdge(7, 2, 7));
	}
	
	public void testDjikstra() {
		Djikstra d = new Djikstra(graph, 0);
		int[] distTo = d.getDistances();
		
		for (int i : distTo) {
			System.out.println(i);
		}
	}
}
