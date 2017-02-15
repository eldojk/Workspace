package workspace.ws.ds.data;

import java.util.ArrayList;
import java.util.List;

public class Stack {
	private List<Object> elements;

	public Stack() {
		elements = new ArrayList<Object>();
	}
	
	public void printStack() {
		for (Object element : elements) {
			System.out.println(element);
		}
	}

	public void push(Object object) {
		elements.add(object);
	}

	public Object pop() {
		if (elements.size() < 1) {
			throw new NullPointerException("No more elements");
		}

		return elements.remove(elements.size() - 1);
	}
	
	public boolean isEmpty() {
		return elements.size() == 0;
	}
	
	public Object peek() {
		if (elements.size() < 1) {
			throw new NullPointerException("No more elements");
		}
		
		return elements.get(elements.size() - 1);
	}
}
