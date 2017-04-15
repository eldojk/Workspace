package workspace.ws.ds.algos.arrays;

import junit.framework.TestCase;

public class KthSmallestElementSortedMatrixTest extends TestCase{
	private KthSmallestElementSortedMatrix util;
	private int[][] matrix;
	
	public void setUp() {
		matrix = new int[][] {
				new int[] {10, 20, 30, 40},
				new int[] {15, 25, 35, 45},
				new int[] {24, 29, 37, 48},
				new int[] {32, 33, 39, 50}
		};
	}
	
	public void testKthSmallestElementOne() {
		util = new KthSmallestElementSortedMatrix(matrix, 3);
		assertEquals(20, util.kthSmallest());
	}
	
	public void testKthSmallestElementTwo() {
		util = new KthSmallestElementSortedMatrix(matrix, 7);
		assertEquals(30, util.kthSmallest());
	}
	
	public void testKthSmallestElementThree() {
		util = new KthSmallestElementSortedMatrix(matrix, 15);
		assertEquals(48, util.kthSmallest());
	}
}
