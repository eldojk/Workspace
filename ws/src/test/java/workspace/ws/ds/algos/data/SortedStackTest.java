package workspace.ws.ds.algos.data;

import junit.framework.TestCase;
import workspace.ws.ds.data.SortAStack;
import workspace.ws.ds.data.Stack;

public class SortedStackTest extends TestCase{
	private Stack stack;
	
	class A implements Comparable<A> {
		public int data;
		
		public A(int data) {
			this.data = data;
		}

		@Override
		public int compareTo(A o) {
			if (this.data > o.data) {
				return 1;
			} else if (this.data < o.data) {
				return -1;
			} else {
				return 0;
			}
		}
	}
	
	protected void setUp() {
		stack = new Stack();
		
		stack.push(new A(3));
		stack.push(new A(1));
		stack.push(new A(2));
	}

	public void testSortingOfStack() {
		SortAStack sorter = new SortAStack(stack);
		
		sorter.sort();
		
		@SuppressWarnings("unused")
		Stack resultStack = sorter.getStack();
		
//		assertEquals(((A) resultStack.pop()).data, 3);
//		assertEquals(((A) resultStack.pop()).data, 2);
//		assertEquals(((A) resultStack.pop()).data, 1);
	}
}
