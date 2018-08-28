# -*- coding: utf-8 -*-
# @Time    : 2018/8/14 13:21
# @Author  : yunfan

"""
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 输入一个非减排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。 NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
"""


class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if rotateArray is None or len(rotateArray) == 0:
            return 0
        l, r = 0, len(rotateArray) - 1
        while r > l:
            m = (l + r) // 2
            if rotateArray[m] > rotateArray[l]:
                l = m
            if rotateArray[m] < rotateArray[r]:
                r = m


if __name__ == '__main__':
    print(Solution().minNumberInRotateArray([3, 1, 2]))
    print(Solution().minNumberInRotateArray([1]))
    print(Solution().minNumberInRotateArray([2, 1]))
    print(Solution().minNumberInRotateArray([2, 3, 0, 1, 1]))
