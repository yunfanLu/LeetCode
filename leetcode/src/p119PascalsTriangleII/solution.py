# -*- coding: utf-8 -*-
# @Time    : 2018/8/31 13:10
# @Author  : yunfan

class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        b = [1, 1]
        for i in range(1, rowIndex):
            c = [1]
            for j in range(1, len(b)):
                c.append(b[j] + b[j - 1])
            c.append(1)
            b = c
        return b