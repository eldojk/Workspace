package workspace.ws.ds.algos.trees;

import workspace.ws.ds.data.BinaryTreeNode;

public class DifferenceOfOddAndEvenLevelSums {

	private int oddSum;
	private int evenSum;
	private BinaryTreeNode root;

	public DifferenceOfOddAndEvenLevelSums(BinaryTreeNode root) {
		this.root = root;
	}

	private void computeSum(BinaryTreeNode root, int level) {
		if (root == null)
			return;

		if (level % 2 == 0) {
			evenSum += Integer.parseInt(root.data);
		} else {
			oddSum += Integer.parseInt(root.data);
		}

		computeSum(root.left, level + 1);
		computeSum(root.right, level + 1);
	}

	public int calculateDiff() {
		computeSum(this.root, 0);
		return Math.abs(oddSum - evenSum);
	}
}
