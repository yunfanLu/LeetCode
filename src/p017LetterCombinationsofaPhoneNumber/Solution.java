package p017LetterCombinationsofaPhoneNumber;

import java.util.LinkedList;
import java.util.List;

public class Solution {
	final static String[] keyboard = new String[] { " ", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz" };

	public List<String> letterCombinations(String digits) {
		List<String> res = new LinkedList<>();
		if (digits == null || digits.length() < 1) {
			//System.err.println("test");
			return res;
		}
		res.add("");
		for (int i = 0; i < digits.length(); i++) {
			List<String> temp = new LinkedList<>();
			int ind = (int) digits.charAt(i) - '0';
			for (String k : res) {
				for (int j = 0; j < keyboard[ind].length(); j++) {
					char ch = keyboard[ind].charAt(j);
					temp.add(k + ch);
				}
			}
			res = temp;
		}
		return res;
	}

	public static void main(String[] args) {
//		for (int i = 0; i < keyboard.length; i++) {
//			System.out.println(i + "[" + keyboard[i] + "]");
//		}
		List<String> ans = new Solution().letterCombinations("");
		for (String i : ans) {
			System.out.println("[" + i + "]");
		}
		System.err.println("".length());
	}
}