package workspace.ws.ds.algos.trees;

import workspace.ws.ds.data.BinaryTreeNode;

/**
 * amzn
 *
 * http://www.geeksforgeeks.org/check-leaves-level/
 * 
 * @author eldo.joseph
 *
 */
public class CheckIfAllLeavesAreAtSameLevel {
	private BinaryTreeNode root;
	private int firstLeafLevel;

	public CheckIfAllLeavesAreAtSameLevel(BinaryTreeNode root) {
		this.root = root;
	}

	private boolean isLeaf(BinaryTreeNode node) {
		return (node.left == null) && (node.right == null);
	}

	private boolean isLeavesAtSameLevel(BinaryTreeNode root, int level) {
		if (root == null) {
			return true;
		}

		if (isLeaf(root)) {
			if (firstLeafLevel == 0) {
				firstLeafLevel = level;
				return true;
			} else {
				return firstLeafLevel == level;
			}
		}

		return (isLeavesAtSameLevel(root.left, level + 1) &&
				isLeavesAtSameLevel(root.right, level + 1));
	}

	public boolean isLeavesAtSameLevel() {
		return isLeavesAtSameLevel(this.root, 1);
	}
}
