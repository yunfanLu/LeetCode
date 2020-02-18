package p454_4SumII;

import java.util.HashMap;

/**
 * Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that
 * A[i] + B[j] + C[k] + D[l] is zero.
 * To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500.
 * All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.
 * Example:
 * Input:
 * A = [ 1, 2]
 * B = [-2,-1]
 * C = [-1, 2]
 * D = [ 0, 2]
 * Output:
 * 2
 * Explanation:
 * The two tuples are:
 * 1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
 * 2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
 */
class Solution {
    public static void main(String[] args) {
        int[] A = {1, 2};
        int[] B = {-2, -1};
        int[] C = {-1, 2};
        int[] D = {0, 2};
        System.out.print(new Solution().fourSumCount(A, B, C, D));
    }

    public int fourSumCount(int[] A, int[] B, int[] C, int[] D) {
        HashMap<Integer, Integer> sumAB = new HashMap<>();
        for (int a : A) {
            for (int b : B) {
                int tmp = a + b;
                sumAB.put(tmp, sumAB.getOrDefault(tmp, 0) + 1);
//                if (sumAB.containsKey(tmp)) {
//                    sumAB.put(tmp, sumAB.get(tmp) + 1);
//                } else {
//                    sumAB.put(tmp, 1);
//                }
            }
        }

        int ans = 0;
        for (int c : C) {
            for (int d : D) {
                int tmp = -(c + d);
                if (sumAB.containsKey(tmp)) {
                    ans += sumAB.get(tmp);
                }
            }
        }
        return ans;
    }
}

