# -*- coding: utf-8 -*-
# @Time    : 2018/8/29 19:33
# @Author  : yunfan

class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_val = max(nums)
        for it in nums:
            if it != max_val and it * 2 > max_val:
                return -1
        return nums.index(max_val)

if __name__ == '__main__':
    print(Solution().dominantIndex([3,6]))