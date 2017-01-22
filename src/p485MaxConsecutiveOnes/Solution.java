package p485MaxConsecutiveOnes;

public class Solution {

	public int findMaxConsecutiveOnes(int[] nums) {
		int res = 0;
		int tmp = 0;
		for(int i = 0; i < nums.length; i ++){
			if(nums[i] == 1){
				tmp ++;
				res = Math.max(res, tmp);
			}else{
				tmp = 0;
			}
		}
		return res;
	}

	public static void main(String[] args) {
		System.out.println(new Solution().findMaxConsecutiveOnes(new int[]{1,1,0,1,1,1}));
	}

}
