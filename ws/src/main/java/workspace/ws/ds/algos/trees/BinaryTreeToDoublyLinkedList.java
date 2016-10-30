package workspace.ws.ds.algos.trees;

import workspace.ws.ds.data.BinaryTreeNode;

/**
 * http://www.geeksforgeeks.org/in-place-convert-a-given-binary-tree-to-doubly-linked-list/
 * 
 * @author eldo.joseph
 *
 */
public class BinaryTreeToDoublyLinkedList {
	private BinaryTreeNode root;

	public BinaryTreeToDoublyLinkedList(BinaryTreeNode root) {
		this.root = root;
	}

	private BinaryTreeNode getLeftMostNode(BinaryTreeNode node) {
		while (node.left != null)
			node = node.left;

		return node;
	}

	private BinaryTreeNode getRightMostNode(BinaryTreeNode node) {
		while (node.right != null)
			node = node.right;

		return node;
	}

	private BinaryTreeNode convertToDoublyLinkedList(BinaryTreeNode node) {
		if (node == null)
			return node;

		BinaryTreeNode leftRoot = convertToDoublyLinkedList(node.left);

		if (leftRoot != null) {
			leftRoot = getRightMostNode(leftRoot);
			leftRoot.right = node;
			node.left = leftRoot;
		}

		BinaryTreeNode rightRoot = convertToDoublyLinkedList(node.right);

		if (rightRoot != null) {
			rightRoot = getLeftMostNode(rightRoot);
			rightRoot.left = node;
			node.right = rightRoot;
		}

		return node;
	}

	public BinaryTreeNode getDoublyLinkedList() {
		BinaryTreeNode llRoot = convertToDoublyLinkedList(this.root);
		return getLeftMostNode(llRoot);
	}
}
