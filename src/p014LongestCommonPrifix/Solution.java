package p014LongestCommonPrifix;
/**
 * Write a function to find the longest common prefix string amongst an array of strings.
 * @author onion
 * the common prefix string is all strings' prefix string!
 * @notice
 * the input strs maybe is null or the first string is "".
 * you should know the "" is not null.
 */
public class Solution {
	public String longestCommonPrefix(String[] strs) {
		String res = "";
		if(strs == null || strs.length == 0) return res;
		out:
		for(int i = 0; i < strs[0].length(); i ++){
			char ch = strs[0].charAt(i);
			boolean is = true;
			for(int j = 0; j < strs.length; j ++){
				if(i < strs[j].length() && ch == strs[j].charAt(i)){
					is = true;
				}else{
					break out;
				}
			}
			if(is) res += ch;
		}
		return res;
	}

	public static void main(String[] args) {
		String[] strs = {"aaaaa","aa"};
		System.out.println("ans : " + new Solution().longestCommonPrefix(strs));
		String a = "";
		if(a == null){
			System.out.println("a is null");
		}else{
			System.out.println("a is't null");
		}
	}
}
