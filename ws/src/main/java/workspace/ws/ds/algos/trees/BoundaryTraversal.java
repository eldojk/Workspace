package workspace.ws.ds.algos.trees;

import workspace.ws.ds.data.BinaryTreeNode;

public class BoundaryTraversal {

	private BinaryTreeNode root;
	private String traversal;

	public BoundaryTraversal(BinaryTreeNode root) {
		this.root = root;
		this.traversal = "";
	}

	private void appendString(String subString) {
		this.traversal += subString + " ";
	}

	private void printTopDownLeft(BinaryTreeNode root) {
		if (root == null)
			return;

		if ((root.left != null) & (!BinaryTreeNode.isLeafNode(root.left))) {
			appendString(root.left.data);
			printTopDownLeft(root.left);
		}
	}

	private void printBottomUpRight(BinaryTreeNode root) {
		if (root == null)
			return;

		if ((root.right != null) & (!BinaryTreeNode.isLeafNode(root.right))) {
			printBottomUpRight(root.right);
			appendString(root.right.data);
		}
	}

	private void printLeaves(BinaryTreeNode root) {
		if (root != null) {
			printLeaves(root.left);

			if (BinaryTreeNode.isLeafNode(root)) {
				appendString(root.data);
			}

			printLeaves(root.right);
		}
	}

	private void printRoot(BinaryTreeNode root) {
		if (root != null)
			appendString(root.data);
	}

	public String getTraversal() {
		printRoot(this.root);
		printTopDownLeft(this.root);
		printLeaves(this.root);
		printBottomUpRight(this.root);

		return this.traversal;
	}
}
