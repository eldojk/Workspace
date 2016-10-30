package workspace.ws.ds.algos.trees;

import java.util.Arrays;
import java.util.List;

import workspace.ws.ds.data.BinaryTreeNode;
import junit.framework.TestCase;

public class LeftViewTest extends TestCase{
	private BinaryTreeNode treeRoot;
	private LeftView viewer;
	
	protected void setUp() {
		BinaryTreeNode root = new BinaryTreeNode("1");
		root.left = new BinaryTreeNode("2");
		root.right = new BinaryTreeNode("3");
		root.left.left = new BinaryTreeNode("4");
		root.left.right = new BinaryTreeNode("5");
		root.right.left = new BinaryTreeNode("6");
		root.right.right = new BinaryTreeNode("7");
		treeRoot = root;
	}
	
	public void testLeftView() {
		viewer = new LeftView(treeRoot);
		List<String> expectedOutput = Arrays.asList(new String[]{"1", "2", "4"});
		
		List<String> result = viewer.getLeftView();
		
		assertEquals(expectedOutput, result);
	}
	
	public void testLeftViewAnother() {
		treeRoot.left.left = null;
		viewer = new LeftView(treeRoot);
		List<String> expectedOutput = Arrays.asList(new String[]{"1", "2", "5"});
		
		List<String> result = viewer.getLeftView();
		
		assertEquals(expectedOutput, result);
	}
}
