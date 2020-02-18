# -*- coding: utf-8 -*-
# @Time    : 2018/8/29 14:52
# @Author  : yunfan

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(-1)
        ind = head
        while True:
            if l1 is None:
                ind.next = l2
            if l2 is None:
                ind.next = l1
            if (l1 is None) or (l2 is None):
                break
            if l1.val < l2.val:
                node = l1
                l1 = l1.next
            else:
                node = l2
                l2 = l2.next
            ind.next = node
            ind = ind.next
        return head.next











