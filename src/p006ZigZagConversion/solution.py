# -*- coding: utf-8 -*-
# @Time    : 28/12/2017 14:53
# @Author  : yunfan
import math


class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1: return s
        numCols = len(s)
        m = [['' for j in range(numCols)] for i in range(numRows)]

        ind, i, j = 0, 0, 0
        while ind < len(s):
            for t in range(0, numRows, 1):
                if ind < len(s):
                    m[i][j] = s[ind]
                    ind, i = ind + 1, i + 1
            i, j = i - 2, j + 1
            for t in range(numRows - 1, 1, -1):
                if ind < len(s):
                    m[i][j] = s[ind]
                    ind, i, j = ind + 1, i - 1, j + 1
        res = ''
        for i in m: res += ''.join(i)
        return res


if __name__ == '__main__':
    s = Solution()
    res = s.convert('ABC', 2)
    print(res)
