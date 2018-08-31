# -*- coding: utf-8 -*-
# @Time    : 2018/8/31 10:33
# @Author  : yunfan

class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, len(numbers) - 1
        while l < r:
            flag = numbers[l] + numbers[r]
            if flag < target:
                l += 1
            elif flag > target:
                r -= 1
            else:
                return l + 1, r + 1
        return -1, -1