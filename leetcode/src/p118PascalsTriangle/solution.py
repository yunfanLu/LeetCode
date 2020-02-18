# -*- coding: utf-8 -*-
# @Time    : 2018/8/29 22:07
# @Author  : yunfan

class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows <= 0:
            return []
        res = [[1]]
        for i in range(1, numRows):
            a = [1]
            for j in range(1, i):
                a.append(res[i - 1][j - 1] + res[i - 1][j])
            a.append(1)
            res.append(a)
        return res