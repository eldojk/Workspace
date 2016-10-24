package workspace.ws.ds.trees;

import workspace.ws.ds.data.BinaryTreeNode;
import junit.framework.TestCase;

public class BoundaryTraversalTest extends TestCase{
	private BinaryTreeNode treeRoot;
	private BoundaryTraversal traverser;
	
	protected void setUp() {
		BinaryTreeNode root = new BinaryTreeNode("20");
		root.left = new BinaryTreeNode("8");
		root.right = new BinaryTreeNode("22");
		root.left.left = new BinaryTreeNode("4");
		root.left.right = new BinaryTreeNode("12");
		root.right.right = new BinaryTreeNode("25");
		root.left.right.left = new BinaryTreeNode("10");
		root.left.right.right = new BinaryTreeNode("14");
		treeRoot = root;
		traverser = new BoundaryTraversal(treeRoot);
	}
	
	public void testTraversal() {
		String result = traverser.printTraversal();
		String expectedOutput = "20 8 4 10 14 25 22 ";
		assertTrue(result.equals(expectedOutput));
	}
}
