package p021MergeTwoSortedLists;

public class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode res = new ListNode(-1);
        ListNode temp = res;
        while(l1 != null || l2 != null){
        	int v1 = Integer.MAX_VALUE;
        	int v2 = Integer.MAX_VALUE;
        	
        	if(l1 != null) v1 = l1.val;
        	if(l2 != null) v2 = l2.val;
        	
        	if(v1 < v2){
        		temp.next = new ListNode(l1.val);
        		l1 = l1.next;
        	}else{
        		temp.next = new ListNode(l2.val);
        		l2 = l2.next;
        	}
        	temp = temp.next;
        }
        return res.next;
    }
    public static void main(String[] args) {
    	ListNode l1 = new ListNode(0);
		ListNode temp = l1;
		for (int i = 1; i < 10; i++) {
			temp.next = new ListNode((int)(Math.random()*100.0));
			temp = temp.next;
		}
		ListNode l2 = new ListNode(10);
		temp = l2;
		for(int i = 1; i < 14; i ++){
			temp.next = new ListNode((int)(Math.random()*100.0));
			temp = temp.next;
		}
		ListNode ans = new Solution().mergeTwoLists(l1, l2);
		System.out.println(l1.toString());
		System.out.println(l2.toString());
		System.out.println(ans.toString());
	}
}