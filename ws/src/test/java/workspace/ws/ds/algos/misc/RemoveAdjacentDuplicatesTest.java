package workspace.ws.ds.algos.misc;

import junit.framework.TestCase;

public class RemoveAdjacentDuplicatesTest extends TestCase{
	
	public void testRemove() {
		assertEquals(RemoveAdjacentDuplicates.remove("azxxxzy"), "azxzy");
	}
}
