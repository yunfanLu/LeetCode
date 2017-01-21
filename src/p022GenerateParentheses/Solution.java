package p022GenerateParentheses;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class Solution {
	public List<String> generateParenthesis(int n) {
		List<String> res = new ArrayList<>();
		if(n <= 0) return res;
		gao(res,"",n,n);
		return res;
	}
	private void gao(List<String> res, String string, int l, int r) {
		if(l == 0 && r == 0){
			res.add(string);
			return;
		}
		if(l > 0){
			gao(res, string + "(", l - 1, r);
		}
		if(r > 0 && l < r){
			gao(res, string + ")", l, r - 1);
		}
	}
	public static void main(String[] args) {
		List<String> ans = new Solution().generateParenthesis(2);
		System.out.println("ans_hash : " + ans);
		System.out.println(ans);
	}
}