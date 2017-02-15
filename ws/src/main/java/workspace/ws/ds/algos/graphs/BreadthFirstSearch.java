package workspace.ws.ds.algos.graphs;

import workspace.ws.ds.data.Graph;
import workspace.ws.ds.data.Queue;

public class BreadthFirstSearch {
	private Graph graph;
	private boolean[] visited;
	private Queue queue;

	private boolean isVisited(int vertex) {
		return visited[vertex];
	}

	protected void visit(int vertex) {
		visited[vertex] = true;
	}

	public BreadthFirstSearch(Graph graph) {
		this.graph = graph;
		this.visited = new boolean[graph.V()];
		this.queue = new Queue();
	}

	public void breadthFirstSearch(int source) {
		queue.push(source);

		while (!queue.isEmpty()) {
			int vertex = (Integer) queue.pop();
			visit(vertex);

			for (int nieghbour : graph.adj(vertex)) {
				if (!isVisited(nieghbour)) {
					queue.push(nieghbour);
				}
			}
		}
	}

	public boolean[] getVisitedVertices() {
		return visited;
	}
}
