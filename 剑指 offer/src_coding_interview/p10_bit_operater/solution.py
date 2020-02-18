# -*- coding: utf-8 -*-
# @Time    : 2018/8/14 15:13
# @Author  : yunfan

'''
题目描述
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
'''

class Solution:
    def NumberOf1(self, n):
        if n < 0:
            n = 2 ** 32 + n
        bin_n = str(bin(n))
        # print(bin_n)
        return bin_n[2:].count('1')

if __name__ == '__main__':
    print(Solution().NumberOf1(10))
    print(Solution().NumberOf1(-10))
    print(Solution().NumberOf1(-2147483648))