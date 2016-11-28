package workspace.ws.ds.data;

/**
 * UF DataStructure with QuickFind implementation
 * 
 * @author eldo.joseph
 *
 */
public class UnionFind {
	private int[] elements;
	private int size;

	public UnionFind(int size) {
		elements = new int[size];
		this.size = size;

		for (int i = 0; i < size; i++) {
			elements[i] = i;
		}
	}

	public void union(int element1, int element2) {
		int secondElementSet = elements[element2];

		for (int i = 0; i < size; i++) {
			if (elements[i] == secondElementSet)
				elements[i] = elements[element1];
		}
	}

	public boolean find(int element1, int element2) {
		return elements[element1] == elements[element2];
	}
}
