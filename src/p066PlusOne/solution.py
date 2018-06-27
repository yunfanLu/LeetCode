"""
66. Plus One

Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
"""


class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits.reverse()
        tag = 1
        for i in range(len(digits)):
            tag = digits[i] + tag
            digits[i] = tag % 10
            tag //= 10
        if tag != 0:
            digits.append(tag)
        digits.reverse()
        return digits

if __name__ == '__main__':
    print(Solution().plusOne([1, 2, 3]))
    print(Solution().plusOne([9, 9, 9]))
