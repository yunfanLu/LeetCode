# -*- coding: utf-8 -*-
# @Time    : 04/01/2018 15:37
# @Author  : yunfan

class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums)
        while l < r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid
            else:
                l = mid + 1
        return r


s = Solution()
print(s.searchInsert([1,3], 2))
