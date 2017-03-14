package workspace.ws.ds.algos.graphs;

import workspace.ws.ds.data.DiGraph;
import workspace.ws.ds.data.Stack;

/**
 * http://www.geeksforgeeks.org/given-sorted-dictionary-find-precedence-characters/
 * 
 * @author eldo.joseph
 */
public class AlienLanguageCharacterPrecedence {
	private DiGraph graph;
	private Stack topology;

	private int findMismatchIndex(String a, String b) {
		for (int i = 0; i < Integer.min(a.length(), b.length()); i++) {
			if (a.charAt(i) != b.charAt(i)) {
				return i;
			}
		}

		return -1;
	}

	public AlienLanguageCharacterPrecedence(String[] array, int length) {
		graph = new DiGraph(length);

		for (int i = 1; i < array.length; i++) {
			String str1 = array[i - 1];
			String str2 = array[i];
			int misMatch = findMismatchIndex(str1, str2);

			int u = (int) str1.charAt(misMatch) - (int) 'a';
			int v = (int) str2.charAt(misMatch) - (int) 'a';

			graph.addEdge(u, v);
		}

		TopologicalSort top = new TopologicalSort(graph);
		topology = top.getTopologicalSortedOrder();
	}

	public void printCharsInOrder() {
		while (!topology.isEmpty()) {
			int ch = (int) topology.pop();
			int ascii = ch + (int) 'a';
			System.out.println((char) ascii);
		}
	}

	public static void main(String[] args) {
		AlienLanguageCharacterPrecedence a = new AlienLanguageCharacterPrecedence(
				new String[] { "baa", "abcd", "abca", "cab", "cad" }, 4);
		a.printCharsInOrder();
		
		System.out.println("");
		
		a = new AlienLanguageCharacterPrecedence(
				new String[] { "caa", "aaa","aab" }, 3);
		a.printCharsInOrder();
	}
}
