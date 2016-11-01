package workspace.ws.ds.data;

import java.util.List;
import java.util.ArrayList;

public class Queue {
	private List<Object> elements;

	public Queue() {
		elements = new ArrayList<Object>();
	}

	public void push(Object object) {
		elements.add(object);
	}

	public Object pop() {
		if (elements.size() < 1) {
			throw new NullPointerException("No more elements");
		}

		return elements.remove(0);
	}

	public boolean isEmpty() {
		return elements.size() == 0;
	}
}
