package workspace.ws.ds.algos.strings;

public class ReverseString {

	private StringBuilder string;

	private void reverseString(StringBuilder string, int start, int end) {
		if (start > end) {
			return;
		}

		char startChar = string.charAt(start);
		char endChar = string.charAt(end);

		string.setCharAt(start, endChar);
		string.setCharAt(end, startChar);

		reverseString(string, start + 1, end - 1);
	}

	public String reverse(String string) {
		this.string = new StringBuilder(string);
		reverseString(this.string, 0, string.length() - 1);

		return this.string.toString();
	}

}
