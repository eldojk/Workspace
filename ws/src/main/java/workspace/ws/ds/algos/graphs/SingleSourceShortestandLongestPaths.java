package workspace.ws.ds.algos.graphs;

import workspace.ws.ds.data.DirectedEdge;
import workspace.ws.ds.data.EdgeWeightedDiGraph;
import workspace.ws.ds.data.Stack;

/**
 * amzn, smsg
 * 
 * http://www.geeksforgeeks.org/find-longest-path-directed-acyclic-graph/
 * http://www.geeksforgeeks.org/shortest-path-for-directed-acyclic-graphs/
 * 
 * @author eldo.joseph
 */
public class SingleSourceShortestandLongestPaths {
	private EdgeWeightedDiGraph digraph;
	TopologicalSortOnEdgeListGraph topologyUtil;

	public SingleSourceShortestandLongestPaths(EdgeWeightedDiGraph digraph) {
		this.digraph = digraph;
	}

	public int[] getShortestPath(int source) {
		topologyUtil = new TopologicalSortOnEdgeListGraph(digraph);
		Stack topology = topologyUtil.getTopologicalSortedOrder();
		int[] dist = new int[digraph.V()];

		for (int i = 0; i < dist.length; i++)
			dist[i] = Integer.MAX_VALUE;

		dist[source] = 0;

		// Consider vertices in topological order and relax every edge
		while (!topology.isEmpty()) {
			int vertex = (int) topology.pop();

			for (DirectedEdge edge : digraph.adj(vertex)) {
				int neighbour = edge.to();

				if (dist[neighbour] > dist[vertex] + edge.getWeight()) {
					dist[neighbour] = (int) (dist[vertex] + edge.getWeight());
				}
			}
		}

		return dist;
	}

	public int[] getLongestPath(int source) {
		topologyUtil = new TopologicalSortOnEdgeListGraph(digraph);
		Stack topology = topologyUtil.getTopologicalSortedOrder();
		int[] dist = new int[digraph.V()];

		for (int i = 0; i < dist.length; i++)
			dist[i] = Integer.MIN_VALUE;

		dist[source] = 0;

		while (!topology.isEmpty()) {
			int vertex = (int) topology.pop();

			for (DirectedEdge edge : digraph.adj(vertex)) {
				int neighbour = edge.to();

				if (dist[neighbour] < dist[vertex] + edge.getWeight()) {
					dist[neighbour] = (int) (dist[vertex] + edge.getWeight());
				}
			}
		}

		return dist;
	}
}
