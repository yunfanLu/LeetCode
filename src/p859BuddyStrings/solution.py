# -*- coding: utf-8 -*-
# @Time    : 2018/7/7 14:24
# @Author  : yunfan

"""
Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B.
Example 1:
Input: A = "ab", B = "ba"
Output: true
Example 2:
Input: A = "ab", B = "ab"
Output: false
Example 3:
Input: A = "aa", B = "aa"
Output: true
Example 4:
Input: A = "aaaaaaabc", B = "aaaaaaacb"
Output: true
Example 5:
Input: A = "", B = "aa"
Output: false
Note:
0 <= A.length <= 20000
0 <= B.length <= 20000
A and B consist only of lowercase letters.
"""


class Solution:
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if A is None or B is None:
            return False
        a_l, b_l = len(A), len(B)
        if a_l != b_l:
            return False

        not_same = []
        for i in range(a_l):
            if A[i] != B[i]:
                not_same.append(i)

        if len(not_same) == 2:
            x, y = not_same
            if A[x] == B[y] and B[x] == A[y]:
                return True

        if len(not_same) == 0:
            for i in range(min(a_l, 27)):
                for j in range(i + 1, min(a_l, 27)):
                    if A[i] == A[j]:
                        return True
        return False

if __name__ == '__main__':
    print(Solution().buddyStrings("ab","ca"))