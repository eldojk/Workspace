package workspace.ws.ds.algos.unionfind;

public class QuickFind implements UnionFind {
	
	private int[] elementsArray;
	
	public QuickFind(int size) {
		elementsArray = new int[size];
		for (int i = 0; i < size; i++)
			elementsArray[i] = i;
	}

	@Override
	public void union(int p, int q) {
		int pid = elementsArray[p];
		int qid = elementsArray[q];
		
		for (int i = 0; i <  elementsArray.length; i++) {
			if(elementsArray[i] == pid) {
				elementsArray[i] = qid;
			}
		}
	}

	@Override
	public boolean isConnected(int p, int q) {
		return elementsArray[p] == elementsArray[q];
	}
	
}
