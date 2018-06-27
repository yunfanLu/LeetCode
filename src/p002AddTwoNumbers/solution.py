"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        head = None
        tag = 0
        while l1 is not None or l2 is not None or tag != 0:
            sum3 = 0
            if l1 is not None:
                sum3 += l1.val
                l1 = l1.next
            if l2 is not None:
                sum3 += l2.val
                l2 = l2.next
            sum3 += tag
            x = sum3 % 10
            tag = sum3 // 10
            if head is None:
                head = ListNode(x)
                ind = head
            else:
                ind.next = ListNode(x)
                ind = ind.next
        return head
