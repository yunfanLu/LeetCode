package tmp;

import java.util.ArrayList;

public class Solution {

    int[] as = new int[]{0, 1, 6, 8, 9};

    private boolean check(ArrayList<Integer> nums, int N){
        long ans = 0;
        for(int num: nums){
            ans *= 10;
            ans += (long) num;
        }
        long T = (long) N;
        return ans > T;
    }

    private boolean llsame(ArrayList<Integer> nums){
        int N = nums.size();
        int j = 0;
        for (int i = N - 1; i >= 0; i --, j ++){
            int t = nums.get(i);
            int o = t;
            if(t == 9){
                o = 6;
            }else if (t == 6){
                o = 9;
            }
            int r = nums.get(j);
            if (r != o) {
                return false;
            }
        }
        return true;
    }

    private int dfs(ArrayList<Integer> nums, int N) {
        int i = 1;
        if (nums.size() > 0) {
            i = 0;
        }

        if (check(nums, N) || nums.size() > 10){
            return 0;
        }

        int ans = 0;
        for (; i < as.length; i ++){
            int o = as[i];
            nums.add(o);
            if (check(nums, N)){
                nums.remove(nums.size() - 1);
                break;
            }
            if (!llsame(nums)){
                ans += 1;
            }
            ans += dfs(nums, N);
            nums.remove(nums.size() - 1);
        }
        return ans;
    }


    public int confusingNumberII(int N) {
        ArrayList<Integer> nums = new ArrayList<Integer>();
        int ans = dfs(nums, N);
        return ans;
    }

    public static void main(String[] args){
        System.out.println(Integer.MAX_VALUE);
        Solution s = new Solution();
        System.out.println(s.confusingNumberII(20));
        System.out.println(s.confusingNumberII(100));
        System.out.println(s.confusingNumberII(1000000000));
    }
}