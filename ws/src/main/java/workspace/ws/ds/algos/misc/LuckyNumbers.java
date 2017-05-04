package workspace.ws.ds.algos.misc;

/**
 * smsg
 * http://www.geeksforgeeks.org/lucky-numbers/
 * 
 * @author eldo.joseph
 */
public class LuckyNumbers {
	
	private static boolean isLucky(int number, int counter) {
		int nextPosition = number;
		
		if (counter > number)
			return true;
		
		if (number % counter == 0)
			return false;
		
		nextPosition = nextPosition - (nextPosition/counter);
		counter++;
		
		return isLucky(nextPosition, counter);
	}
	
	public static boolean isLucky(int number) {
		return isLucky(number, 2);
	}
}
