package workspace.ws.ds.data;

import java.util.ArrayList;
import java.util.List;

public class EdgeWeightedGraph {
	private int V;
	private List<Edge>[] adj;
	private List<Edge> edges;

	@SuppressWarnings("unchecked")
	public EdgeWeightedGraph(int vertices) {
		this.V = vertices;
		adj = (List<Edge>[]) new ArrayList[vertices];
		edges = new ArrayList<Edge>();
	}

	public void addEdge(Edge edge) {
		int v = edge.either();
		int w = edge.other(v);

		adj[v].add(edge);
		adj[w].add(edge);
		
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
		return adj[vertex];
	}
}
