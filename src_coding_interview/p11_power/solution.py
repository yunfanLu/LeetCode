# -*- coding: utf-8 -*-
# @Time    : 2018/8/14 15:21
# @Author  : yunfan

'''
题目描述
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
'''

class Solution:
    def Power(self, base, exponent):
        '''
        base ^ exponent = 1. / (base ^ (exponent * -1))
        :param base: float
        :param exponent: int
        :return: base ^ exponent
        '''
        if exponent < 0:
            return 1. / self.Power(base, - exponent)
        elif exponent == 0:
            return 1
        else:
            if exponent == 1:
                return base
            elif exponent == 2:
                return base * base
            elif exponent % 2 == 0:
                t = self.Power(base, exponent//2)
                return t * t
            else:
                t = self.Power(base, exponent // 2)
                return t * t * base

if __name__ == '__main__':
    print(Solution().Power(3, 2))
    print(Solution().Power(3, -2))