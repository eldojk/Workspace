package workspace.ws.ds.data;

public class DiGraph extends Graph {

	public void addEdge(int fromVertex, int toVertex) {
		adjacencyList.get(fromVertex).add(toVertex);
	}

}
