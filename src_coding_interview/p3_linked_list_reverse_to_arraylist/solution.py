# -*- coding: utf-8 -*-
# @Time    : 2018/8/14 12:37
# @Author  : yunfan

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        """
        :param listNode: ListNode
        :return: list
        """
        res = []
        if listNode is None:
            return res
        while listNode is not None:
            res.append(listNode.val)
            listNode = listNode.next
        res.reverse()
        return res

if __name__ == '__main__':
    l = ListNode(1)
    l.next = ListNode(2)
    l.next.next = ListNode(3)
    l.next.next.next = ListNode(4)
    print(Solution().printListFromTailToHead(l))