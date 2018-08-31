# -*- coding: utf-8 -*-
# @Time    : 2018/8/31 10:23
# @Author  : yunfan

class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return sum(nums[::2])

print(Solution().arrayPairSum([1,3,2,4]))