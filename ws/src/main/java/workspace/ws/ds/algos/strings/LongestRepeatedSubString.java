package workspace.ws.ds.algos.strings;

public class LongestRepeatedSubString {
	private SuffixArrays suffixArrays;
	
	public LongestRepeatedSubString(String string) {
		suffixArrays = new SuffixArrays(string);
	}
	
	public int longestCommonPrefix(String str1, String str2) {
		int i = 0;
		int minimumLength = str1.length();
		
		if (str2.length() < minimumLength)
			minimumLength = str2.length();
		
		while (i < minimumLength) {
			if (str1.charAt(i) == str2.charAt(i))
				i++;
			else
				break;
		}
		
		return i;
	}
	
	public String getLRS() {
		String[] suffixes = suffixArrays.getSuffixes();
		
		String lrs = "";
		for (int i = 0; i < suffixes.length - 1; i++) {
			int len = longestCommonPrefix(suffixes[i], suffixes[i + 1]);
			
			if (len > lrs.length())
				lrs = suffixes[i].substring(0, len);
		}
		
		return lrs;
	}
}
