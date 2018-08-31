# -*- coding: utf-8 -*-
# @Time    : 2018/8/31 11:00
# @Author  : yunfan

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, 0
        res = 0
        while r < len(nums):
            if nums[r] == 1:
                if r > 0 and nums[r - 1] != 1:
                    l = r
                res = max(res, r - l + 1)
            r += 1
        return res