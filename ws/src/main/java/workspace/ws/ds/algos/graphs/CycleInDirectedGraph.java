package workspace.ws.ds.algos.graphs;

import workspace.ws.ds.data.DiGraph;

/**
 * smsg, amzn
 * 
 * https://www.youtube.com/watch?v=rKQaZuoUR4M tushar roy
 * 
 * @author eldo.joseph
 */
public class CycleInDirectedGraph {
	private DiGraph graph;
	private boolean cycleFound;

	public CycleInDirectedGraph(DiGraph graph) {
		this.graph = graph;
	}

	public boolean isCyclePresent() {
		boolean[] greySet = new boolean[graph.V()]; // visiting
		boolean[] blackSet = new boolean[graph.V()]; // visited

		for (int i = 0; i < graph.V(); i++) {
			if (!blackSet[i]) {
				dfs(i, greySet, blackSet);
			}
		}

		return cycleFound;
	}

	private void dfs(int source, boolean[] greySet, boolean[] blackSet) {
		greySet[source] = true;

		for (int neighbour : graph.adj(source)) {

			if (greySet[neighbour]) {
				cycleFound = true;
				break;
			}

			dfs(neighbour, greySet, blackSet);
		}

		greySet[source] = false;
		blackSet[source] = true;
	}
}
