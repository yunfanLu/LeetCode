package p021MergeTwoSortedLists;

public class ListNode {
	int val;
	ListNode next;

	ListNode(int x) {
		val = x;
	}
	
	@Override
	public String toString() {
		String res = "[";
		ListNode i = this;
		while(i != null){
			res += i.val;
			res += ", ";
			i = i.next;
		}
		res += "]";
		return res;
	}
}