package workspace.ws.ds.algos.graphs;

import workspace.ws.ds.data.DirectedEdge;
import workspace.ws.ds.data.EdgeWeightedDiGraph;
import workspace.ws.ds.data.Stack;

/**
 * http://www.geeksforgeeks.org/find-number-of-employees-under-every-manager/
 * 
 * @author eldo.joseph
 */
public class NumberOfEmployeesUnderEveryManager {
	private EdgeWeightedDiGraph graph;
	private TopologicalSortOnEdgeListGraph top;

	public NumberOfEmployeesUnderEveryManager(EdgeWeightedDiGraph graph) {
		this.graph = graph;
		top = new TopologicalSortOnEdgeListGraph(graph);
	}

	public int[] getHierarchy() {
		Stack topology = top.getTopologicalSortedOrder();

		int[] hierarchy = new int[graph.V()];

		while (!topology.isEmpty()) {
			int employee = (int) topology.pop();

			for (DirectedEdge edge : graph.adj(employee)) {

				int manager = edge.to();
				
				if (employee != manager)
					hierarchy[manager] += 1 + hierarchy[employee];
			}
		}

		return hierarchy;
	}
}
