package workspace.ws.ds.algos.trees;

import junit.framework.TestCase;
import workspace.ws.ds.data.BinaryTreeNode;

public class PruneSubtreesInLessThanKPathTest extends TestCase {
	private BinaryTreeNode treeRoot;
	private PruneSubtreesInLessThanKPath treePruner;

	protected void setUp() {
		BinaryTreeNode root = new BinaryTreeNode("1");
		root.left = new BinaryTreeNode("2");
		root.right = new BinaryTreeNode("3");
		root.left.left = new BinaryTreeNode("4");
		root.left.right = new BinaryTreeNode("5");
		root.right.left = new BinaryTreeNode("6");
		root.right.right = new BinaryTreeNode("7");
		root.left.left.left = new BinaryTreeNode("8");
		root.left.left.right = new BinaryTreeNode("9");
		root.left.right.left = new BinaryTreeNode("12");
		root.right.right.left = new BinaryTreeNode("10");
		root.right.right.left.right = new BinaryTreeNode("11");
		root.left.left.right.left = new BinaryTreeNode("13");
		root.left.left.right.right = new BinaryTreeNode("14");
		root.left.left.right.right.left = new BinaryTreeNode("15");

		treeRoot = root;
		treePruner = new PruneSubtreesInLessThanKPath(treeRoot, 20);
	}

	public void testPruneSubtreesInLessThanKPath() {
		BinaryTreeNode root = treePruner.pruneTree();

		assertNull(root.left.left.left);
		assertNull(root.right.left);

		assertNotNull(root.left.left.right);
		assertNotNull(root.left.left.right.left);
		assertNotNull(root.left.left.right.right);
		assertNotNull(root.left.left.right.right.left);
		assertNotNull(root.left.right);
		assertNotNull(root.left.right.left);
		assertNotNull(root.right.right);
		assertNotNull(root.right.right.left);
		assertNotNull(root.right.right.left.right);
	}
}
