package workspace.ws.ds.data;

public class DLLNode<Key, Value> {
	
	public Value data;
	public Key key;
	public DLLNode<Key,Value> prev;
	public DLLNode<Key, Value> next;
	
	public DLLNode(Key key, Value data) {
		this.data = data;
		this.key = key;
	}
}
