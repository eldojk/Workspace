package workspace.ws.ds.algos.graphs;

import workspace.ws.ds.data.Edge;
import workspace.ws.ds.data.EdgeWeightedGraph;

/**
 * amzn
 * 
 * http://www.geeksforgeeks.org/check-given-graph-tree/
 * 
 * @author eldo.joseph
 */
public class IsGraphTree {

	private static boolean areAllVerticesVisited(boolean[] visited) {
		for (boolean value : visited) {
			if (!value)
				return false;
		}

		return true;
	}

	private static void dfs(EdgeWeightedGraph graph, boolean[] visited,
			int source) {
		visited[source] = true;

		for (Edge edge : graph.adj(source)) {
			int neighbour = edge.other(source);
			dfs(graph, visited, neighbour);
		}
	}

	public static boolean check(EdgeWeightedGraph graph) {
		CycleInUndirectedGraph cycleDetector = new CycleInUndirectedGraph(graph);

		// should not contain cycles
		if (cycleDetector.detectCycle())
			return false;

		// should be connected
		boolean[] visited = new boolean[graph.V()];
		dfs(graph, visited, 0);

		return areAllVerticesVisited(visited);
	}
}
