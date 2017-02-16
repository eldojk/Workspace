package workspace.ws.ds.algos.graphs;

import workspace.ws.ds.data.Graph;

public class ConnectedComponents {
	protected Graph graph;
	protected boolean[] visited;
	private int[] componentId;
	private int component;

	private boolean isVisited(int vertex) {
		return visited[vertex];
	}

	protected void visit(int vertex) {
		visited[vertex] = true;
	}

	public ConnectedComponents(Graph graph) {
		this.graph = graph;
		this.visited = new boolean[graph.V()];
		componentId = new int[graph.V()];

		for (int i = 0; i < componentId.length; i++)
			componentId[i] = i;

		preProcess();
	}

	private void depthFirstSearch(int source) {
		visit(source);
		componentId[source] = component;

		for (int nieghbour : graph.adj(source)) {
			if (!isVisited(nieghbour)) {
				depthFirstSearch(nieghbour);
			}
		}
	}

	private void preProcess() {
		for (int v = 0; v < graph.V(); v++) {

			if (!isVisited(v)) {
				depthFirstSearch(v);
				component++;
			}
		}
	}

	public int getNumberOfComponents() {
		return component;
	}

	public int getComponentId(int vertex) {
		return componentId[vertex];
	}

	public boolean isConnected(int vertex1, int vertex2) {
		return componentId[vertex1] == componentId[vertex2];
	}
}
