package p560SubarraySumEqualK;

import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;

class Solution {
    public static void main(String[] args) {
        int[] nums = {1, 1, 1};
        int k = 2;
        System.out.println(new Solution().subarraySum(nums, k));
    }

    public int subarraySum(int[] nums, int k) {
        int ans = 0;
        HashMap<Integer, List<Integer>> map = new HashMap<>();
        int sum = 0;
        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];
            if (sum == k){
                ans += 1;
            }
            int sub = sum - k;
            if (map.containsKey(sub)) {
                ans += map.get(sub).size();
            }
            if (!map.containsKey(sum)) {
                map.put(sum, new LinkedList<>());
            }
            map.get(sum).add(i);
        }
        return ans;
    }
}