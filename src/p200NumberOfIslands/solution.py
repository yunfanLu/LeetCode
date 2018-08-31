# -*- coding: utf-8 -*-
# @Time    : 2018/8/31 15:26
# @Author  : yunfan

tx = [-1, 0, 1, 0]
ty = [0, 1, 0, -1]


class Solution(object):

    def _dfs(self, grid, i, j):
        if i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]) and grid[i][j] == '1':
            grid[i][j] = '0'
            for k in range(4):
                self._dfs(grid, i + tx[k], j + ty[k])

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    res += 1
                    self._dfs(grid, i, j)
        return res