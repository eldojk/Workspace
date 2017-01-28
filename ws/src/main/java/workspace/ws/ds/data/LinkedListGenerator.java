package workspace.ws.ds.data;

public class LinkedListGenerator {

	public static LinkedListNode fromString(String str) {
		String[] datas = str.split(" ");

		return fromArray(datas);
	}

	public static LinkedListNode fromArray(String[] str) {
		LinkedListNode head = null;

		for (String data : str) {
			LinkedListNode node = new LinkedListNode(data);

			if (head == null)
				head = node;
		}

		return head;
	}
}
