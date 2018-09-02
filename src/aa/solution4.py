# -*- coding: utf-8 -*-
# @Time    : 2018/9/2 14:25
# @Author  : yunfan

tx = [0, 0, 1, -1]
ty = [1, -1, 0, 0]


class Solution:

    def _dfs(self, image, tag, x, y, newColor):
        if image[x][y] == newColor:
            return
        image[x][y] = newColor
        for i in range(4):
            dx = x + tx[i]
            dy = y + ty[i]
            if dx >= 0 and dx < len(image) and dy >= 0 and dy < len(image[0]) and image[dx][dy] == tag:
                self._dfs(image, tag, dx, dy, newColor)

    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        if len(image) == 0 or len(image) == 0:
            return None
        self._dfs(image, image[sr][sc], sr, sc, newColor)
        return image


if __name__ == '__main__':
    a = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    print(Solution().floodFill(a, 1, 1, 2))
