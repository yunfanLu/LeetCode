# -*- coding: utf-8 -*-
# @Time    : 2018/8/29 10:50
# @Author  : yunfan

"""
Write a program to find the node at which the intersection of two singly linked lists begins.
For example, the following two linked lists:
A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3
begin to intersect at node c1.

Notes:
If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
Credits:
Special thanks to @stellari for adding this problem and creating all test cases.
"""

# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def _length_node(self, head):
        res = 0
        while head is not None:
            head = head.next
            res += 1
        return res

    def _forward_steps(self, node, step):
        if step < 0:
            return None
        for i in range(step):
            node = node.next
        return node

    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None

        lenA, lenB = self._length_node(headA), self._length_node(headB)
        if lenA > lenB:
            headA = self._forward_steps(headA, lenA - lenB)
        else:
            headB = self._forward_steps(headB, lenB - lenA)
        while True:
            if (headA is None) or (headB is None):
                return None
            if headA is headB:
                return headA
            headA = headA.next
            headB = headB.next



if __name__ == '__main__':
    A = ListNode(1)
    B = ListNode(2)
    # C = ListNode(3)
    # D = ListNode(4)
    # E = ListNode(5)
    #
    # A.next = B
    # B.next = D
    # C.next = D
    # D.next = E
    #
    # print(Solution().getIntersectionNode(A, B).val)

    print(Solution().getIntersectionNode(A, B))


