package workspace.ws.ds.algos.graphs;

import workspace.ws.ds.data.Graph;

public class IsPathExists extends DepthFirstSearch {

	private int destination;
	private boolean isDestinationFound;

	public IsPathExists(Graph graph) {
		super(graph);
	}

	protected void visit(int vertex) {
		super.visit(vertex);

		if (vertex == destination) {
			isDestinationFound = true;
		}
	}
	
	private void setDestination(int destination) {
		isDestinationFound = false;
		this.destination = destination;
	}

	public boolean doesPathExist(int source, int destination) {
		setDestination(destination);
		depthFirstSearch(source);

		return isDestinationFound;
	}

}
