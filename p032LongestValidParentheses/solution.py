# -*- coding: utf-8 -*-
# @Time    : 04/01/2018 15:05
# @Author  : yunfan

'''
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
'''


class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = ['1']
        ans = 0
        for c in s:
            stack.append(c)
            while len(stack) >= 2 and stack[-1] == ')' and stack[-2] == '(':
                ans += 2
                stack.pop()
                stack.pop()
        return ans

s = Solution()
print(s.longestValidParentheses('(()'))
