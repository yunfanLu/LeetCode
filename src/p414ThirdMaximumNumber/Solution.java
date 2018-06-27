package p414ThirdMaximumNumber;

import java.util.Arrays;
public class Solution {
	class SortedList{
		int[] array;
		int size;
		int ind;
		public SortedList(int size) {
			this.size = size;
			this.array = new int[size];
			this.ind = 0;
		}
		public void put(int foo){
			{
				for(int i = 0; i < ind; i ++){
					if(array[i] == foo) return;
				}
			}
				
			if(ind == size){
				if(array[ind - 1] > foo) return;
				array[ind - 1] = foo;
			}else{
				array[ind] = foo;
				ind ++;
			}
			for(int i = ind - 1; i > 0; i --){
				if(array[i - 1] < array[i]){
					int t = array[i];
					array[i] = array[i - 1];
					array[i - 1] = t;
				}else{
					break;
				}
			}
		}
		@Override
		public String toString() {
			return "ind : " + ind + ", " + Arrays.toString(this.array);
		}
	}
	
	public int thirdMax(int[] nums){
		int res = 0;
		SortedList s = new SortedList(3);
		for(int i = 0; i < nums.length; i ++){
			s.put(nums[i]);
		}
//		System.out.println(s.toString());
		if(s.ind == 3)res = s.array[2];
		else res = s.array[0];
		
		return res;
	}
	public static void main(String[] args) {
		//[1,2,2,5,3,5]
		System.out.println(new Solution().thirdMax(new int[]{1,2,2,5,3,5}));
	}
}
