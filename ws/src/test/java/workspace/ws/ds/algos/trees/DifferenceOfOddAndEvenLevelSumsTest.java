package workspace.ws.ds.algos.trees;

import junit.framework.TestCase;
import workspace.ws.ds.data.BinaryTreeNode;
import workspace.ws.ds.algos.trees.DifferenceOfOddAndEvenLevelSums;

public class DifferenceOfOddAndEvenLevelSumsTest extends TestCase{
	private BinaryTreeNode treeRoot;
	private DifferenceOfOddAndEvenLevelSums diffCalculator;
	
	protected void setUp() {
		BinaryTreeNode root = new BinaryTreeNode("1");
		root.left = new BinaryTreeNode("2");
		root.right = new BinaryTreeNode("3");
		root.left.left = new BinaryTreeNode("4");
		root.left.right = new BinaryTreeNode("5");
		root.right.left = new BinaryTreeNode("6");
		root.right.right = new BinaryTreeNode("7");
		treeRoot = root;
		diffCalculator = new DifferenceOfOddAndEvenLevelSums(treeRoot);
	}
	
	public void testDifferenceOfOddAndEvenLevelSums() {
		int result = diffCalculator.calculateDiff();
		assertEquals(result, 18);
	}
}
