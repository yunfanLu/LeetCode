# -*- coding: utf-8 -*-
# @Time    : 2018/6/28 18:13
# @Author  : yunfan

"""
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
"""


class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        a = list(s)
        s = a[:]
        a.reverse()
        for i in range(len(a)):
            if a[i] == s[i]:
                continue
            else:
                a1 = a[:i] + a[i + 1:]
                s1 = s[:len(a) - i - 1] + s[len(a) - i:]

                s2 = s[:i] + s[i + 1:]
                a2 = a[:len(a) - i - 1] + a[len(a) - i:]
                if a1 == s1 or a2 == s2:
                    return True
                else:
                    return False
        return True


if __name__ == '__main__':
    print(Solution().validPalindrome("ebcbbececabbacecbbcbe"))
