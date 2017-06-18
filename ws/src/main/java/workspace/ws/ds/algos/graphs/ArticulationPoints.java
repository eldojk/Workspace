package workspace.ws.ds.algos.graphs;

import java.util.ArrayList;
import java.util.List;

import workspace.ws.ds.data.Graph;

/**
 * amzn
 * 
 * http://www.geeksforgeeks.org/articulation-points-or-cut-vertices-in-a-graph/
 * 
 * @author eldo.joseph
 */
public class ArticulationPoints {
	private Graph graph;
	private static final int NIL = -1;
	private int time = 0;
	List<Integer> articulationPoints = new ArrayList<Integer>();

	private void populateArticulationPoints(int u, boolean visited[],
			int disc[], int low[], int parent[], boolean ap[]) {

		int children = 0;
		visited[u] = true;
		disc[u] = ++time;
		low[u] = disc[u];

		for (int v : this.graph.adj(u)) {

			if (!visited[v]) {
				children++;
				parent[v] = u;
				populateArticulationPoints(v, visited, disc, low, parent, ap);

				low[u] = Math.min(low[u], low[v]);

				// (1) u is root of DFS tree and has two or more children.
				if (parent[u] == NIL && children > 1)
					ap[u] = true;

				// (2) If u is not root and low value of one of its child
				// is more than discovery value of u.
				if (parent[u] != NIL && low[v] >= disc[u])
					ap[u] = true;
				
			} else if (v != parent[u]) {
				
				low[u] = Math.min(low[u], disc[v]);
			}
		}
	}

	public ArticulationPoints(Graph graph) {
		this.graph = graph;
		boolean visited[] = new boolean[graph.V()];
		int disc[] = new int[graph.V()];
		int low[] = new int[graph.V()];
		int parent[] = new int[graph.V()];
		boolean ap[] = new boolean[graph.V()];

		for (int i = 0; i < graph.V(); i++) {
			parent[i] = NIL;
			visited[i] = false;
			ap[i] = false;
		}

		for (int i = 0; i < graph.V(); i++)
			if (visited[i] == false)
				populateArticulationPoints(i, visited, disc, low, parent, ap);

		for (int i = 0; i < graph.V(); i++)
			if (ap[i] == true)
				articulationPoints.add(i);
	}

	public List<Integer> getArticulationPoints() {
		return articulationPoints;
	}
}
