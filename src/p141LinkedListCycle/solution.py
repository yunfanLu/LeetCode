# -*- coding: utf-8 -*-
# @Time    : 2018/8/29 09:50
# @Author  : yunfan

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fi, fj = head, head
        while True:
            if fi is not None:
                fi = fi.next
            if (fj is not None) and (fj.next is not None):
                fj = fj.next.next
            else:
                fj = None
            if (fi is None) or (fj is None):
                return False
            if fi is fj:
                return True

