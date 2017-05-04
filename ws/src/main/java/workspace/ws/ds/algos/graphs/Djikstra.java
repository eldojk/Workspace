package workspace.ws.ds.algos.graphs;

import workspace.ws.ds.data.DirectedEdge;
import workspace.ws.ds.data.DjikstraMinPQ;
import workspace.ws.ds.data.EdgeWeightedDiGraph;

public class Djikstra {
	
	private DirectedEdge[] edgeTo;
	private int[] distTo;
	private DjikstraMinPQ pq;
	
	public Djikstra(EdgeWeightedDiGraph graph, int source) {
		edgeTo = new DirectedEdge[graph.V()];
		distTo = new int[graph.V()];
		pq = new DjikstraMinPQ(graph.V());
		
		for (int v = 0; v < graph.V(); v++)
			distTo[v] = Integer.MAX_VALUE;
		
		distTo[source] = 0;
		
		pq.insert(source, 0);
		
		while(!pq.isEmpty()) {
			int v = pq.deleteMin();
			
			for (DirectedEdge edge : graph.adj(v)) {
				relax(edge);
			}
		}
	}

	private void relax(DirectedEdge edge) {
		int v = edge.from();
		int w = edge.to();
		
		if (distTo[w] > distTo[v] + edge.getWeight()) {
			distTo[w] = distTo[v] + (int) edge.getWeight();
			edgeTo[w] = edge;
			
			if (pq.contains(w)) {
				pq.decreaseKey(w, distTo[w]);
			}
			else {
				pq.insert(w, distTo[w]);
			}
		}
	}
	
	public int[] getDistances() {
		return distTo;
	}
	
	public DirectedEdge[] getEgdeTo() {
		return edgeTo;
	}
}
