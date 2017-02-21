package workspace.ws.ds.data;

import java.util.ArrayList;
import java.util.List;

public class EdgeWeightedGraph {
	private int V;
	private List<List<Edge>> adj;
	private List<Edge> edges;

	public EdgeWeightedGraph(int vertices) {
		this.V = vertices;
		adj = new ArrayList<List<Edge>>();
		for (int i = 0; i < vertices; i++)
			adj.add(new ArrayList<Edge>());
		edges = new ArrayList<Edge>();
	}

	public void addEdge(Edge edge) {
		int v = edge.either();
		int w = edge.other(v);

		adj.get(v).add(edge);
		adj.get(w).add(edge);
		
		edges.add(edge);
	}

	public int V() {
		return V;
	}
	
	public int E() {
		return edges.size();
	}
	
	public List<Edge> edges() {
		return edges;
	}

	public List<Edge> adj(int vertex) {
		return adj.get(vertex);
	}
}
