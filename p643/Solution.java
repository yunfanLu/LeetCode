import java.util.Queue;
import java.util.LinkedList;
import java.lang.Integer;

public class Solution {
    public double findMaxAverage(int[] nums, int k) {
        Queue<Integer> q = new LinkedList<>();
        int ans = Integer.MIN_VALUE;
        int count = 0;
        for(int t : nums){
            q.offer(t);
            count += t;
            if(q.size() > k){
                count -= q.poll();
            }
            ans = Math.max(ans,count);
        }
        return ans * 1.0 / k;
    }
}