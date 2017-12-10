package p026RemoveDuplicatesfromSortedArray;

import java.util.Arrays;

public class Solution {
    public int removeDuplicates(int[] nums) {
    	if(nums.length < 1) return 0;
    	
    	int res = 1;
    	for(int j = 1; j < nums.length; j ++){
    		if(nums[j] != nums[res - 1]){
    			nums[res] = nums[j];
    			res ++;
    		}
    	}
    	return res;
    }
    public static void main(String[] args) {
		int[] a = new int[5];
		for(int i = 0; i < 5; i ++){
			a[i] = (int)(Math.random() * 3);
		}
		Arrays.sort(a);
		System.out.println(Arrays.toString(a));
		System.out.println(new Solution().removeDuplicates(a));
		System.out.println(Arrays.toString(a));	
	}
}