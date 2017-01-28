package workspace.ws.ds.data;

public class StackUsingLinkedList {
	private LinkedListNode top;
	
	public void push(String str) {
		if (top == null) {
			top = new LinkedListNode(str);
			return;
		}
		
		LinkedListNode newTop = new LinkedListNode(str);
		newTop.next = top;
		top = newTop;
	}
	
	public String pop() {
		if (top == null) {
			throw new NullPointerException("No more elements");
		}
		
		String value = top.data;
		top = top.next;
		
		return value;
	}
	
	public boolean isEmpty() {
		return top == null;
	}
}
