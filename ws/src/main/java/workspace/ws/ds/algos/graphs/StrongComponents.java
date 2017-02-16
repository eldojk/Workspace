package workspace.ws.ds.algos.graphs;

import workspace.ws.ds.data.DiGraph;

public class StrongComponents extends TopologicalSort {
	private DiGraph transpose;
	private int components;

	public StrongComponents(DiGraph digraph) {
		super(digraph);
	}

	private void unvisitAllVertices() {
		for (int i = 0; i < digraph.V(); i++)
			visited[i] = false;
	}

	private void transposeGraph() {
		transpose = new DiGraph(this.digraph.V());

		for (int vertex = 0; vertex < digraph.V(); vertex++) {
			for (int neighbour : digraph.adj(vertex)) {
				transpose.addEdge(neighbour, vertex);
			}
		}
	}

	private void dfsVisit(int source) {
		visited[source] = true;

		for (int neighbour : transpose.adj(source)) {
			if (!visited[neighbour]) {
				dfsVisit(neighbour);
			}
		}
	}

	private void dfsFinal() {
		while (!topology.isEmpty()) {
			int vertex = (int) topology.pop();

			if (!visited[vertex]) {
				dfsVisit(vertex);
				components++;
			}
		}
	}

	public int computeStronglyConnectedComponents() {
		unvisitAllVertices();
		transposeGraph();
		dfsFinal();

		return components;
	}
}
