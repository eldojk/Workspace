package workspace.ws.ds.algos.strings;

import java.util.Arrays;

public class SuffixArrays {
	private String[] suffixes;
	
	public SuffixArrays(String string) {
		int N = string.length();
		suffixes = new String[N];
		
		for (int i = 0; i < N; i++)
			suffixes[i] = string.substring(i, N);
		
		Arrays.sort(suffixes);
	}
	
	public String[] getSuffixes() {
		return suffixes;
	}
}
