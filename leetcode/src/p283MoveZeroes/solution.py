# -*- coding: utf-8 -*-
# @Time    : 2018/8/31 14:04
# @Author  : yunfan


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                l = i
                break
        if l == -1:
            return
        for i in range(l + 1, len(nums)):
            if nums[i] != 0:
                nums[l] = nums[i]
                nums[i] = 0
                l += 1
        for i in range(l, len(nums)):
            nums[i] = 0
