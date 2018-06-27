# -*- coding: utf-8 -*-
# @Time    : 07/02/2018 12:33
# @Author  : yunfan

# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def mergeTwoLists(self, a, b):
        a_f, a_n = a, a.next
        b_f, b_n = b, b.next
        # res =
        # while a.next is not None and b.next is not None:


    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
