# -*- coding: utf-8 -*-
# @Time    : 2018/6/26 21:57
# @Author  : yunfan

"""
Given a string, find the length of the longest substring without repeating characters.
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i, j = 0, 0
        len_s = len(s)
        is_in = {}
        ans = 0
        while j < len_s:
            if (s[j] not in is_in) or (is_in[s[j]] == 0):
                is_in[s[j]] = 1
                ans = max(ans, j - i + 1)
            else:
                while i < j:
                    if s[i] != s[j]:
                        is_in[s[i]] = 0
                        i += 1
                    else:
                        i += 1
                        break
            j += 1
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))
    print(s.lengthOfLongestSubstring("bbbbb"))
    print(s.lengthOfLongestSubstring("tmmzuxt"))