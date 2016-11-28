package workspace.ws.ds.algos.heaps;

/**
 * Implementation of a binary Heap
 * 
 * @author eldo.joseph
 *
 */
public class Heap {
	private HeapType heapType;
	private int size;
	private int[] heap;
	private int count;

	public Heap(HeapType heapType, int size) {
		this.heapType = heapType;
		this.size = size;
		this.heap = new int[size + 1];
		this.count = 0;
	}

	/**
	 * Swap elements at indices in the heap
	 * 
	 * @param element1
	 * @param element2
	 */
	private void swap(int element1, int element2) {
		int temp = heap[element1];
		heap[element1] = heap[element2];
		heap[element2] = temp;
	}

	/**
	 * Get parent of and index
	 * 
	 * @param index
	 * @return
	 */
	private int getParent(int index) {
		return (int) Math.floor(index);
	}

	/**
	 * Get eligible child for swapping
	 * 
	 * @param index
	 * @return
	 */
	private int getChild(int index) {
		int leftChild = 2 * index;
		int rightChild = leftChild + 1;

		if (leftChild > count) {

			return 0;
		} else if ((leftChild <= count) && (rightChild > count)) {

			if ((heapType.equals(HeapType.MAXHEAP))
					&& (heap[index] < heap[leftChild])) {

				return leftChild;
			} else if ((heapType.equals(HeapType.MINHEAP))
					&& (heap[index] > heap[leftChild])) {

				return leftChild;
			}

			return 0;

		} else {

			int min = leftChild;
			int max = rightChild;

			if (leftChild > rightChild) {
				min = rightChild;
				max = rightChild;
			}

			if (heapType.equals(HeapType.MAXHEAP)) {
				return max;
			}

			return min;
		}
	}

	/**
	 * Checks if heap property is satisfied for two indices
	 * 
	 * @param parent
	 * @param child
	 * @return
	 */
	private boolean isHeapSatisfied(int parent, int child) {
		if (heapType.equals(HeapType.MAXHEAP)) {
			return (parent >= child);
		}

		return (parent <= child);
	}

	/**
	 * Add an element to heap
	 * 
	 * @param element
	 * @throws HeapException
	 */
	public void add(int element) throws HeapException {
		if (count >= size) {
			throw new HeapException("Overflow");
		}

		// Swimming
		++count;
		heap[count] = element;
		int index = count;

		while (index > 1) {
			int parent = getParent(index);

			if (!isHeapSatisfied(heap[parent], heap[index])) {
				swap(parent, index);
			}

			index = parent;
		}
	}

	/**
	 * Remove heap top element
	 * 
	 * @return
	 * @throws HeapException
	 */
	public int deleteTop() throws HeapException {
		if (count <= 0) {
			throw new HeapException("Underflow");
		}

		int index = 1;
		swap(index, count);
		int top = heap[count];
		heap[count] = 0;
		--count;

		// Sinking
		while (index <= count) {
			int child = getChild(index);

			if (child != 0) {
				swap(index, child);
				index = child;
				continue;
			}

			break;
		}

		return top;
	}
}
