# -*- coding: utf-8 -*-
# @Time    : 04/01/2018 15:05
# @Author  : yunfan

'''
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
'''


class Solution:
    class Node:
        def __init__(self, ind, ch):
            self.ind = ind
            self.ch = ch

        def __str__(self):
            return 'ind : ' + str(self.ind) + ' , ch : ' + ch

    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack_in = []
        for i in range(len(s)):
            stack_in.append(self.Node(i, s[i]))

        stack = []
        for i in stack_in:
            if len(stack) >= 1 and stack[-1].ch == '(' and i.ch == ')':
                # stack.pop(index=-1)
                del (stack[-1])
            else:
                stack.append(i)

        if len(stack) == 0: return len(s)
        ans = 0
        for i in range(len(stack)):
            if i == 0:
                ans = max(ans, stack[i].ind - 0)
            else:
                ans = max(ans, stack[i].ind - stack[i - 1].ind - 1)
        ans = max(ans, len(stack_in) - stack[-1].ind - 1)

        return ans


s = Solution()
print(s.longestValidParentheses('(()())((()'))
print(s.longestValidParentheses('()'))
print(s.longestValidParentheses('()(()()'))
print(s.longestValidParentheses(')())())(((((((('))
