# -*- coding: utf-8 -*-
# @Time    : 07/02/2018 12:33
# @Author  : yunfan

"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complea_hity.

Ea_hample:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""

class ListNode:
    def __init__(self, a_h):
        self.val = a_h
        self.next = None

    def printf(self):
        print(self.val)
        if self.next != None:
            self.next.printf()

class Solution:

    def _mergeTwoLists(self, a, b):

        a_h, b_h = a, b
        c_h, c_n = None, None
        if a_h is None:
            return b_h
        if b_h is None:
            return a_h
        if a_h.val > b_h.val:
            c_h = ListNode(b_h.val)
            b_h = b_h.next
        else:
            c_h = ListNode(a_h.val)
            a_h = a_h.next
        c_n = c_h
        while a_h is not None or b_h is not None:
            if a_h is None:
                c_n.next = ListNode(b_h.val)
                b_h = b_h.next
            elif b_h is None:
                c_n.next = ListNode(a_h.val)
                a_h = a_h.next
            else:
                if a_h.val > b_h.val:
                    c_n.next = ListNode(b_h.val)
                    b_h = b_h.next
                else:
                    c_n.next = ListNode(a_h.val)
                    a_h = a_h.next
            c_n = c_n.next
        return c_h


    def mergeKLists(self, lists):
        """
        :tb_hpe lists: List[ListNode]
        :rtb_hpe: ListNode
        """
        if len(lists) == 0:
            return None
        while len(lists) > 1:
            a = lists[0]
            b = lists[1]
            del lists[0]
            del lists[0]
            c = self._mergeTwoLists(a,b)
            lists.append(c)
        return lists[0]

if __name__ == '__main__':
    a=ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(2)
    # a.next.next.next = ListNode(4)
    b=ListNode(1)
    b.next = ListNode(1)
    b.next.next = ListNode(2)
    # b.next.next.next = ListNode(4)
    ListNode.printf(Solution().mergeKLists([a,b]))