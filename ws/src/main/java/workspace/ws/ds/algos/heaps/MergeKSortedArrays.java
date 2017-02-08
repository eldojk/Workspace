package workspace.ws.ds.algos.heaps;

/**
 * http://www.geeksforgeeks.org/merge-k-sorted-arrays/
 * 
 * @author eldo.joseph
 */
public class MergeKSortedArrays {
	private MinPriorityQueue<Element> mpq;
	private int[][] array;
	private int n;
	private int k;
	private int nextArray;
	private int[] currentIndices;

	private class Element implements Comparable<Element> {
		public int data;
		public int array;

		public Element(int data, int array) {
			this.data = data;
			this.array = array;
		}

		@Override
		public int compareTo(Element o) {
			if (this.data < o.data)
				return -1;
			else if (this.data > o.data)
				return 1;
			else
				return 0;
		}

	}

	public MergeKSortedArrays(int[][] array, int n, int k) {
		this.array = array;
		this.n = n;
		this.k = k;
		this.mpq = new MinPriorityQueue<Element>(k);
		this.nextArray = 0;
		this.currentIndices = new int[k];
	}

	private void insertNext() {
		if (currentIndices[nextArray] == n) {
			mpq.insert(new Element(Integer.MAX_VALUE, nextArray));
			return;
		}
		
		mpq.insert(new Element(array[nextArray][currentIndices[nextArray]], nextArray));
		currentIndices[nextArray]++;
	}

	public int[] getSortedArray() {
		for (int i = 0; i < k; i++) {
			mpq.insert(new Element(array[i][0], i));
			currentIndices[i]++;
		}
		
		int[] sortedArray = new int[n * k];

		for (int i = 0; i < n; i++) {
			for (int m = 0; m < k; m++) {
				Element el = mpq.deleteTop();
				sortedArray[m + i * k] = el.data;
				nextArray = el.array;
				
				insertNext();
			}
		}

		return sortedArray;
	}
}
