package workspace.ws.ds.algos.tries;

public class PhoneBook {
	
	public static void main(String[] args) {
		RWayTrie<Boolean> trie = new RWayTrie<Boolean>();
		trie.put("geeks", true);
		trie.put("gee", true);
		trie.put("geccs", true);
		trie.put("sdfss", true);
		trie.put("gks", true);
		trie.put("geeklsgfdfps", true);
		trie.put("abcd", true);
		trie.put("lmn", true);
		trie.put("zebra", true);
		
		trie.searchWithPrefix("gee");
		
		System.out.println("----");
		
		trie.printInAlphabeticalOrder();
	}
}
