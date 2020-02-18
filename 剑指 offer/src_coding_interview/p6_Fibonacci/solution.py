# -*- coding: utf-8 -*-
# @Time    : 2018/8/14 14:13
# @Author  : yunfan

"""
题目描述
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
n<=39
"""

class Solution:
    def __init__(self):
        self.fib = [0, 1]
        for _ in range(40):
            self.fib.append(self.fib[-1] + self.fib[-2])

    def Fibonacci(self, n):
        if n >=0 and n < len(self.fib):
            return self.fib[n]
        return 0