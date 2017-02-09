package workspace.ws.ds.algos.heaps;

import junit.framework.TestCase;

public class ConnectNRopesWithMinimumCostTest extends TestCase{
	private ConnectNRopesWithMinimumCost connector;

	protected void setUp() {
		int[] arr = new int[] {4, 3, 2, 6};
		connector = new ConnectNRopesWithMinimumCost(arr, 4);
	}

	public void testConnectNRopesWithMinimumCost() {
		assertEquals(29, connector.getMinCost());
	}
}
