import java.util.Scanner;

public class Solution{
    public boolean checkPossibility(int[] nums) {
       int count = 0;
       for(int i = 0; i < nums.length - 1; i ++){
           if(nums[i] > nums[i + 1]){
               count ++;
           }
           if(count > 1){
               return false;
           }
       }
       return true;
    }

    public static void main(String[] args) {
        Scanner cin = new Scanner(System.in);
        int N = cin.nextInt();
        int[] nums = new int[N];
        for(int i = 0; i < N; i ++){
            nums[i] = cin.nextInt();
        }
        System.out.println(new Solution().checkPossibility(nums));
    }
}