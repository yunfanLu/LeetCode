class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        csum = 0
        max_val = -1e12
        for num in nums:
            if csum > 0:
                csum += num
            else:
                csum = num
            max_val = max(max_val, csum)
        return max_val

s = Solution()
print(s.maxSubArray([1,2,3]))