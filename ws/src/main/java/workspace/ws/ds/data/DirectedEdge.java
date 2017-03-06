package workspace.ws.ds.data;

public class DirectedEdge implements Comparable<DirectedEdge> {
	private int v, w;
	private double weight;
	
	public DirectedEdge(int v, int w) {
		this.v = v;
		this.w = w;
		this.weight = 0;
	}

	public DirectedEdge(int v, int w, double weight) {
		this.v = v;
		this.w = w;
		this.weight = weight;
	}

	public int from() {
		return v;
	}

	public int to() {
		return w;
	}

	public double getWeight() {
		return weight;
	}

	@Override
	public int compareTo(DirectedEdge o) {
		if (this.weight < o.getWeight()) {
			return -1;
		} else if (this.weight > o.getWeight()) {
			return 1;
		} else {
			return 0;
		}
	}
}
