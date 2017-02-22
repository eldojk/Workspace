package workspace.ws.ds.algos.graphs;

import workspace.ws.ds.algos.unionfind.QuickFind;
import workspace.ws.ds.algos.unionfind.UnionFind;
import workspace.ws.ds.data.Edge;
import workspace.ws.ds.data.EdgeWeightedGraph;

public class CycleInUndirectedGraph {
	private EdgeWeightedGraph graph;
	private UnionFind uf;

	public CycleInUndirectedGraph(EdgeWeightedGraph graph) {
		this.graph = graph;
	}

	public boolean detectCycle() {
		uf = new QuickFind(graph.V());
		for (Edge edge : graph.edges()) {
			int v = edge.from();
			int w = edge.to();

			if (uf.isConnected(v, w)) {
				return true;
			}

			uf.union(v, w);
		}

		return false;
	}

}
