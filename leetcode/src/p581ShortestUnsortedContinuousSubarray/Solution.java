package p581ShortestUnsortedContinuousSubarray;

import java.util.Stack;

class Solution {
    public int findUnsortedSubarray(int[] nums) {
        Stack<Integer> stack = new Stack<>();

        int l = nums.length;
        int r = 0;
        for (int i = 0; i < nums.length; i++) {
            if (stack.isEmpty() || (nums[stack.peek()] <= nums[i])) {
                stack.push(i);
            } else {
                int ind = 0;
                while ((!stack.isEmpty()) && (nums[stack.peek()] > nums[i])) {
                    ind = stack.pop();
                }
                l = Math.min(l, ind);
                stack.push(i);
            }
        }
        stack.clear();

        for (int i = nums.length - 1; i >= 0; i--) {
            if (stack.isEmpty() || (nums[stack.peek()] >= nums[i])) {
                stack.push(i);
            } else {
                int ind = nums.length;
                while ((!stack.isEmpty()) && (nums[stack.peek()] < nums[i])) {
                    ind = stack.pop();
                }
                r = Math.max(r, ind);
                stack.push(i);
            }
        }

        return Math.max(r - l + 1, 0);
    }

    public static void main(String[] args){
        int[] a = {2, 6, 4, 8, 10, 9, 15};
        System.out.println(new Solution().findUnsortedSubarray(a));
    }
}