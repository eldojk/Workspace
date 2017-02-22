package workspace.ws.ds.algos.graphs;

import workspace.ws.ds.data.Graph;

/**
 * http://www.geeksforgeeks.org/eulerian-path-and-circuit/
 * 
 * @author eldo.joseph
 */

public class EulerianGraph {

	public static final int EULERIAN_CYCLE = 1;
	public static final int EULERIAN_PATH = 2;
	public static final int NON_EULERIAN = 3;

	private Graph graph;
	private boolean[] visited;

	public EulerianGraph(Graph graph) {
		this.graph = graph;
		visited = new boolean[graph.V()];
	}

	private void dfs(int source) {
		visited[source] = true;

		for (int neighbour : graph.adj(source)) {
			if (!visited[neighbour]) {
				dfs(neighbour);
			}
		}
	}

	private boolean areAllNonZeroDegreeVerticesConnected() {
		// find a non zero degree vertex

		int source = 0;
		for (source = 0; source < graph.V(); source++) {
			if (graph.adj(source).size() > 0) {
				break;
			}
		}

		// If there are no edges in the graph, return true
		if (source == graph.V())
			return true;

		// Start DFS traversal from a vertex with non-zero degree
		dfs(source);

		// Check if all non-zero degree vertices are visited
		for (int v = 0; v < graph.V(); v++) {
			if ((graph.adj(v).size() > 0) && (!visited[v])) {
				return false;
			}
		}

		return true;
	}

	public int checkEulerian() {
		if (!areAllNonZeroDegreeVerticesConnected()) {
			return NON_EULERIAN;
		}

		// count odd degree vertices
		int oddVerticesCount = 0;
		for (int v = 0; v < graph.V(); v++) {
			if (graph.adj(v).size() % 2 != 0) {
				oddVerticesCount++;
			}
		}

		if (oddVerticesCount == 2)
			return EULERIAN_PATH;
		else if (oddVerticesCount == 0)
			return EULERIAN_CYCLE;

		return NON_EULERIAN;
	}
}
