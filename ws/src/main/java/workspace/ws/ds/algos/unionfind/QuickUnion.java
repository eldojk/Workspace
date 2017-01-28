package workspace.ws.ds.algos.unionfind;

public class QuickUnion implements UnionFind{

	private int[] elementsArray;
	
	public QuickUnion(int size) {
		elementsArray = new int[size];
		for (int i = 0; i < size; i++)
			elementsArray[i] = i;
	}
	
	private int getRoot(int n) {
		while(n != elementsArray[n]) {
			n = elementsArray[n];
		}
		
		return n;
	}
	
	@Override
	public void union(int p, int q) {
		int rootOfp = getRoot(p);
		int rootOfq = getRoot(q);
		
		elementsArray[rootOfp] = rootOfq;
	}

	@Override
	public boolean isConnected(int p, int q) {
		return getRoot(p) == getRoot(q);
	}

}
