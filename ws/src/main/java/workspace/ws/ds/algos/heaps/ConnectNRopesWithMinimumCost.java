package workspace.ws.ds.algos.heaps;

/**
 * http://www.geeksforgeeks.org/connect-n-ropes-minimum-cost/
 * 
 * @author eldo.joseph
 */
public class ConnectNRopesWithMinimumCost {
	private MinPriorityQueue<Integer> mpq;
	private int[] array;
	
	public ConnectNRopesWithMinimumCost(int[] array, int n) {
		mpq = new MinPriorityQueue<Integer>(n);
		this.array = array;
	}
	
	public int getMinCost() {
		int totalCost = 0;
		for (int element : array)
			mpq.insert(element);
		
		while (mpq.getSize() >= 2) {
			int element1 = mpq.deleteTop();
			int element2 = mpq.deleteTop();
			int combinedElement = element1 + element2;
			
			totalCost += combinedElement;
			
			mpq.insert(combinedElement);
		}
		
		return totalCost;
	}
	
	public static void main(String[] args) {
		int[] arr = new int[] {4, 3, 2, 6};
		ConnectNRopesWithMinimumCost c = new ConnectNRopesWithMinimumCost(arr, 4);
		System.out.println(c.getMinCost());
	}
}
