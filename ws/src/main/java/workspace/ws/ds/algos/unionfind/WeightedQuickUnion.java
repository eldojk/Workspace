package workspace.ws.ds.algos.unionfind;

import workspace.ws.ds.algos.unionfind.UnionFind;

public class WeightedQuickUnion implements UnionFind{

	private int[] elementsArray;
	private int[] sizeArray;
	
	public WeightedQuickUnion(int size) {
		elementsArray = new int[size];
		sizeArray = new int[size];
		
		for (int i = 0; i < size; i++) {
			elementsArray[i] = i;
			sizeArray[i] = 1;
		}
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
		
		if (sizeArray[rootOfp] <= sizeArray[rootOfq]) {
			elementsArray[rootOfp] = rootOfq;
			sizeArray[rootOfq] += sizeArray[rootOfp];
		} else {
			elementsArray[rootOfq] = rootOfp;
			sizeArray[rootOfp] += sizeArray[rootOfq];
		}
		
	}

	@Override
	public boolean isConnected(int p, int q) {
		return getRoot(p) == getRoot(q);
	}

}
