# -*- coding: utf-8 -*-
# @Time    : 05/02/2018 22:12
# @Author  : yunfan

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stk = []
        for ch in s:
            if len(stk) > 0 and (
                    (ch == '}' and stk[-1] == '{') or\
                    (ch == ']' and stk[-1] == '[') or\
                    (ch == ')' and stk[-1] == '(')
                ):
                stk.pop()
            else:
                stk.append(ch)
        if len(stk) == 0: return True
        return False

if __name__ == '__main__':
    s = Solution()