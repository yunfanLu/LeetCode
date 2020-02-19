package p448findAllNumbersDisappearedInAnArray;

import java.util.LinkedList;
import java.util.List;

public class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        List<Integer> ans = new LinkedList<>();
        for (int i = 0; i < nums.length; i ++){
            int ind = Math.abs(nums[i]) - 1;
            nums[ind] = - Math.abs(nums[ind]);
        }
        for (int i = 0; i < nums.length; i ++){
            if (nums[i] > 0){
                ans.add(i + 1);
            }
        }
        return ans;
    }
}
