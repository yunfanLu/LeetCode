# -*- coding: utf-8 -*-
# @Time    : 2018/8/29 13:09
# @Author  : yunfan

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        super_head = ListNode(-1)
        super_head.next = head
        a, b = super_head, head
        while b is not None:
            while (b is not None) and b.val == val:
                a.next = b.next
                b = b.next
            if b is not None:
                a, b = a.next, b.next
        return super_head.next