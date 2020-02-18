# -*- coding: utf-8 -*-
# @Time    : 2018/6/29 21:44
# @Author  : yunfan

"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""


class Solution:
    def __hash_str(self, str):
        sl = list(str)
        sl.sort()
        return "".join(sl)

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = []
        ind_dic = {}
        for istr in strs:
            hash_str = self.__hash_str(istr)
            if hash_str in ind_dic:
                ind = ind_dic[hash_str]
                res[ind].append(istr)
            else:
                ind = len(res)
                ind_dic[hash_str] = ind
                res.append([istr])
        return res


if __name__ == '__main__':
    print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
