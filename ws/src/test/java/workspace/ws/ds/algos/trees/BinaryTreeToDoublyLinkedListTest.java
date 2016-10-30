package workspace.ws.ds.algos.trees;

import workspace.ws.ds.algos.trees.BinaryTreeToDoublyLinkedList;
import workspace.ws.ds.data.BinaryTreeNode;
import junit.framework.TestCase;

public class BinaryTreeToDoublyLinkedListTest extends TestCase {
	private BinaryTreeNode treeRoot;
	private BinaryTreeToDoublyLinkedList converter;

	protected void setUp() {
		BinaryTreeNode root = new BinaryTreeNode("1");
		root.left = new BinaryTreeNode("2");
		root.right = new BinaryTreeNode("3");
		root.left.left = new BinaryTreeNode("4");
		root.left.right = new BinaryTreeNode("5");
		root.right.left = new BinaryTreeNode("6");
		root.right.right = new BinaryTreeNode("7");
		treeRoot = root;
		converter = new BinaryTreeToDoublyLinkedList(treeRoot);
	}

	public void testBinaryTreeToDoublyLinkedListConvertion() {
		BinaryTreeNode head = converter.getDoublyLinkedList();

		String resultSet[] = { "4", "2", "5", "1", "6", "3", "7" };
		int index = 0;

		while (head != null) {
			assertEquals(resultSet[index], head.data);
			head = head.right;
			++index;
		}
	}
}
