package workspace.ws.ds.algos.unionfind;

public interface UnionFind {
	public void union(int p, int q);
	
	public boolean isConnected(int p, int q);
}
