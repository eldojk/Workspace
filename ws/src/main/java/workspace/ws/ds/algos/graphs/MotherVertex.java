package workspace.ws.ds.algos.graphs;

import workspace.ws.ds.data.DiGraph;

/**
 * http://www.geeksforgeeks.org/find-a-mother-vertex-in-a-graph/
 * 
 * @author eldo.joseph
 */
public class MotherVertex {
	private DiGraph graph;
	private boolean[] visited;
	
	public MotherVertex(DiGraph graph) {
		this.graph = graph;
		visited = new boolean[graph.V()];
	}
	
	private void dfs(int source) {
		for (int neighbour : graph.adj(source)) {
			dfs(neighbour);
		}
		
		visited[source] = true;
	}
	
	public int getMotherVertex() {
		int v = 0;
		
		for (int i = 0; i < graph.V(); i++) {
			if (!visited[i]) {
				dfs(i);
				v = i;
			}
		}
		
		visited = new boolean[graph.V()];
		
		dfs(v);
		
		for (boolean val : visited) {
			if (!val)
				return -1;
		}
		
		return v;
	}
}
