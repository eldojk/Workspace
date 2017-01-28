package workspace.ws.ds.data;

public class QueueUsingLinkedList {
	private LinkedListNode head;
	private LinkedListNode tail;

	public void push(String data) {
		if (head == null) {
			head = new LinkedListNode(data);
			tail = head;
		}

		tail.next = new LinkedListNode(data);
		tail = tail.next;
	}

	public String pop() {
		if (head == null) {
			throw new NullPointerException("No more elements");
		}

		String elementToPop = head.data;

		if (head == tail) {
			head = null;
			tail = null;
			return elementToPop;
		}

		head = head.next;
		return elementToPop;
	}

	public boolean isEmpty() {
		return head == null;
	}
}
