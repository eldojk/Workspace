package workspace.ws.ds.algos.tries;

// http://www.geeksforgeeks.org/implement-a-phone-directory/ amzn
public class RWayTrie<Value> {

	private static final int R = 256;
	private Node root = new Node();

	private static class Node {
		private Object value;
		private Node[] next = new Node[R];
	}

	public void put(String key, Value val) {
		root = put(root, key, val, 0);
	}

	private Node put(Node node, String key, Value val, int d) {
		if (node == null)
			node = new Node();

		if (d == key.length()) {
			node.value = val;
			return node;
		}

		char c = key.charAt(d);
		node.next[c] = put(node.next[c], key, val, d + 1);
		return node;
	}

	@SuppressWarnings("unchecked")
	public Value get(String key) {
		Node node = get(root, key, 0);

		if (node == null)
			return null;

		return (Value) node.value;
	}

	public Node get(Node node, String key, int d) {
		if (node == null)
			return null;

		if (d == key.length())
			return node;

		char c = key.charAt(d);
		return get(node.next[c], key, d + 1);
	}

	public boolean contains(String key) {
		return get(key) != null;
	}
	
	private Node findPrefixNode(Node node, String prefix, int index) {
		if ((index < prefix.length()) && (node != null)) {
			Node next = node.next[prefix.charAt(index)];
			return findPrefixNode(next, prefix, index + 1);
		}
		
		return node;
	}
	
	private void recursivelyPrintPrefixes(String prefix, Node node) {
		if (node.value != null) {
			System.out.println(prefix);
		}
		
		for (int i = 0; i < node.next.length; i++) {
			if (node.next[i] != null)
				recursivelyPrintPrefixes(prefix + (char) i, node.next[i]);
		}
	}
	
	/**
	 * For search suggestions
	 * 
	 * @param prefix
	 */
	public void searchWithPrefix(String prefix) {
		Node node = findPrefixNode(root, prefix, 0);
		
		if (node == null) {
			System.out.println("No results found");
			return;
		}
		
		recursivelyPrintPrefixes(prefix, node);
	}
	
	private void printLexicographically(Node node, String prefix) {
		if (node.value != null) {
			System.out.println(prefix);
		}
		
		for(int i = 0; i < R; i++) {
			if (node.next[i] != null) {
				printLexicographically(node.next[i], prefix + (char) i);
			}
		}
	}
	
	public void printInAlphabeticalOrder() {
		printLexicographically(root, "");
	}
}
