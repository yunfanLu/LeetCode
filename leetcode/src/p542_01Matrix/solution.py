# -*- coding: utf-8 -*-
# @Time    : 2018/9/5 08:48
# @Author  : yunfan

'''
Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.
Example 1:
Input:

0 0 0
0 1 0
0 0 0
Output:
0 0 0
0 1 0
0 0 0
Example 2:
Input:

0 0 0
0 1 0
1 1 1
Output:
0 0 0
0 1 0
1 2 1
Note:
The number of elements of the given matrix will not exceed 10,000.
There are at least one 0 in the given matrix.
The cells are adjacent in only four directions: up, down, left and right.
'''

INF = 123456789
tx = [0, 1, 0, -1]
ty = [1, 0, -1, 0]


class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if (matrix is None) or (len(matrix) == 0) or (len(matrix[0]) == 0):
            return None
        N, M = len(matrix), len(matrix[0])
        res = [[INF for i in range(M)] for j in range(N)]
        queue = []
        for i in range(N):
            for j in range(M):
                if matrix[i][j] == 1:
                    flag = False
                    for k in range(4):
                        x, y = i + tx[k], j + ty[k]
                        if x >= 0 and x < N and y >= 0 and y < M and matrix[x][y] == 0:
                            flag = True
                            break
                    if flag:
                        res[i][j] = 1
                        queue.append((i, j))
                else:
                    res[i][j] = 0
        while queue:
            size = len(queue)
            x, y = queue.pop()
            for i in range(4):
                dx, dy = x + tx[i], y + ty[i]
                if dx >= 0 and dx < N and dy >= 0 and dy < M and res[dx][dy] == INF:
                    res[dx][dy] = res[x][y] + 1
                    queue.append((dx, dy))
        return res








