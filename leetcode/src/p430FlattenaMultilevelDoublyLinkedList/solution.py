# -*- coding: utf-8 -*-
# @Time    : 2018/8/29 15:34
# @Author  : yunfan

"""
# Definition for a Node.

"""

class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution(object):

    def _flatten(self, head):
        if head is None:
            return None, None
        a, b = self._flatten(head.child)
        c, d = self._flatten(head.next)
        head.child = None
        if (a is not None) and (c is not None):
            a.prev = head
            b.next = c
            a.prev.next = a
            b.next.prev = b
            return head, d
        elif (a is not None) and (c is None):
            a.prev = head
            a.prev.next = a
            return head, b
        elif (a is None) and (c is not None):
            c.prev = head
            c.prev.next = c
            return head, d
        else:
            return head, head

    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        return self._flatten(head)[0]
