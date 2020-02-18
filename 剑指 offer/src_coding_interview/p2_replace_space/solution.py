# -*- coding: utf-8 -*-
# @Time    : 2018/8/14 12:30
# @Author  : yunfan

"""
题目描述
请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
"""

# -*- coding:utf-8 -*-
class Solution:
    def replaceSpace(self, s):
        """
        :param s: str
        :return: str
        """
        res = s.replace(' ', '%20')
        return res