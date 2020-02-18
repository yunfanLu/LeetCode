# -*- coding: utf-8 -*-
# @Time    : 2018/9/1 10:17
# @Author  : yunfan


class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for i in tokens:
            if i not in ['+', '-', '*', '/']:
                stack.append(int(i))
            else:
                a, b = stack.pop(), stack.pop()
                if i == "+":
                    c = b + a
                elif i == '-':
                    c = b - a
                elif i == '*':
                    c = b * a
                else:
                    c = int(b / a)
                stack.append(c)
        return stack[0]


if __name__ == '__main__':
    print(Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
