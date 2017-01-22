package p492ConstructTheRectangle;

import java.util.Arrays;

public class Solution {
    public int[] constructRectangle(int area) {
    	int[] r = new int[2];
    	r[0] = (int)(Math.sqrt(area*1.0) + 1);
    	while(true){
    		r[1] = area / r[0];
    		if(r[0] * r[1] == area) break;
    		r[0] --;
    	}
    	if(r[0] < r[1]){
    		int t = r[0];
    		r[0] = r[1];
    		r[1] = t;
    	}
    	return r;
    }
    public static void main(String[] args) {
		for(int i = 0; i < 10; i ++){
			int a = (int) (Math.random() * 100);
			System.out.println(a + ", " + Arrays.toString(new Solution().constructRectangle(a)));
		}
	}    
}