# -*- coding: utf-8 -*-
# @Time    : 2018/8/31 10:16
# @Author  : yunfan

class Solution1:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        s.reverse()
        res = ''
        for ch in s:
            res += ch
        return res

class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]

print(Solution().reverseString("A man, a plan, a canal: Panama"))