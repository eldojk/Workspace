package workspace.ws.ds.algos.misc;

import workspace.ws.ds.data.Stack;

/**
 * smsg
 * 
 * http://www.geeksforgeeks.org/recursively-remove-adjacent-duplicates-given-string/
 * 
 * @author eldo.joseph
 */
public class RemoveAdjacentDuplicates {
	
	public static String remove(String str) {
		Stack stack = new Stack();
		
		for (int i = 0; i < str.length(); i++) {
			char ch = str.charAt(i);
			
			if (!stack.isEmpty() && (char) stack.peek() == ch) {
				stack.pop();
			}
			else {
				stack.push(ch);
			}
		}
		
		StringBuilder builder = new StringBuilder();
		
		while (!stack.isEmpty()) {
			builder.append((char) stack.pop());
		}
		
		builder.reverse();
		
		return builder.toString();
	}
}
