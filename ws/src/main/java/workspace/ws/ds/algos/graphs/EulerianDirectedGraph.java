package workspace.ws.ds.algos.graphs;

import java.util.Set;

import workspace.ws.ds.data.DiGraph;

/**
 * amzn
 * 
 * http://www.geeksforgeeks.org/euler-circuit-directed-graph/
 * 
 * A directed graph has an eulerian cycle if following conditions are true: All
 * vertices with nonzero degree belong to a single strongly connected component.
 * i.e. There is only one sc.
 * 
 * In degree and out degree of every vertex is same.
 * 
 * @author eldo.joseph
 *
 */
public class EulerianDirectedGraph {

	/**
	 * Checks if a digraph is Eulerian
	 * 
	 * @param graph
	 * @return
	 */
	public static boolean isEulerianCircuit(DiGraph graph) {
		if (!isStronglyConnected(graph))
			return false;

		int[] inDegree = getIndegreeArray(graph);

		for (int v = 0; v < graph.V(); v++) {

			if (graph.adj(v).size() != inDegree[v])
				return false;
		}

		return true;
	}

	/**
	 * Gets inDegree of all graph vertices
	 * 
	 * @param graph
	 * @return
	 */
	private static int[] getIndegreeArray(DiGraph graph) {
		int[] inDegree = new int[graph.V()];

		for (int v = 0; v < graph.V(); v++) {

			Set<Integer> neighbours = graph.adj(v);

			for (int neighbour : neighbours) {
				inDegree[neighbour]++;
			}
		}

		return inDegree;
	}

	/**
	 * Verifies if graph is strongly connected
	 * 
	 * @param graph
	 * @return
	 */
	private static boolean isStronglyConnected(DiGraph graph) {
		boolean[] visited = new boolean[graph.V()];
		dfs(0, visited, graph);

		for (int v = 0; v < graph.V(); v++) {

			if (!visited[v])
				return false;
		}

		DiGraph transpose = getTranspose(graph);
		visited = new boolean[graph.V()];

		dfs(0, visited, transpose);

		for (int v = 0; v < transpose.V(); v++) {

			if (!visited[v])
				return false;
		}

		return true;
	}

	/**
	 * Recursive depth first search
	 * 
	 * @param source
	 * @param visited
	 * @param graph
	 */
	private static void dfs(int source, boolean[] visited, DiGraph graph) {
		visited[source] = true;

		for (int neighbour : graph.adj(source)) {
			if (!visited[neighbour])
				dfs(neighbour, visited, graph);
		}
	}

	/**
	 * Get transpose of a graph
	 * 
	 * @param graph
	 * @return
	 */
	private static DiGraph getTranspose(DiGraph graph) {
		DiGraph transpose = new DiGraph(graph.V());

		for (int v = 0; v < graph.V(); v++) {
			Set<Integer> neighbours = graph.adj(v);

			for (int neighbour : neighbours) {
				transpose.addEdge(neighbour, v);
			}
		}

		return transpose;
	}
}
