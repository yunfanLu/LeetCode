# -*- coding: utf-8 -*-
# @Time    : 2018/8/29 16:50
# @Author  :

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def _lenght_make_circle(self, head):
        node = head
        res = 1
        while node.next is not None:
            node = node.next
            res += 1
        node.next = head
        return res

    def _forward(self, node, steps):
        for i in range(1, steps):
            node = node.next
        return node

    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return
        list_len = self._lenght_make_circle(head)
        k = k % list_len
        node = self._forward(head, list_len - k)
        res = node.next
        node.next = None
        return res
