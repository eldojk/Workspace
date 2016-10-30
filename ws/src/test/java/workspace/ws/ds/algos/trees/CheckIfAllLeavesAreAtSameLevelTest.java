package workspace.ws.ds.algos.trees;

import workspace.ws.ds.algos.trees.CheckIfAllLeavesAreAtSameLevel;
import workspace.ws.ds.data.BinaryTreeNode;
import junit.framework.TestCase;

public class CheckIfAllLeavesAreAtSameLevelTest extends TestCase {
	private BinaryTreeNode treeRoot;
	private CheckIfAllLeavesAreAtSameLevel checker;

	protected void setUp() {
		BinaryTreeNode root = new BinaryTreeNode("1");
		root.left = new BinaryTreeNode("2");
		root.right = new BinaryTreeNode("3");
		root.left.left = new BinaryTreeNode("4");
		root.left.right = new BinaryTreeNode("5");
		root.right.left = new BinaryTreeNode("6");
		root.right.right = new BinaryTreeNode("7");
		treeRoot = root;
	}

	public void testCheckIfAllLeavesAreAtSameLevel() {
		checker = new CheckIfAllLeavesAreAtSameLevel(treeRoot);
		assertTrue(checker.isLeavesAtSameLevel());
	}

	public void testCheckIfAllLeavesAreAtSameLevelFalseCondition() {
		treeRoot.left.left.left = new BinaryTreeNode("8");
		checker = new CheckIfAllLeavesAreAtSameLevel(treeRoot);
		assertFalse(checker.isLeavesAtSameLevel());
	}
}
