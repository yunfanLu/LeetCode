# -*- coding: utf-8 -*-
# @Time    : 2018/8/29 22:01
# @Author  : yunfan

'''
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
'''

class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if (matrix is None) or (len(matrix) == 0) or (len(matrix[0]) == 0):
            return []
        N, M = len(matrix), len(matrix[0])
        used = [[0 for i in range(M)] for j in range(N)]
        x, y = 0, 0
        res = []
        for _ in range(N * M):
            while y < M and used[x][y] == 0:
                res.append(matrix[x][y])
                used[x][y] = 1
                y += 1
            y -= 1
            x += 1
            while x < N and used[x][y] == 0:
                res.append(matrix[x][y])
                used[x][y] = 1
                x += 1
            x -= 1
            y -= 1
            while y >= 0 and used[x][y] == 0:
                res.append(matrix[x][y])
                used[x][y] = 1
                y -= 1
            y += 1
            x -= 1
            while x >= 0 and used[x][y] == 0:
                res.append(matrix[x][y])
                used[x][y] = 1
                x -= 1
            x += 1
            y += 1
        return res
