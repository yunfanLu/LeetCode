# -*- coding: utf-8 -*-
# @Time    : 2018/8/14 14:19
# @Author  : yunfan


"""
题目描述
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
* 用公式做
"""

class Solution:
    def jumpFloorII(self, number):
        a = [0]
        for i in range(1, number + 1):
            t = sum(a) + 1
            a.append(t)
        return a[number]