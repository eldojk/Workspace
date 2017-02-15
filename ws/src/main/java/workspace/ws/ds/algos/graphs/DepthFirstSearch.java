package workspace.ws.ds.algos.graphs;

import workspace.ws.ds.data.Graph;
import workspace.ws.ds.data.Stack;

/**
 * This algorithm works correctly for digraphs as well
 * without any modification
 * 
 * @author eldo.joseph
 */
public class DepthFirstSearch {
	protected Graph graph;
	protected boolean[] visited;
	private int[] edgeTo;
	private int source;

	private boolean isVisited(int vertex) {
		return visited[vertex];
	}

	protected void visit(int vertex) {
		visited[vertex] = true;
	}

	public DepthFirstSearch(Graph graph) {
		this.graph = graph;
		this.visited = new boolean[graph.V()];
		this.edgeTo = new int[graph.V()];

		for (int i = 0; i < graph.V(); i++)
			edgeTo[i] = -1;
	}

	public void depthFirstSearch(int source) {
		for (int nieghbour : graph.adj(source)) {
			if (!isVisited(nieghbour)) {
				visit(nieghbour);
				edgeTo[nieghbour] = source;
				depthFirstSearch(nieghbour);
			}
		}

		this.source = source;
	}

	public boolean[] getVisitedVertices() {
		return visited;
	}

	public boolean hasPathTo(int vertex) {
		return visited[vertex];
	}

	public Stack getPathTo(int vertex) {
		if (!hasPathTo(vertex)) {
			return null;
		}

		Stack s = new Stack();
		for (int v = vertex; v != source; v = edgeTo[v]) {
			s.push(v);
		}
		s.push(source);

		return s;
	}
}
