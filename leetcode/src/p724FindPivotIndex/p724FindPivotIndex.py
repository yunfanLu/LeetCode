# -*- coding: utf-8 -*-
# @Time    : 2018/8/29 19:20
# @Author  : yunfan

class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum_nums = sum(nums)
        flag = 0
        for i in range(len(nums)):
            if flag * 2 + nums[i] == sum_nums:
                return i
            else:
                flag += nums[i]
        return -1