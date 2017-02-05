package workspace.ws.ds.algos.heaps;

import junit.framework.TestCase;

//import org.junit.Test;

public class MaxPriorityQueueTest extends TestCase {
	private MaxPriorityQueue<Integer> mpq;
	
	protected void setUp() {
		mpq = new MaxPriorityQueue<Integer>(10);
	}

	public void testMpq() {
		mpq.insert(3);
		mpq.insert(6);
		mpq.insert(2);
		mpq.insert(1);
		
		int max = mpq.deleteMax();
		assertEquals(6, max);
		max = mpq.deleteMax();
		assertEquals(3, max);
		max = mpq.deleteMax();
		assertEquals(2, max);
		max = mpq.deleteMax();
		assertEquals(1, max);
	}
}
