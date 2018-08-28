# -*- coding: utf-8 -*-
# @Time    : 2018/8/14 11:07
# @Author  : yunfan

"""
题目描述
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
[
[1,2,3,4],
[2,3,4,5],
[3,4,5,6],
[6,7,8,9]
]

解题的坑点：
* 对于递增和严格递增的理解
* 对于边界情况，h_m, w_m 和 h_h, w_h 之间的约束
* 对于异常情况的处理。[[],[],[]]
"""


class Solution:

    def _find_in_sorted_2d_array(self, tar, arr, h_m, w_m, h_h, w_h):
        h_c = (h_m + h_h) // 2
        w_c = (w_m + w_h) // 2
        cmp = arr[h_c][w_c]
        if h_m > h_h or w_m > w_h:
            return False
        if h_m == h_h and w_m == w_h and tar != cmp:
                return False
        if tar == cmp:
            return True
        elif tar > cmp:
            return self._find_in_sorted_2d_array(tar, arr, h_c + 1, w_c + 1, h_h, w_h) or \
                   self._find_in_sorted_2d_array(tar, arr, h_c + 1, w_m, h_h, w_c) or \
                   self._find_in_sorted_2d_array(tar, arr, h_m ,w_c + 1, h_c, w_h)
        elif tar < cmp:
            return self._find_in_sorted_2d_array(tar, arr, h_m, w_m, h_c - 1, w_c - 1) or \
                   self._find_in_sorted_2d_array(tar, arr, h_c, w_m, h_h, w_c - 1) or \
                   self._find_in_sorted_2d_array(tar, arr, h_m, w_c, h_c - 1, w_h)

    def Find(self, target, array):
        """
        :param target: int
        :param array: 2d arrays
        :return: bool, target exit in array
        """
        if array is None or len(array) < 1 or len(array[0]) < 1:
            return False
        h, w = len(array), len(array[0])
        return self._find_in_sorted_2d_array(target, array, 0, 0, h - 1, w - 1)

def test():
    t = 7
    # a = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
    a = [[]]
    print(Solution().Find(t, a))

if __name__ == '__main__':
    test()