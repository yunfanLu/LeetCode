# -*- coding: utf-8 -*-
# @Time    : 2018/7/4 00:24
# @Author  : yunfan

"""
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
Note 1:
The input string length won't exceed 1000.
Note 2:
palindromic substrings, "aba" is and "abc" not
"""


class Solution:
    def _is_palindromic(self, s):
        return s == s[::-1]

    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        s_len = len(s)
        for i in range(s_len):
            for j in range(i + 1, s_len + 1):
                sub_s = s[i:j]
                res += self._is_palindromic(sub_s)
                print(sub_s, " , ", res)
        return res

if __name__ == '__main__':
    print(Solution().countSubstrings("abc"))
    print(Solution().countSubstrings("aaa"))
