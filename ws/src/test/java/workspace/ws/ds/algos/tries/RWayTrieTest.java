package workspace.ws.ds.algos.tries;

import junit.framework.TestCase;

public class RWayTrieTest extends TestCase{
	private RWayTrie<Integer> trie;
	
	protected void setUp() {
		trie = new RWayTrie<Integer>();
	}
	
	public void testTrieOperations() {
		trie.put("eldo", 7);
		trie.put("joe", 3);
		
		assertEquals(7, (int) trie.get("eldo"));
		assertEquals(3, (int) trie.get("joe"));
		
		assertEquals(null, trie.get("joseph"));
		
		assertTrue(trie.contains("joe"));
		assertFalse(trie.contains("baby"));
	}
}
