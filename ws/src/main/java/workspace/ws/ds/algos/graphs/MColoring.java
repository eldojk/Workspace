package workspace.ws.ds.algos.graphs;

import workspace.ws.ds.data.Graph;

/**
 * http://www.geeksforgeeks.org/backttracking-set-5-m-coloring-problem/
 * 
 * @author eldo.joseph
 */
public class MColoring {
	private int[] color;
	private int m;
	private Graph graph;
	
	public MColoring(Graph graph, int m) {
		this.graph = graph;
		this.m = m;
		this.color = new int[graph.V()];
	}
	
	public boolean isColorable() {
		return isColorable(0);
	}

	private boolean isColorable(int v) {
		if (v == graph.V())
			return true;
		
		for (int c = 1; c <=m; c++) {
			
			if (isSafe(v, c)) {
				color[v] = c;
				
				if (isColorable(v + 1))
					return true;
				
				color[v] = 0;
			}
		}
		
		return false;
	}

	private boolean isSafe(int vertex, int c) {
		for(int neighbour : graph.adj(vertex)) {
			if (color[neighbour] == c) {
				return false;
			}
		}
		
		return true;
	}
}
