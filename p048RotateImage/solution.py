# -*- coding: utf-8 -*-
# @Time    : 06/01/2018 19:11
# @Author  : yunfan

'''
Example 1:

Given input matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
Example 2:

Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
],

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
'''


class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anythsing, modify matrix in-place instead.
        """
        print('*matrix[::-1]' , *matrix[::-1])
        matrix[::] = zip(*matrix[::-1])


s = Solution()
a = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
s.rotate(a)
# print(a)

a = [
    [5, 1, 9, 11],
    [2, 4, 8, 10],
    [13, 3, 6, 7],
    [15, 14, 12, 16]
]
s.rotate(a)
# print(a)
