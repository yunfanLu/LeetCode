"""
4. Median of Two Sorted Arrays
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = nums1 + nums2
        nums.sort()
        nums_len = len(nums)
        if nums_len % 2 == 0:
            return (nums[nums_len // 2] + nums[nums_len // 2 - 1]) / 2
        else:
            return nums[nums_len // 2]


if __name__ == '__main__':
    print(Solution().findMedianSortedArrays([1, 3], []))
