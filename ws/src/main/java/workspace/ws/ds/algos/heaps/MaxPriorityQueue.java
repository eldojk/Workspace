package workspace.ws.ds.algos.heaps;

public class MaxPriorityQueue<Key extends Comparable<Key>> {
	protected Key[] pq;
	protected int N;

	@SuppressWarnings("unchecked")
	public MaxPriorityQueue(int capacity) {
		pq = (Key[]) new Comparable[capacity + 1];
	}

	protected boolean less(int i, int j) {
		if ((j >= pq.length) || (pq[j] == null)) {
			return false;
		}

		// is i < j
		return pq[i].compareTo(pq[j]) < 0;
	}

	protected void exchange(int i, int j) {
		Key temp = pq[i];
		pq[i] = pq[j];
		pq[j] = temp;
	}

	public void swim(int k) {
		while (k > 1) {
			int parent = k / 2;
			if (less(parent, k)) {
				exchange(parent, k);
			}
			
			k = parent;
		}
	}

	public void sink(int k) {
		while (2 * k <= N) {
			int child = 2 * k;

			if (less(child, child + 1)) {
				child += 1;
			}

			if (!less(k, child)) {
				break;
			}

			exchange(k, child);
			k = child;
		}
	}

	public boolean isEmpty() {
		return N == 0;
	}
	
	public int getSize() {
		return N;
	}

	public void insert(Key key) {
		N++;
		pq[N] = key;
		swim(N);
	}

	public Key deleteTop() {
		Key max = pq[1];
		exchange(1, N);
		N--;
		pq[N + 1] = null;
		sink(1);
		return max;

	}
}
