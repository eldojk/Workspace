package workspace.ws.ds.algos.heaps;

import junit.framework.TestCase;

public class PriorityQueueTest extends TestCase {
	private MaxPriorityQueue<Integer> mpq;
	private MinPriorityQueue<Integer> mpq2;
	
	protected void setUp() {
		mpq = new MaxPriorityQueue<Integer>(10);
		mpq2 = new MinPriorityQueue<Integer>(10);
	}

	public void testMaxPriorityQueue() {
		mpq.insert(3);
		mpq.insert(6);
		mpq.insert(2);
		mpq.insert(1);
		
		int max = mpq.deleteTop();
		assertEquals(6, max);
		max = mpq.deleteTop();
		assertEquals(3, max);
		max = mpq.deleteTop();
		assertEquals(2, max);
		max = mpq.deleteTop();
		assertEquals(1, max);
	}
	
	public void testMinPriorityQueue() {
		mpq2.insert(3);
		mpq2.insert(6);
		mpq2.insert(2);
		mpq2.insert(1);
		
		int max = mpq2.deleteTop();
		assertEquals(1, max);
		max = mpq2.deleteTop();
		assertEquals(2, max);
		max = mpq2.deleteTop();
		assertEquals(3, max);
		max = mpq2.deleteTop();
		assertEquals(6, max);
	}
}
