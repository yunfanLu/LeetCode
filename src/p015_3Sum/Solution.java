package p015_3Sum;

import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;

public class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> res = new LinkedList();
        int len = nums.length;
        
        HashMap<Integer, HashMap<Integer, Boolean>> numSet = new HashMap<>();
        for(int i = 0; i < len; i ++){
        	if(numSet.get(nums[i]) == null){
        		numSet.put(nums[i], new HashMap<>());
        	}
        	numSet.get(nums[i]).put(i, true);
        }
        
        for(int i = 0; i < len; i ++){
        	for(int j = i + 1; j < len; j ++){
        		int t = - nums[i] - nums[j] ;
        		if(numSet.get(t) == null) continue;
        		HashMap<Integer, Boolean> indSet = numSet.get(t);
        		int count = 0;
        		for(int r : indSet.keySet()){
        			if(r > i && r > j){
        				count ++;
        				List<Integer> temp = new LinkedList<>();
        				temp.add(nums[i]);
        				temp.add(nums[j]);
        				temp.add(nums[r]);
        				res.add(temp);
        				break;
        			}
        		}
        	}
        }
        return res;
    }
    
    public static void main(String[] args) {
		int[] nums = {-1, 0, 1, 2, -1, -4};
		List<List<Integer>> ans = new Solution().threeSum(nums);
		for(List<Integer> i:ans){
			for(int j:i){
				System.out.print(j + ", ");
			}
			System.out.println();
		}
    }
}