package p494TargetSum;

public class Solution {
    public int findTargetSumWays(int[] nums, int S) {
    	int res = 0;
    	if(nums.length < 1) return res;
    	if(nums.length == 1){
    		if(nums[0] == S) res ++;
    		if(nums[0] == -S) res ++;
    		return res;
    	}
    	res += gao(nums, S - nums[0], 1);
    	res += gao(nums, S + nums[0], 1);
    	return res;
    }
    
    private int gao(int[] nums, int i, int j) {
		int res = 0;
		if(j == nums.length - 1){
			if(i + nums[j] == 0) res ++;
			if(i - nums[j] == 0) res ++;
			return res;
		}
		res += gao(nums, i + nums[j], j + 1);
		res += gao(nums, i - nums[j], j + 1);
		return res;
	}

	public static void main(String[] args) {
		int[] nums = new int[]{1};
		int S = 1;
		long begin = System.currentTimeMillis();
		System.out.println(new Solution().findTargetSumWays(nums, S));
		long end = System.currentTimeMillis();
		System.out.println(end - begin + " ms");
	}
}

class Solution2 {
    private int dfs(int[] nums, int ind, int S){
        if(ind == nums.length){
            if(S == 0){
                return 1;
            }else{
                return 0;
            }
        }
        int res = 0;
        res += dfs(nums, ind + 1, S + nums[ind]);
        res += dfs(nums, ind + 1, S - nums[ind]);
        return res;
    }

    public int findTargetSumWays(int[] nums, int S) {
        return dfs(nums, 0, S);
    }
}