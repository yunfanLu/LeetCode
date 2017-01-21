package p024SwapNodesInPairs;

public class Solution {
    public ListNode swapPairs(ListNode head) {
    	ListNode newhead = new ListNode(-1);
    	newhead.next = head;
    	if(head == null) return newhead.next;
    	
    	ListNode i = newhead;
    	ListNode j = i.next;
    	ListNode k = null;
    	if(j != null) k = j.next;
    	if(k == null) return newhead.next;
    	while(k != null){
    		j.next = k.next;
    		i.next = k;
    		k.next = j;
    		if(j.next == null || j.next.next == null) break;
    		i = k.next;
    		j = j.next;
    		k = j.next;
    	}
    	return newhead.next;
    }

    public static void main(String[] args) {
		ListNode list = new ListNode(0);
		ListNode temp = list;
		for(int i = 1; i < 8; i ++){
			temp.next = new ListNode(i);
			temp = temp.next;
		}
		System.out.println(list.toString());
		list = new Solution().swapPairs(list);
		System.out.println(list.toString());
		System.out.println(new Solution().swapPairs(null));
	}
}
