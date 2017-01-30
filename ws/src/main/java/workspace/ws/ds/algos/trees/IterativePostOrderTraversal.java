package workspace.ws.ds.algos.trees;

import workspace.ws.ds.data.BinaryTreeNode;
import workspace.ws.ds.data.Stack;

/**
 * http://www.geeksforgeeks.org/iterative-postorder-traversal/
 * 
 * @author eldo.joseph
 */
public class IterativePostOrderTraversal {
	private BinaryTreeNode root;
	private Stack stack1;
	private Stack stack2;
	
	public IterativePostOrderTraversal(BinaryTreeNode root) {
		this.root = root;
		stack1 = new Stack();
		stack2 =  new Stack();
	}
	
	public String traverse() {
		stack1.push(root);
		
		while(!stack1.isEmpty()) {
			BinaryTreeNode node = (BinaryTreeNode) stack1.pop();
			stack2.push(node);
			
			if (node.left != null)
				stack1.push(node.left);
			if (node.right != null)
				stack1.push(node.right);
		}
		
		String repr = "";
		while (!stack2.isEmpty()) {
			BinaryTreeNode node = (BinaryTreeNode) stack2.pop();
			repr += node.toString() + " ";
		}
		
		return repr;
	}
}
