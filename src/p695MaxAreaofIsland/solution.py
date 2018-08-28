"""
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:
[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.

种子染点法，唯一需要注意的是
这里遍历的写法是
for i in range(4):
    nx, ny = x + tx[i], y + ty[i]
而不是
for dx in tx:
    for dy in ty:
        nx, ny = x + dx, y + dy
第一种写法是上下上下左右，第二种写法是周围8个点。
"""

tx = [-1, 1, 0, 0]
ty = [0, 0, 1, -1]


class Solution:

    def _dfs(self, grid, x, y, n, m, index):
        """
        :param grid: List[List[int]]
        :param x: int
        :param y: int
        :param n: int
        :param m: int
        :param index: int
        :return: void
        """
        if grid[x][y] == 1:
            grid[x][y] = index
            for i in range(4):
                nx, ny = x + tx[i], y + ty[i]
                if nx >= 0 and nx < n and ny >= 0 and ny < m:
                    self._dfs(grid, nx, ny, n, m, index)

    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return 0
        n, m = len(grid), len(grid[0])
        index = 2
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    self._dfs(grid, i, j, n, m, index)
                    index += 1
        print('-'*10)
        for i in grid:
            print(i)
        print('-'*10)

        count = [0 for i in range(index + 1)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] >= 2:
                    count[grid[i][j]] += 1
        print(count)
        ans = 0
        for i in count:
            ans = max(i, ans)
        return ans


def main():
    a = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
         [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
         [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    # a = [[0,1],[1,0]]
    print(Solution().maxAreaOfIsland(a))


if __name__ == '__main__':
    main()
