package p019RemoveNthNodeFromEndofList;

// Definition for singly-linked list.

public class Solution {
	private static boolean DEBUG = false;

	public ListNode removeNthFromEnd(ListNode head, int n) {
		ListNode newHead = new ListNode(-1);
		newHead.next = head;

		int len = 0;
		ListNode tmp = newHead;
		while (tmp.next != null) {
			tmp = tmp.next;
			len++;
		}
		
//		if (DEBUG) {
//			System.out.println("len : " + len);
//		}

		tmp = newHead;
		for (int i = 0; i < len - n; i++) {
			tmp = tmp.next;
		}
		
//		if (DEBUG) {
//			System.out.println("tmp1    : " + tmp.toString());
//		}
		
		if (tmp.next != null){
			tmp.next = tmp.next.next;
		}
		
		head = newHead.next;
//		if(DEBUG){
//			System.out.println("newHead : " + newHead.toString());
//			System.out.println("tmp2    : " + tmp.toString());
//			System.out.println("head    : " + head.toString());
//			System.out.println("head-hashcode : " +head.hashCode());
//		}
	
		return head;
	}

	public static void main(String[] args) {
		ListNode head = new ListNode(0);
		ListNode temp = head;
		for (int i = 1; i < 10; i++) {
			temp.next = new ListNode(i);
			temp = temp.next;
		}
		//head = new ListNode(1);
		System.out.println(head.toString());
		head = new Solution().removeNthFromEnd(head, 10);
		System.out.println("head-hashcode : " +head.hashCode());
		System.out.println("head    : " + head.toString());
	}
}