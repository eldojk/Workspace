package workspace.ws.ds.algos.misc;

/**
 * smsg
 * http://www.geeksforgeeks.org/find-excel-column-name-given-number/
 * 
 * @author eldo.joseph
 */
public class ExcelColumns {
	
	private static char getChar(int number) {
		if (number == 0)
			return 'Z';
		
		int asciiA = (int) 'A';
		int requiredAscii = (number - 1 + asciiA);
		
		return (char) requiredAscii;
	}
	
	public static String getColName(int number) {
		StringBuilder builder = new StringBuilder();
		
		while (number > 0) {
			int remainder = number % 26;
			char chr = getChar(remainder);
			
			if (chr == 'Z')
				number = (number/26) - 1;
			else
				number = (number / 26);
			
			builder.append(chr);
		}
		
		builder.reverse();
		
		return builder.toString();
	}
}
