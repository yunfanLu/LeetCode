package p42TrappingRainWater;

/**
 * Created by onion on 2017/3/1.
 */
public class Solution {
    public int trap(int[] height) {
        if(height == null || height.length == 0) return 0;
        int N = height.length;
        int[] l = new int[N];
        int[] r = new int[N];

        l[0] = 0;
        for (int i = 1; i < N; i++) {
            l[i] = Math.max(l[i - 1], height[i - 1]);
        }

        r[N - 1] = 0;
        for (int i = N - 2; i >= 0; i--) {
            r[i] = Math.max(r[i + 1], height[i + 1]);
        }

        int res = 0;
        for (int i = 0; i < N; i++) {
            int val = Math.min(l[i], r[i]) - height[i];
            val = Math.max(val, 0);

            res += val;
        }

        return res;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.print(s.trap(new int[]{0,1,0,2,1,0,1,3,2,1,2,1}));
    }
}