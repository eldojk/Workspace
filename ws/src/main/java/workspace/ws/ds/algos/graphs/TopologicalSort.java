package workspace.ws.ds.algos.graphs;

import workspace.ws.ds.data.DiGraph;
import workspace.ws.ds.data.Stack;

/**
 * Idea is to use DFS and once a vertex is processed move it to a stack. The
 * final stack will give the topological order. Just pop until its empty, and
 * the order in which the elements come out is the topological order
 * 
 * @author eldo.joseph
 *
 */
public class TopologicalSort {
	protected DiGraph digraph;
	protected boolean[] visited;
	protected Stack topology;

	public TopologicalSort(DiGraph digraph) {
		this.digraph = digraph;
		topology = new Stack();
		visited = new boolean[digraph.V()];
		preProcess();
	}

	protected void preProcess() {
		for (int v = 0; v < digraph.V(); v++) {
			if (!visited[v]) {
				dfs(v);
			}
		}
	}

	protected void dfs(int source) {
		visited[source] = true;
		
		for (int neighbour : digraph.adj(source)) {
			if (!visited[neighbour]) {
				dfs(neighbour);
			}
		}

		topology.push(source);
	}

	protected Stack getTopologicalSortedOrder() {
		return topology;
	}
}
