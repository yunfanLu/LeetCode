package p028ImplementstrStr;

import java.util.Arrays;

public class Solution {
	private static final boolean DEBUG = false;
    public int strStr(String haystack, String needle) {
    	int res = -1;

    	if(needle == null) return -1;
    	if(needle.length() == 0){
    		return 0;
    	}
    	
        final int[] next = KMP(needle);        
        int j = 0;
        int i = 0;
        for(; i < haystack.length(); i ++){
        	if(haystack.charAt(i) == needle.charAt(j)){
        		j ++;
        		if(j == needle.length()) break;
        	}else{
        		j = next[j];
        		if(j == -1){
        			j = 0;
        		}else{
        			i --;
        		}
        	}
        }
        if(j == needle.length()) {
        	res = i - j + 1;
        }
        return res;
    }

	private int[] KMP(String needle) {
		int[] next = new int[needle.length()];
		next[0] = -1;
		int j = 0;
		int k = -1;
		while(j < needle.length() - 1){
			while(k >= 0 && needle.charAt(k) != needle.charAt(j)){
				k = next[k];
			}
			k ++ ;
			j ++ ;
			next[j] = k;
		}
		{
			if(DEBUG){
				System.out.println(Arrays.toString(needle.toCharArray()));
				System.out.println(Arrays.toString(next));
			}
		}
		return next;
	}
	public static void main(String[] args) {
		String a = "mississippi";
		String b = "issip";
		System.out.println(new Solution().strStr(a, b));
	}
}