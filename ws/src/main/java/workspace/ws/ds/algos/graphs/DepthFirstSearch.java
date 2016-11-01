package workspace.ws.ds.algos.graphs;

import java.util.HashSet;
import java.util.Set;

import workspace.ws.ds.data.Graph;

public class DepthFirstSearch {
	private Graph graph;
	private Set<Integer> visited;

	private boolean isVisited(int vertex) {
		return visited.contains(vertex);
	}

	private void visit(int vertex) {
		visited.add(vertex);
	}

	public DepthFirstSearch(Graph graph) {
		this.graph = graph;
		this.visited = new HashSet<Integer>();
	}

	public void depthFirstSearch(int source) {
		for (int nieghbour : graph.adj(source)) {
			if (!isVisited(nieghbour)) {
				visit(nieghbour);
				depthFirstSearch(nieghbour);
			}
		}
	}

	public Set<Integer> getVisitedVertices() {
		return visited;
	}
}
