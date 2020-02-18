package p002AddTwoNumbers;

/**
 * Definition for singly-linked list. public class ListNode { int val; ListNode
 * next; ListNode(int x) { val = x; } }
 */

// Definition for singly-linked list.

class ListNode {
	int val;
	ListNode next;

	ListNode(int x) {
		val = x;
	}

	public ListNode(int[] a) {
		if (a.length > 0) {
			this.val = a[0];
			ListNode end = this;
			for (int i = 1; i < a.length; i++) {
				ListNode temp = new ListNode(a[i]);
				end.next = temp;
				end = end.next;
			}
		}
	}

	@Override
	public String toString() {
		String res = "[";
		ListNode temp = this;
		while (temp != null) {
			res += temp.val;
			res += " -> ";
			temp = temp.next;
		}
		res += "null";
		return res;
	}
}

public class Solution {
	private static boolean DEBUG = true;

	public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
		ListNode head = null;
		ListNode end = null;
		ListNode l = l1;
		ListNode r = l2;
		int carry = 0;

		while (l != null || r != null) {
			int t = 0;
			if (l != null) t += l.val;
			if (r != null) t += r.val;
			t += carry;

			ListNode temp = new ListNode(t % 10);
			carry = t / 10;
			if (head == null) {
				head = temp;
				end = temp;
			} else {
				end.next = temp;
				end = temp;
			}
			if (l != null) l = l.next;
			if (r != null) r = r.next;
		}

		if (carry != 0) end.next = new ListNode(carry);
		return head;
	}

	public static void main(String[] args) {
		Solution solution = new Solution();
		solution.judge(new int[] { 1 }, new int[] { 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9 });
	}

	private void judge(int[] a1, int[] a2) {
		ListNode t = null, r = null;
		Solution solution = new Solution();

		t = new ListNode(a1);
		System.out.println(t.toString());
		r = new ListNode(a2);
		System.out.println(r.toString());

		ListNode ans = solution.addTwoNumbers(t, r);
		System.out.println(ans.toString());
	}
}