# -*- coding: utf-8 -*-
# @Time    : 2018/7/4 00:56
# @Author  : yunfan

"""
Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.
"""


class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                a = i
                j = a - 1
                while j >= 0 and nums[j] == nums[a]:
                        a = j
                        j -= 1
                break
        b = -1
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] < nums[i - 1]:
                b = i
                j = b + 1
                while j < len(nums) and nums[j] == nums[b]:
                        b = j
                        j += 1

                break
        print("a {}, b {}".format(a, b))
        return b - a + 1


if __name__ == '__main__':
    # [2, 6, 4, 8, 10, 9, 15]
    # [1, 2, 3]
    # print(Solution().findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))
    # print(Solution().findUnsortedSubarray([1, 2, 3]))
    print(Solution().findUnsortedSubarray([1,2,4,5,3]))
