package p029DivideTwoIntegers;

public class Solution {
    public int divide(int dividend, int divisor) {
    	if(divisor == 0){
    		if(dividend >= 0) return Integer.MAX_VALUE;
    		return Integer.MIN_VALUE;
    	}
    	if(dividend == 0) return 0;
    	if(dividend == Integer.MIN_VALUE && divisor == -1) return Integer.MAX_VALUE;

    	return dividend/divisor;    	
    }
    
    public static void main(String[] args) {
    	System.out.println(new Solution().divide(-2147483648, -1));
    }
}