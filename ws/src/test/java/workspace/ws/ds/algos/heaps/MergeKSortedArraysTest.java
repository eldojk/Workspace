package workspace.ws.ds.algos.heaps;

import junit.framework.TestCase;
import static org.junit.Assert.*;

public class MergeKSortedArraysTest extends TestCase {
	private MergeKSortedArrays merger;

	protected void setUp() {
		int arr[][] = { {1, 3, 5, 7},
	            		{2, 4, 6, 8},
	            		{0, 9, 10, 11} };
		merger = new MergeKSortedArrays(arr, 4, 3);
	}

	public void testMergeKSortedArrays() {
		int[] expected = new int[] {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11};
		int[] actual = merger.getSortedArray();
 		assertArrayEquals(expected, actual);
	}
}
