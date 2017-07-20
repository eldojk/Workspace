package workspace.ws.ds.algos.graphs;

import java.util.List;

import workspace.ws.ds.data.DiGraph;

/**
 * amzn
 * 
 * http://www.geeksforgeeks.org/given-array-strings-find-strings-can-chained-
 * form-circle/
 * 
 * @author eldo.joseph
 */
public class CanWordsChain {

	public static boolean canThey(List<String> words) {
		DiGraph g = new DiGraph(26);

		for (String word : words) {
			int asciiA = Integer.valueOf('a');

			int src = Integer.valueOf(word.charAt(0)) - asciiA;
			int dest = Integer.valueOf(word.charAt(word.length() - 1)) - asciiA;

			g.addEdge(src, dest);
		}

		return EulerianDirectedGraph.isEulerianCircuit(g);
	}
}
