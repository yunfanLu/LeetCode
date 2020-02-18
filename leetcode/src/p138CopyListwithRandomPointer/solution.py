# -*- coding: utf-8 -*-
# @Time    : 2018/8/29 16:04
# @Author  : yunfan

# Definition for singly-linked list with a random pointer.

class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head is None:
            return

        node = head
        while node is not None:
            new_node = RandomListNode(node.label)
            new_node.next = node.next
            node.next = new_node
            node = node.next.next
        node = head
        while node is not None:
            cp_node = node.next
            if node.random is not None:
                cp_node.random = node.random.next
            node = node.next.next

        node = head
        res_node = head.next
        while True:
            cp_node = node.next
            if cp_node.next is None:
                node.next = None
                break
            node.next = cp_node.next
            node = node.next
            cp_node.next = node.next
        return res_node


def to_string(node):
    res = ''
    while node is not None:
        res += ' {}[{}]'.format(node.label, id(node))
        if node.random is not None:
            res += '(' + node.random.label + ')'
        node = node.next
    return res


if __name__ == '__main__':
    a1 = RandomListNode(1)
    a2 = RandomListNode(2)

    a1.next = a2

    b = Solution().copyRandomList(a1)
    print(to_string(a1))
    print(to_string(b))
