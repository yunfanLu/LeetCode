# -*- coding: utf-8 -*-
# @Time    : 06/01/2018 19:49
# @Author  : yunfan

class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        try:
            float(s)
            return True
        except:
            return False


s = Solution()
print(s.isNumber('123'))
print(s.isNumber('1.23'))
print(s.isNumber('1e3'))
print(s.isNumber('1ea'))
