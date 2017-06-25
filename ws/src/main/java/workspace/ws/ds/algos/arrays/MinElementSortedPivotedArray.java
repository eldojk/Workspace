package workspace.ws.ds.algos.arrays;

/**
 * http://www.geeksforgeeks.org/find-minimum-element-in-a-sorted-and-rotated-array/
 * amzn, msft
 * 
 * @author eldo.joseph
 *
 */
public class MinElementSortedPivotedArray {
	
	private int[] array;
	
	public MinElementSortedPivotedArray(int[] array) {
		this.array = array;
	}
	
	private int search(int low, int high) {
		if (high < low)
			return array[0];
		
		if (high == low)
			return array[low];
		
		if (high - low == 1) {
			if (array[low] < array[high])
				return array[low];
			
			return array[high];
		}
		
		int mid = (low + high) / 2;
		
		if (array[mid + 1] < array[mid])
			return array[mid + 1];
		
		if (array[mid] < array[mid - 1])
			return array[mid];
		
		if (array[mid] < array[high])
			return search(low, mid - 1);
		
		return search(mid + 1, high);
	}
	
	public int search() {
		return search(0, array.length - 1);
	}
	
	public static void main(String[] args) {
		MinElementSortedPivotedArray util = new MinElementSortedPivotedArray(new int[] {5, 6, 1, 2, 3, 4});
		System.out.println(util.search());
		
		util = new MinElementSortedPivotedArray(new int[] {1, 2, 3, 4, 5, 6, 7});
		System.out.println(util.search());
		
		util = new MinElementSortedPivotedArray(new int[] {2, 3, 4, 5, 6, 7, 8, 1});
		System.out.println(util.search());
	}
}
