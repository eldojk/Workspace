package workspace.ws.ds.algos.trees;

import junit.framework.TestCase;
import workspace.ws.ds.data.BinaryTreeNode;

public class IterativePostOrderTraversalTest extends TestCase{
	private BinaryTreeNode treeRoot;
	private IterativePostOrderTraversal traverser;
	
	protected void setUp() {
		BinaryTreeNode root = new BinaryTreeNode("1");
		root.left = new BinaryTreeNode("2");
		root.right = new BinaryTreeNode("3");
		root.left.left = new BinaryTreeNode("4");
		root.left.right = new BinaryTreeNode("5");
		root.right.left = new BinaryTreeNode("6");
		root.right.right = new BinaryTreeNode("7");
		treeRoot = root;
		traverser = new IterativePostOrderTraversal(treeRoot);
	}
	
	public void testBoundaryTraversal() {
		String result = traverser.traverse();
		String expectedOutput = "4 5 2 6 7 3 1 ";
		assertTrue(result.equals(expectedOutput));
	}
}
