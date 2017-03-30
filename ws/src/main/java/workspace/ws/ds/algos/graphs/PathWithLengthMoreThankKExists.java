package workspace.ws.ds.algos.graphs;

import workspace.ws.ds.data.Edge;
import workspace.ws.ds.data.EdgeWeightedGraph;

/**
 * http://www.geeksforgeeks.org/find-if-there-is-a-path-of-more-than-k-length-from-a-source/
 * 
 * We start from given source, explore all paths from current vertex. We keep track of current distance
 * from source. If distance becomes more than k, we return true. If a path doesn’t produces more than k
 * distance, we backtrack.
 * How do we make sure that the path is simple and we don’t loop in a cycle? The idea is to keep track 
 * of current path vertices in an array. Whenever we add a vertex to path, we check if it already 
 * exists or not in current path. If it exists, we ignore the edge.
 * 
 * @author eldo.joseph
 */
public class PathWithLengthMoreThankKExists {
	private EdgeWeightedGraph graph;
	private int k;
	
	public PathWithLengthMoreThankKExists(EdgeWeightedGraph graph, int k) {
		this.graph = graph;
		this.k = k;
	}
	
	public boolean exists() {
		boolean[] path = new boolean[graph.V()];
		path[0] = true;
		
		return exists(0, this.k, path);
	}
	
	private boolean exists(int src, int k, boolean[] path) {
		if (k <= 0)
			return true;
		
		for (Edge edge : graph.adj(src)) {
			int v = edge.other(src);
			
			if (path[v])
				continue;
			
			if (edge.getWeight() >= k)
				return true;
			
			path[v] = true;
			
			if (exists(v, (int) (k - edge.getWeight()), path))
				return true;
			
			path[v] = false;
		}
		
		return false;
	}
}
