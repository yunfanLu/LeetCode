# -*- coding: utf-8 -*-
# @Time    : 2018/8/30 14:52
# @Author  : yunfan

class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        try:
            i = haystack.index(needle)
            return i
        except:
            return -1

print(Solution().strStr('12','2'))
print(Solution().strStr('12','3'))
print(Solution().strStr('12',''))