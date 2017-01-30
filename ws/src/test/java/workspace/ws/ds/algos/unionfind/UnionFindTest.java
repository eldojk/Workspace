package workspace.ws.ds.algos.unionfind;

import junit.framework.TestCase;

public class UnionFindTest extends TestCase{
	
	public void testQuickFind() {
		UnionFind uf = new QuickFind(10);
		
		uf.union(0, 5);
		uf.union(5, 6);
		uf.union(1, 2);
		uf.union(8, 3);
		uf.union(8, 9);
		uf.union(3, 4);
		
		assertTrue(uf.isConnected(0, 6));
		assertTrue(uf.isConnected(5, 6));
		assertTrue(uf.isConnected(1, 2));
		assertTrue(uf.isConnected(8, 4));
		assertTrue(uf.isConnected(3, 8));
		
		assertFalse(uf.isConnected(3, 1));
		assertFalse(uf.isConnected(0, 4));

	}
	
	public void testQuickUnion() {
		UnionFind uf = new QuickUnion(10);
		
		uf.union(0, 5);
		uf.union(5, 6);
		uf.union(1, 2);
		uf.union(8, 3);
		uf.union(8, 9);
		uf.union(3, 4);
		
		assertTrue(uf.isConnected(0, 6));
		assertTrue(uf.isConnected(5, 6));
		assertTrue(uf.isConnected(1, 2));
		assertTrue(uf.isConnected(8, 4));
		assertTrue(uf.isConnected(3, 8));
		
		assertFalse(uf.isConnected(3, 1));
		assertFalse(uf.isConnected(0, 4));

	}
	
	public void testWeightedQuickUnion() {
		UnionFind uf = new WeightedQuickUnion(10);
		
		uf.union(0, 5);
		uf.union(5, 6);
		uf.union(1, 2);
		uf.union(8, 3);
		uf.union(8, 9);
		uf.union(3, 4);
		
		assertTrue(uf.isConnected(0, 6));
		assertTrue(uf.isConnected(5, 6));
		assertTrue(uf.isConnected(1, 2));
		assertTrue(uf.isConnected(8, 4));
		assertTrue(uf.isConnected(3, 8));
		
		assertFalse(uf.isConnected(3, 1));
		assertFalse(uf.isConnected(0, 4));

	}
}
