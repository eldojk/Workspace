package workspace.ws.ds.algos.misc;

/**
 * amzn
 * 
 * http://stackoverflow.com/questions/25884250/how-to-show-all-combinations-of-ip-address-that-can-be-created-from-a-string-of
 * 
 * @author eldo.joseph
 */
public class AllIpAddresses {
	public static void main(String[] args) {
		String number = "19216801";
		int len = number.length() - 3;
		
		for (int a = 0; a < len; a++) {
			for (int b = 0; b < len - a; b++) {
				for (int c = 0; c < len - a - b; c++) {
					
					StringBuilder sb = new StringBuilder(number);
					
					sb.insert(a + 1, ".");
					sb.insert(a + b + 3, ".");
					sb.insert(a + b + c + 5, ".");
					
					System.out.println(sb);
				}
			}
		}
	}
}
