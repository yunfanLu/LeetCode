# -*- coding: utf-8 -*-
# @Time    : 2018/8/29 12:51
# @Author  : yunfan

'''
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        new_head = head
        while head.next is not None:
            node = head.next
            head.next = node.next
            node.next = new_head
            new_head = node
        return new_head


def to_string(node):
    res = ''
    while node is not None:
        res += ' ' + str(node.val)
        node = node.next
    return res


if __name__ == '__main__':
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n1.next = n2
    n2.next = n3

    print(to_string(n1))
    n1 = Solution().reverseList(n1)
    print(to_string(n1))
