package workspace.ws.ds.algos.trees;

import workspace.ws.ds.algos.trees.ReverseLevelOrder;
import workspace.ws.ds.data.BinaryTreeNode;
import junit.framework.TestCase;

public class ReverseLevelOrderTest extends TestCase{
	private BinaryTreeNode treeRoot;
	private ReverseLevelOrder traverser;
	
	protected void setUp() {
		BinaryTreeNode root = new BinaryTreeNode("1");
		root.left = new BinaryTreeNode("2");
		root.right = new BinaryTreeNode("3");
		root.left.left = new BinaryTreeNode("4");
		root.left.right = new BinaryTreeNode("5");
		root.right.left = new BinaryTreeNode("6");
		root.right.right = new BinaryTreeNode("7");
		treeRoot = root;
		traverser = new ReverseLevelOrder(treeRoot);
	}
	
	public void testReverseLevelOrderTraversal() {
		String result = traverser.getTraversal();
		String expectedOutput = "4 5 6 7 2 3 1 ";
		assertTrue(result.equals(expectedOutput));
	}
}
