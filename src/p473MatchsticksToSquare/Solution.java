package p473MatchsticksToSquare;

import java.util.Arrays;

/**
 * Created by onion on 2017/2/26.
 */
public class Solution {
    public boolean makesquare(int[] nums) {
        if (nums == null || nums.length < 4) return false;

        /**
         * 排序后这里有一个剪枝！就是如果当期的大了，那么直接返回 false。
         */

        Arrays.sort(nums);
        long sum = 0;
        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];
        }
        if (sum % 4 != 0) return false;

        long[] sums = new long[4];
        return dfs(nums, sums, sum / 4, 0);
    }

    private boolean dfs(int[] nums, long[] sums, long len, int ind) {
        if (ind == nums.length) {
            if (sums[0] == len && sums[1] == len && sums[2] == len) {
                return true;
            } else {
                return false;
            }
        }
        for (int i = 0; i < 4; i++) {
            if (sums[i] + nums[ind] <= len) {
                sums[i] += nums[ind];
                if (dfs(nums, sums, len, ind + 1) == true) {
                    return true;
                }
                sums[i] -= nums[ind];
            } else {
                return false;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        int[][] nums = new int[][]{
                {1, 1, 2, 2, 2},
                {1, 1, 1, 1},
                {1, 2, 3, 3, 2, 1, 1, 2, 3, 3, 2, 1},
                {5, 5, 5, 5, 16, 4, 4, 4, 4, 4, 3, 3, 3, 3, 4},
                {8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 60},
                {}
        };
        Solution t = new Solution();
        for (int i = 0; i < nums.length; i++) {
            System.out.println(t.makesquare(nums[i]));
        }
    }
}