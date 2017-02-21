package workspace.ws.ds.data;

public class Edge implements Comparable<Edge> {
	private int v, w;
	private double weight;

	public Edge(int v, int w, double weight) {
		this.v = v;
		this.w = w;
		this.weight = weight;
	}

	public int either() {
		return v;
	}

	public int other(int vertex) {
		if (vertex == v) {
			return w;
		}

		return v;
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
	public int compareTo(Edge o) {
		if (this.weight < o.getWeight()) {
			return -1;
		} else if (this.weight > o.getWeight()) {
			return 1;
		} else {
			return 0;
		}
	}
}
