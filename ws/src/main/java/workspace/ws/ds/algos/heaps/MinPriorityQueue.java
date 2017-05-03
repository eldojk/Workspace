package workspace.ws.ds.algos.heaps;

public class MinPriorityQueue<Key extends Comparable<Key>> extends
		MaxPriorityQueue<Key> {

	public MinPriorityQueue(int capacity) {
		super(capacity);
	}

	protected boolean less(int i, int j) {
		if ((j >= pq.length) || (pq[j] == null)) {
			return false;
		}

		// is i > j
		return pq[i].compareTo(pq[j]) > 0;
	}
	
	

}
