package workspace.ws.ds.algos.arrays;

import workspace.ws.ds.algos.heaps.MinPriorityQueue;

class Node implements Comparable<Node> {
	public int value;
	public int i;
	public int j;

	@Override
	public int compareTo(Node other) {
		if (this.value > other.value)
			return 1;
		else if (this.value < other.value)
			return -1;
		else
			return 0;
	}
	
}

public class KthSmallestElementSortedMatrix {
	private MinPriorityQueue<Node> pq;
	private int[][] matrix;
	private int k;
	private int smallestElement;
	
	public KthSmallestElementSortedMatrix(int[][] matrix, int k) {
		this.matrix = matrix;
		this.k = k;
		pq = new MinPriorityQueue<Node>(matrix.length);
	}
	
	public int kthSmallest() {
		
		// Add first elements of each row
		for (int i = 0; i < matrix.length; i++) {
			Node node = new Node();
			node.value = matrix[i][0];
			node.i = i;
			node.j = 0;
			pq.insert(node);
		}
		
		int rowLength = matrix[0].length;
		
		while (k > 0) {
			// keep deleting till k becomes 0
			Node deletedNode = pq.deleteTop();
			smallestElement = deletedNode.value;
			
			// Insert from the row where the node was deleted
			// If no elements remain in that row, ignore it
			if (deletedNode.j < rowLength - 1) {
				int newI = deletedNode.i;
				int newJ = deletedNode.j + 1;
				
				Node newNode = new Node();
				newNode.value = matrix[newI][newJ];
				newNode.i = newI;
				newNode.j = newJ;
				pq.insert(newNode);
			}
			
			k -= 1;
		}
		
		return smallestElement;
	}
}
