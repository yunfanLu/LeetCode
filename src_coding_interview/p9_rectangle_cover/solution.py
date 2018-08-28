# -*- coding: utf-8 -*-
# @Time    : 2018/8/14 14:38
# @Author  : yunfan

"""
题目描述
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
"""

class Solution:
    def rectCover(self, number):
        f = [0,1,2]
        for _ in range(3, number + 1):
            f.append(f[-1] + f[-2])
        return f[number]