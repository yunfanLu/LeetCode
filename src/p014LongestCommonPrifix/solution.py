# -*- coding: utf-8 -*-
# @Time    : 2018/8/30 14:31
# @Author  : yunfan

class _TireNode:

    def __init__(self, ):
        self.dic = {}
        self.cnt = 0


class _Tire:

    def __init__(self):
        self.root = _TireNode()
        self.cnt_str = 0

    def insert(self, s):
        self.cnt_str += 1
        node = self.root
        for ch in s:
            if ch not in node.dic.keys():
                node.dic[ch] = _TireNode()
            node.cnt += 1
            node = node.dic[ch]

    def prefix(self):
        res = ""
        node = self.root
        while len(node.dic) == 1 and (node.cnt == self.cnt_str):
            for ch in node.dic.keys():
                res += ch
                node = node.dic[ch]
        return res


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        tire = _Tire()
        for s in strs:
            tire.insert(s)
        return tire.prefix()


if __name__ == '__main__':
    print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))
    print(Solution().longestCommonPrefix(["", "b"]))
    print(Solution().longestCommonPrefix(["bb", "b"]))
