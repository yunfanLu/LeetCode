# -*- coding: utf-8 -*-
# @Time    : 2018/8/31 13:38
# @Author  : yunfan

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        ls = s.split()
        return ' '.join(s[::-1] for s in ls)