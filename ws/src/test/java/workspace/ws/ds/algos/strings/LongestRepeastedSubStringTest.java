package workspace.ws.ds.algos.strings;

import junit.framework.TestCase;

public class LongestRepeastedSubStringTest extends TestCase{
	private LongestRepeatedSubString util;

	protected void setUp() {
		util = new LongestRepeatedSubString("aacaagtttacaagc");
	}

	public void testLRS() {
		assertEquals("acaag", util.getLRS());
	}
}
