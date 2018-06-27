# -*- coding: utf-8 -*-
# @Time    : 05/01/2018 17:52
# @Author  : yunfan

class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        ind = [-1]
        stk = []
        for i in range(len(s)):
            if len(stk) >= 1 and stk[-1] == '(' and s[i] == ')':
                del(stk[-1])
                del(ind[-1])
            else:
                stk.append(s[i])
                ind.append(i)
        ind.append(len(s))

        ans = 0
        for i in range(1, len(ind)):
            ans = max(ans, ind[i] - ind[i - 1] - 1)

        return ans

s = Solution()
print(s.longestValidParentheses('(()())((()'))
print(s.longestValidParentheses('()'))
print(s.longestValidParentheses('()(()()'))
print(s.longestValidParentheses(')())())(((((((('))

