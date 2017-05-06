package workspace.ws.ds.data;

import java.util.HashMap;
import java.util.Map;

import workspace.ws.ds.algos.heaps.MinPriorityQueue;

class DjikstraNode implements Comparable<DjikstraNode> {
	public int priority;
	public int vertex;

	@Override
	public int compareTo(DjikstraNode o) {
		if (this.priority > o.priority)
			return 1;
		else if (this.priority < o.priority)
			return -1;
		else
			return 0;
	}
}

public class DjikstraMinPQ extends MinPriorityQueue<DjikstraNode> {

	private Map<Integer, Integer> indexMap;

	public DjikstraMinPQ(int capacity) {
		super(capacity);
		indexMap = new HashMap<Integer, Integer>();

		for (int i = 0; i <= capacity; i++) {
			indexMap.put(i, -1);
		}
	}

	@Override
	protected void exchange(int i, int j) {
		DjikstraNode nodeI = (DjikstraNode) pq[i];
		DjikstraNode nodeJ = (DjikstraNode) pq[j];

		pq[i] = pq[j];
		pq[j] = nodeI;

		indexMap.put(nodeI.vertex, j);
		indexMap.put(nodeJ.vertex, i);
	}

	public void decreaseKey(int vertex, int newPriority) {
		int qIndex = indexMap.get(vertex);
		DjikstraNode node = pq[qIndex];
		node.priority = newPriority;
		swim(qIndex);
	}

	public boolean contains(int vertex) {
		return indexMap.get(vertex) != -1;
	}

	@Override
	public void insert(DjikstraNode node) {
		indexMap.put(node.vertex, N + 1);
		super.insert(node);
	}
	
	public void insert(int vertex, int priority) {
		DjikstraNode node = new DjikstraNode();
		node.vertex = vertex;
		node.priority = priority;
		insert(node);
	}

	@Override
	public DjikstraNode deleteTop() {
		DjikstraNode top = super.deleteTop();
		indexMap.put(top.vertex, -1);

		return top;
	}
	
	public int deleteMin() {
		return deleteTop().vertex;
	}
}
