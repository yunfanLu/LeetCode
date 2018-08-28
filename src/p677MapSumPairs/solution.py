# -*- coding: utf-8 -*-
# @Time    : 2018/8/28 20:37
# @Author  : yunfan

class Node:
    def __init__(self, ch):
        self.last = False
        self.val = 0
        self.ch = ch
        self.next = {}


class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node('')

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        node = self.root
        for ch in key:
            if ch not in node.next.keys():
                node.next[ch] = Node(ch)
            node = node.next[ch]
        node.val = val

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        node = self.root
        for ch in prefix:
            if ch in node.next.keys():
                node = node.next[ch]
            else:
                return 0
        return self._count_node(node)

    def _count_node(self, node):
        res = node.val
        for ch in node.next.keys():
            res += self._count_node(node.next[ch])
        return res

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)