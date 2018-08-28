# -*- coding: utf-8 -*-
# @Time    : 2018/8/14 14:17
# @Author  : yunfan

"""
题目描述
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
"""

class Solution:
    def jumpFloor(self, number):
        a = [0,1,2]
        for _ in range(number):
            a.append(a[-1] + a[-2])
        return a[number]