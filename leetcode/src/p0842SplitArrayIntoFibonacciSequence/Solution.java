package p0842SplitArrayIntoFibonacciSequence;

import java.util.ArrayList;
import java.util.List;

/**
 * Given a string S of digits, such as S = "123456579", we can split it into a Fibonacci-like sequence [123, 456, 579].
 * <p>
 * Formally, a Fibonacci-like sequence is a list F of non-negative integers such that:
 * <p>
 * 0 <= F[i] <= 2^31 - 1, (that is, each integer fits a 32-bit signed integer type);
 * F.length >= 3;
 * and F[i] + F[i+1] = F[i+2] for all 0 <= i < F.length - 2.
 * Also, note that when splitting the string into pieces, each piece must not have extra leading zeroes, except if the piece is the number 0 itself.
 * <p>
 * Return any Fibonacci-like sequence split from S, or return [] if it cannot be done.
 * <p>
 * Example 1:
 * <p>
 * Input: "123456579"
 * Output: [123,456,579]
 * Example 2:
 * <p>
 * Input: "11235813"
 * Output: [1,1,2,3,5,8,13]
 * Example 3:
 * <p>
 * Input: "112358130"
 * Output: []
 * Explanation: The task is impossible.
 * Example 4:
 * <p>
 * Input: "0123"
 * Output: []
 * Explanation: Leading zeroes are not allowed, so "01", "2", "3" is not valid.
 * Example 5:
 * <p>
 * Input: "1101111"
 * Output: [110, 1, 111]
 * Explanation: The output [11, 0, 11, 11] would also be accepted.
 * Note:
 * <p>
 * 1 <= S.length <= 200
 * S contains only digits.
 */
public class Solution {
    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.splitIntoFibonacci("123456579"));
        System.out.println(s.splitIntoFibonacci("11235813"));
        System.out.println(s.splitIntoFibonacci("112358130"));
        System.out.println(s.splitIntoFibonacci("0123"));
        System.out.println(s.splitIntoFibonacci("1101111"));
    }

    private boolean dfs(String S, int i, List<Integer> ans){
        if (i == S.length() && ans.size() > 2){
            return true;
        }
        for (int j = i + 1; j <= S.length(); j ++){
            if (S.charAt(i) == '0' && j != i + 1){
                break;
            }
            long a = Long.valueOf(S.substring(i, j));
            if (a > Integer.MAX_VALUE){
                return false;
            }
            if (ans.size() < 2 || ans.get(ans.size() - 1) + ans.get(ans.size() - 2) == a ){
                ans.add((int)a);
                if (dfs(S, j, ans)){
                    return true;
                }else{
                    ans.remove(ans.size() - 1);
                }
            }
            if (ans.size() >= 2 && ans.get(ans.size() - 1) + ans.get(ans.size() - 2) < a ){
                return false;
            }
        }
        return false;
    }
    public List<Integer> splitIntoFibonacci(String S) {
        int len = S.length();
        List<Integer> ans = new ArrayList<Integer>();
        // the length must big than 3.
        if (len < 3) {
            return ans;
        }
        boolean hasans = dfs(S,0, ans);
        return ans;
    }
}