package p001TwoSum;

import java.util.Arrays;
import java.util.Random;

public class FindTwo {
	/**
	 * @param nums
	 * @param tag
	 * @return
	 * nums is a ascending order arrays, we can define two indexs l inital 0 and r inital nums.lengths - 1, which is the latest number in the array.
	 * than define sum is summation of nums[l] and nums[r], if sum  is smaller than tag, l plus one, else the r  reduce one.
	 */
	public static int[] FindTwoNum(int[] nums,int tag){
		int l = 0;
		int r = nums.length - 1;
		while(l < r){
			int temp = nums[l] + nums[r];
			if(temp < tag) l ++;
			else if(temp > tag) r --;
			else break;
		}
		return new int[]{l, r};
	}
	public static void main(String[] args) {
		final int maxN = 100;
		int[] nums = new int[maxN];
		for(int i = 0; i < maxN; i ++) nums[i] = (int) (Math.random() * (1 << 10));
		Arrays.sort(nums);
		System.out.println(Arrays.toString(nums));
		int tag = nums[maxN/2] + nums[maxN/2 + 1];
		System.out.println(Arrays.toString(FindTwoNum(nums, tag)));
	}
}
