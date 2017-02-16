package workspace.ws.ds.algos.graphs;

import java.util.ArrayList;
import java.util.List;

import workspace.ws.ds.algos.heaps.MinPriorityQueue;
import workspace.ws.ds.algos.unionfind.QuickFind;
import workspace.ws.ds.algos.unionfind.UnionFind;
import workspace.ws.ds.data.Edge;
import workspace.ws.ds.data.EdgeWeightedGraph;

/**
 * We keep adding edges in increasing order of their weights as long as it does
 * not create a cycle
 * 
 * @author eldo.joseph
 */
public class KruskalsMST {
	private List<Edge> mst;

	public KruskalsMST(EdgeWeightedGraph digraph) {
		mst = new ArrayList<Edge>();
		MinPriorityQueue<Edge> minPQ = new MinPriorityQueue<Edge>(digraph.E());

		for (Edge e : digraph.edges()) {
			minPQ.insert(e);
		}

		UnionFind uf = new QuickFind(digraph.V());

		while (!minPQ.isEmpty() && mst.size() < digraph.V() - 1) {
			Edge edge = minPQ.deleteTop();
			int v = edge.either();
			int w = edge.other(v);

			if (!uf.isConnected(v, w)) {
				uf.union(v, w);
				mst.add(edge);
			}
		}
	}

	public List<Edge> minimumSpanningTree() {
		return mst;
	}
}
