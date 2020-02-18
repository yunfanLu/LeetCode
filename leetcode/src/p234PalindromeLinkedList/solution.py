# -*- coding: utf-8 -*-
# @Time    : 2018/8/29 14:12
# @Author  : yunfan

'''
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def _length_list(self, node):
        res = 0
        while node is not None:
            node = node.next
            res += 1
        return res

    def _forward(self, head, steps):
        node = head
        for i in range(1, steps):
            node = node.next
        return node

    def _reverse(self, prev_node):
        node = prev_node.next
        if (node is None) or (node.next is None):
            return
        while node.next is not None:
            a = node.next
            node.next = a.next
            a.next = prev_node.next
            prev_node.next = a


    def _is_same(self, a, b):
        while True:
            if (a is None) or (b is None):
                return True
            else:
                if a.val == b.val:
                    a = a.next
                    b = b.next
                else:
                    return False

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return True
        list_len = self._length_list(head)
        mid_index = (list_len // 2) + (list_len % 2)
        mid_node = self._forward(head, mid_index)
        self._reverse(mid_node)
        return self._is_same(head, mid_node.next)
#
# def to_string(node):
#     res = ''
#     while node is not None:
#         res += ' ' + str(node.val)
#         node = node.next
#     return res
#
# if __name__ == '__main__':
#     a1 = ListNode(1)
#     a2 = ListNode(2)
#     a3 = ListNode(2)
#     a4 = ListNode(1)
#
#     a1.next = a2
#     a2.next = a3
#     a3.next = a4
#
#     print(to_string(a1))
#     print(Solution().isPalindrome(a1))













