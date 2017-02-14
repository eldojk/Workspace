package workspace.ws.ds.data;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Set;

/**
 * Undirected Graph
 * 
 * @author eldo.joseph
 *
 */
public class Graph {
	protected Set<Integer> vertices;
	protected HashMap<Integer, Set<Integer>> adjacencyList;
	protected int V;
	protected int E;

	public Graph() {
		this.vertices = new HashSet<Integer>();
		this.adjacencyList = new HashMap<Integer, Set<Integer>>();
	}

	public Graph(int v) {
		this.vertices = new HashSet<Integer>();
		this.adjacencyList = new HashMap<Integer, Set<Integer>>();
		initializeVertices(v);
	}

	/**
	 * Initialize the number of vertices
	 * 
	 * @param numVertices
	 */
	public void initializeVertices(int numVertices) {
		for (int i = 0; i < numVertices; i++) {
			vertices.add(i);
			adjacencyList.put(i, new HashSet<Integer>());
		}

		V = numVertices;
	}

	/**
	 * Returns the set of vertices
	 * 
	 * @return
	 */
	public Set<Integer> getVertices() {
		return vertices;
	}

	/**
	 * Get number of vertices
	 * 
	 * @return
	 */
	public int V() {
		return V;
	}

	/**
	 * Get vertices adjacent to a vertex
	 * 
	 * @param vertex
	 * @return
	 */
	public Set<Integer> adj(int vertex) {
		return adjacencyList.get(vertex);
	}

	/**
	 * Connect to vertices
	 * 
	 * @param fromVertex
	 * @param toVertex
	 */
	public void addEdge(int fromVertex, int toVertex) {
		adjacencyList.get(fromVertex).add(toVertex);
		adjacencyList.get(toVertex).add(fromVertex);
	}
}
