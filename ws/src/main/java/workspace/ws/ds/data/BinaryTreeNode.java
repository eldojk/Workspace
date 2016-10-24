package workspace.ws.ds.data;

public class BinaryTreeNode {

	public String data;
	public BinaryTreeNode left;
	public BinaryTreeNode right;

	public BinaryTreeNode(String data, BinaryTreeNode left, BinaryTreeNode right) {
		this.data = data;
		this.left = left;
		this.right = right;
	}
	
	public BinaryTreeNode(String data) {
		this.data = data;
	}
	
	public String toString() {
		return data;
	}

	public static boolean isLeafNode(BinaryTreeNode node) {
		return (node.left == null) & (node.right == null);
	}
}
