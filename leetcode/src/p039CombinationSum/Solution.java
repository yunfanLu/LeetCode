package p039CombinationSum;

import java.util.ArrayList;
import java.util.List;

class Solution {
    public static void main(String[] args) {
        System.out.print("hello world");
        Solution slu = new Solution();
        System.out.println(slu.combinationSum(new int[]{2, 3, 4}, 8));
    }

    private void gao(int[] candidates, int target, int ind, List<Integer> tmp, List<List<Integer>> ans) {
        if (target == 0) {
            ans.add(tmp);
            return;
        } else {
            if(ind == candidates.length){

            }
        }
    }

    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> ans = new ArrayList<>();
        List<Integer> tmp = new ArrayList<>();
        gao(candidates, target, 1, tmp, ans);
        return null;
    }
}