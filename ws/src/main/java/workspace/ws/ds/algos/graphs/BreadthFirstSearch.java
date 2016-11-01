package workspace.ws.ds.algos.graphs;

import java.util.HashSet;
import java.util.Set;

import workspace.ws.ds.data.Graph;
import workspace.ws.ds.data.Queue;

public class BreadthFirstSearch {
	private Graph graph;
	private Set<Integer> visited;
	private Queue queue;  

	private boolean isVisited(int vertex) {
		return visited.contains(vertex);
	}

	private void visit(int vertex) {
		visited.add(vertex);
	}

	public BreadthFirstSearch(Graph graph) {
		this.graph = graph;
		this.visited = new HashSet<Integer>();
		this.queue = new Queue();
	}

	public void breadthFirstSearch(int source) {
		queue.push(source);
		
		while (!queue.isEmpty()) {
			int vertex = (Integer) queue.pop();
			
			if (!isVisited(vertex)) {
				visit(vertex);
				
				for (int nieghbour : graph.adj(vertex)) {
					queue.push(nieghbour);
				}
			}
		}
	}

	public Set<Integer> getVisitedVertices() {
		return visited;
	}
}
