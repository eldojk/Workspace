package workspace.ws.ds.data;

import java.util.ArrayList;
import java.util.List;

public class EdgeWeightedDiGraph {
	private int V;
	private List<DirectedEdge>[] adj;
	private List<DirectedEdge> edges;

	@SuppressWarnings("unchecked")
	public EdgeWeightedDiGraph(int vertices) {
		this.V = vertices;
		adj = (List<DirectedEdge>[]) new ArrayList[vertices];
		edges = new ArrayList<DirectedEdge>();
	}

	public void addEdge(DirectedEdge edge) {
		int v = edge.from();

		adj[v].add(edge);

		edges.add(edge);
	}

	public int V() {
		return V;
	}

	public int E() {
		return edges.size();
	}

	public List<DirectedEdge> edges() {
		return edges;
	}

	public List<DirectedEdge> adj(int vertex) {
		return adj[vertex];
	}
}
