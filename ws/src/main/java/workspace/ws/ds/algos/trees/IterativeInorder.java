package workspace.ws.ds.algos.trees;

import workspace.ws.ds.data.BinaryTreeNode;
import workspace.ws.ds.data.Stack;

/**
 * smsg
 * 
 * @author eldo.joseph
 */
public class IterativeInorder {
	BinaryTreeNode root;
	Stack stack;
	
	public IterativeInorder(BinaryTreeNode root) {
		this.root = root;
		stack = new Stack();
	}
	
	public void traverse() {
		BinaryTreeNode current = root;
		boolean done = false;
		
		while (!done) {
			if (current != null) {
				stack.push(current);
				current = current.left;
			}
			
			else {
				if (!stack.isEmpty()) {
					current = (BinaryTreeNode) stack.pop();
					System.out.println(current.data);
					
					current = current.right;
				} else {
					done = true;
				}
			}
		}
	}
}
