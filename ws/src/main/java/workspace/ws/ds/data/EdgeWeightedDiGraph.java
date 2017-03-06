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
		for (int i = 0; i < vertices; i++)
			adj[i] = new ArrayList<DirectedEdge>();
			
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
