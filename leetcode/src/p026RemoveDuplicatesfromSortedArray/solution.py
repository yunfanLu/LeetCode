# -*- coding: utf-8 -*-
# @Time    : 2018/8/31 13:51
# @Author  : yunfan

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        l, r = 0, 1
        while r < len(nums):
            if nums[r] != nums[l]:
                l += 1
                nums[l] = nums[r]
            r += 1
        return l + 1