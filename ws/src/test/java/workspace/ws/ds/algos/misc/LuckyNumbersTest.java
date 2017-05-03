package workspace.ws.ds.algos.misc;

import junit.framework.TestCase;

public class LuckyNumbersTest extends TestCase{

	public void testLuckyNumbers() {
		assertTrue(LuckyNumbers.isLucky(7));
	}
	
	public void testUnLuckyNumbers() {
		assertFalse(LuckyNumbers.isLucky(6));
	}
}
