# -*- coding: utf-8 -*-
# @Time    : 2018/9/1 10:43
# @Author  : yunfan

class Solution(object):

    def _dfs(self, nums, ind, S):
        if ind == len(nums):
            if S == 0:
                return 1
            else:
                return 0
        res = 0
        res += self._dfs(nums, ind + 1, S + nums[ind])
        res += self._dfs(nums, ind + 1, S - nums[ind])
        return res

    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        return self._dfs(nums, 0, S)


if __name__ == '__main__':
    a = [10, 9, 6, 4, 19, 0, 41, 30, 27, 15, 14, 39, 33, 7, 34, 17, 24, 46, 2, 46]
    b = 45
    print(Solution().findTargetSumWays(a, b))