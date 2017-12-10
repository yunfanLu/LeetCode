package p027RemoveElement;

import java.util.Arrays;

public class Solution {
	public int removeElement(int[] nums, int val) {
		if (nums == null || nums.length < 1)
			return 0;

		int len = nums.length;
		int res = 0;
		int ind = 0;

		while (ind < len) {
			while (res < len && nums[res] != val) {
				res++;
			}
			ind = res + 1;
			while (ind < len && nums[ind] == val) {
				ind++;
			}
			if (res >= len || ind >= len)
				break;
			nums[res] = nums[ind];
			nums[ind] = val;

			res++;
			ind++;
		}

		return res;
	}

	public static void main(String[] args) {
		int[] ns = new int[] { 1, 2, 3, 3, 3, 3, 4, 4, 4, 3, 3, 3 };
		System.out.println(new Solution().removeElement(ns, 3));
		System.out.println(Arrays.toString(ns));
	}
}