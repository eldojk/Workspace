package workspace.ws.ds.algos.strings;

import junit.framework.TestCase;

public class ReverseStringTest extends TestCase{
	private ReverseString reverser;

	protected void setUp() {
		reverser = new ReverseString();
	}

	public void testReverseString() {
		assertEquals("abcd", reverser.reverse("dcba"));
		assertEquals("joseph", reverser.reverse("hpesoj"));
		assertEquals("eldojk", reverser.reverse("kjodle"));
		assertEquals("malayalam", reverser.reverse("malayalam"));
		assertEquals("joe", reverser.reverse("eoj"));
	}
}
