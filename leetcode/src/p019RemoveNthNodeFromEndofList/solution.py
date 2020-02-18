# -*- coding: utf-8 -*-
# @Time    : 2018/8/29 11:23
# @Author  : yunfan

'''
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def _length(self, head):
        res = 0
        while head is not None:
            head = head.next
            res += 1
        return res

    def _forward_steps(self, head, steps):
        if steps < 0:
            return None
        for i in range(0, steps):
            head = head.next
        return head

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if n <= 0:
            return
        list_len = self._length(head)
        if list_len == n:
            head = head.next
        elif list_len > n:
            node_prev = self._forward_steps(head, list_len - n - 1)
            node = node_prev.next
            if node is not None:
                node_prev.next = node.next
            node.next = None
        return head


def print_list_node(node):
    res = ''
    while node is not None:
        res += ' ' + str(node.val)
        node = node.next
    return res

if __name__ == '__main__':
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)
    n6 = ListNode(6)
    n7 = ListNode(7)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = n7

    print(print_list_node(n1))
    n1 = Solution().removeNthFromEnd(n1, 7)
    print(print_list_node(n1))


