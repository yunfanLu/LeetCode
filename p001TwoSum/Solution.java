package p001TwoSum;

import java.util.Arrays;
import java.util.HashMap;

public class Solution {

	
	public static void main(String[] args) {
		int[] nums = new int[]{0,2,4,0};
		int tag = 0;
		System.out.println(Arrays.toString(nums));
		int[] ans = twoSum(nums, tag);
	}

	////因为可能出现重复的数字，所以每次加入的时候就判断。
	//[0,4,2,0] 0
	public static int[] twoSum(int[] nums, int tag) {
		int l = 0;
		int r = 0;
		HashMap<Integer, Integer> valIndex = new HashMap<>();
		for(int i = 0; i < nums.length; i ++){
			if(valIndex.containsKey(tag - nums[i])){
				l = valIndex.get(tag - nums[i]);
				r = i;
				break;
			}
			valIndex.put(nums[i], i);
		}
		return new int[]{l, r};
	}
}
