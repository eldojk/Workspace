package workspace.ws.ds.algos.trees;

import workspace.ws.ds.data.BinaryTreeNode;

/**
 * http://www.geeksforgeeks.org/remove-all-nodes-which-lie-on-a-path-having-sum-
 * less-than-k/
 * 
 * Remove all nodes which don’t lie in any path with sum>= k, Given a binary
 * tree, a complete path is defined as a path from root to a leaf. The sum of
 * all nodes on that path is defined as the sum of that path. Given a number K,
 * you have to remove (prune the tree) all nodes which don’t lie in any path
 * with sum>=k.
 * 
 * @author eldo.joseph
 *
 */
public class PruneSubtreesInLessThanKPath {

	private BinaryTreeNode root;
	private int k;

	public PruneSubtreesInLessThanKPath(BinaryTreeNode root, int k) {
		this.root = root;
		this.k = k;
	}

	private boolean isAnyPathSumGreaterOrEqualsToK(BinaryTreeNode root,
			int currentSum) {
		if (currentSum >= this.k) {
			return true;
		}

		if (root == null) {
			return false;
		}

		boolean hasLeftSubtreeGotRequiredSum = isAnyPathSumGreaterOrEqualsToK(
				root.left, currentSum + Integer.parseInt(root.data));
		boolean hasRightSubtreeGotRequiredSum = isAnyPathSumGreaterOrEqualsToK(
				root.right, currentSum + Integer.parseInt(root.data));

		if (!hasLeftSubtreeGotRequiredSum)
			root.left = null;

		if (!hasRightSubtreeGotRequiredSum)
			root.right = null;

		return (hasLeftSubtreeGotRequiredSum || hasRightSubtreeGotRequiredSum);
	}

	public BinaryTreeNode pruneTree() {
		isAnyPathSumGreaterOrEqualsToK(this.root, 0);
		return this.root;
	}
}
