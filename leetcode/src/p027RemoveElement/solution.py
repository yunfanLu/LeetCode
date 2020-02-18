# -*- coding: utf-8 -*-
# @Time    : 2018/8/31 10:47
# @Author  : yunfan

class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        l, r = 0, 0
        while r < len(nums):
            if nums[r] == val:
                r += 1
            else:
                if l != r:
                    nums[l] = nums[r]
                l += 1
                r += 1
        return l