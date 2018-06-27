# -*- coding: utf-8 -*-
# @Time    : 30/12/2017 19:58
# @Author  : yunfan

class Solution:
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_length = 20001
        a = [0 for i in range(max_length)]
        for num in nums:
            a[num] += 1
        dp = [[0 for i in range(2)] for j in range(max_length)]
        dp[0][1] = a[0]
        for i in range(1, max_length):
            dp[i][0] = max(dp[i - 1])
            dp[i][1] = max(dp[i - 2]) + i * a[i]
        return max(dp[max_length - 1])

s = Solution()
print(s.deleteAndEarn([3, 4, 2]))
print(s.deleteAndEarn([2, 2, 3, 3, 3, 4]))