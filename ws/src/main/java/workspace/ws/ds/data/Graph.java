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
	private Set<Integer> vertices;
	private HashMap<Integer, Set<Integer>> adjacencyList;

	public Graph() {
		this.vertices = new HashSet<Integer>();
		this.adjacencyList = new HashMap<Integer, Set<Integer>>();
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
