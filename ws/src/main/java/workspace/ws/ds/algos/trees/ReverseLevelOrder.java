package workspace.ws.ds.algos.trees;

import workspace.ws.ds.data.BinaryTreeNode;
import workspace.ws.ds.data.Queue;
import workspace.ws.ds.data.Stack;

/**
 * http://www.geeksforgeeks.org/reverse-level-order-traversal/
 * 
 * @author eldo.joseph
 *
 */
public class ReverseLevelOrder {
	private BinaryTreeNode root;
	private String traversal;
	private Queue queue;
	private Stack stack;

	public ReverseLevelOrder(BinaryTreeNode root) {
		this.root = root;
		this.traversal = "";
		this.queue = new Queue();
		this.stack = new Stack();
	}

	private void appendString(String subString) {
		traversal += subString + " ";
	}

	private void traverse() {
		queue.push(root);

		while (!queue.isEmpty()) {
			BinaryTreeNode node = (BinaryTreeNode) queue.pop();
			stack.push(node);
			
			// Pushing right first, so it goes to the bottom of the stack
			if (node.right != null)
				queue.push(node.right);

			if (node.left != null)
				queue.push(node.left);
		}

		while (!stack.isEmpty()) {
			BinaryTreeNode node = (BinaryTreeNode) stack.pop();
			appendString(node.data);
		}
	}

	public String getTraversal() {
		traverse();
		return traversal;
	}
}
