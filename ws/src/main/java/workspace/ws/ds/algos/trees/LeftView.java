package workspace.ws.ds.algos.trees;

import java.util.ArrayList;
import java.util.List;

import workspace.ws.ds.data.BinaryTreeNode;

/**
 * amzn
 *
 * http://www.geeksforgeeks.org/print-left-view-binary-tree/
 * 
 * @author eldo.joseph
 *
 */
public class LeftView {

	private BinaryTreeNode root;
	private int maxLevel;
	private List<String> leftView;

	public LeftView(BinaryTreeNode root) {
		this.root = root;
		leftView = new ArrayList<String>();
	}

	private void computeLeftView(BinaryTreeNode root, int level) {
		if (root == null) {
			return;
		}

		if (level > maxLevel) {
			leftView.add(root.data);
			maxLevel = level;
		}

		computeLeftView(root.left, level + 1);
		computeLeftView(root.right, level + 1);
	}

	public List<String> getLeftView() {
		computeLeftView(this.root, 1);
		return leftView;
	}
}
