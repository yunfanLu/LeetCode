package p003LogestSubstringWithoutRepeatingCharacters;

import java.util.HashMap;
import java.util.LinkedList;
import java.util.TreeMap;

public class Solution {
	private static boolean DEBUG = false;
	
    public int lengthOfLongestSubstring(String s) {
        int res = 0;
        int temp = 0;
        LinkedList<Character> queue = new LinkedList<>();
        HashMap<Character, Boolean> used = new HashMap<>();
        for(int i = 0; i < s.length(); i ++){
        	char ch = s.charAt(i);
        	queue.add(ch);
        	temp ++;
        	if(used.get(ch) != null){
        		while(queue.getFirst().equals(ch) == false){
        			used.remove(queue.getFirst());
        			queue.removeFirst();
        			temp --;
        		}
        		queue.removeFirst();
        		temp--;
        	}
        	used.put(ch, true);
        	res = Math.max(res, temp);
        }
        return res;
    }
    
    public static void main(String[] args) {
		Solution s = new Solution();
		String str = "abc";
		long t0 = System.currentTimeMillis();
		int ans = s.lengthOfLongestSubstring(str);
		long t1 = System.currentTimeMillis();
		System.out.println(ans);
		System.out.println(t1-t0);
    }
}