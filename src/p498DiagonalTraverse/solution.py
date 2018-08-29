# -*- coding: utf-8 -*-
# @Time    : 2018/8/29 21:34
# @Author  : yunfan

class Solution:
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if (matrix is None) or len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        N, M = len(matrix), len(matrix[0])
        diagonal_list = []
        for y in range(0, M):
            dig = []
            x = 0
            while y >= 0 and x < N:
                dig.append(matrix[x][y])
                x += 1
                y -= 1
            diagonal_list.append(dig)
        for x in range(1, N):
            dig = []
            y = M - 1
            while y >= 0 and x < N:
                dig.append(matrix[x][y])
                x += 1
                y -= 1
            diagonal_list.append(dig)
        res = []
        for i in range(len(diagonal_list)):
            if i % 2 == 0:
                diagonal_list[i].reverse()
            res += diagonal_list[i]
        return res

a = [
    [1,2,3],
    [1,2,3],
    [1,2,3],
    [1,2,3],
]
print(Solution().findDiagonalOrder(a))