package workspace.ws.ds.data;

public class DiGraph extends Graph {
	
	public DiGraph(int vertices) {
		super(vertices);
	}

	public void addEdge(int fromVertex, int toVertex) {
		adjacencyList.get(fromVertex).add(toVertex);
	}

}
