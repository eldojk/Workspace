package workspace.ws.ds.data;

public class SortAStack {
	private Stack stack;

	public SortAStack(Stack stack) {
		this.stack = stack;
	}

	@SuppressWarnings("rawtypes")
	public void sort() {
		if (!stack.isEmpty()) {
			Comparable top = (Comparable) stack.pop();
			sort();
			sortedInsert(top);
		}
	}

	@SuppressWarnings({ "rawtypes", "unchecked" })
	private void sortedInsert(Comparable element) {
		if (stack.isEmpty() || element.compareTo((Comparable) stack.peek()) > 1) {
			stack.push(element);
		} else {
			Comparable top = (Comparable) stack.pop();
			sortedInsert(element);
			stack.push(top);
		}
	}
	
	public Stack getStack() {
		return stack;
	}
}
