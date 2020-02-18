# -*- coding: utf-8 -*-
# @Time    : 2018/8/31 13:11
# @Author  : yunfan

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        ls = s.split(' ')
        ls.reverse()
        res = ''
        for i in range(len(ls)):
            if len(ls[i]) > 0 and ls[i] != ' ':
                if len(res) > 0:
                    res += ' '
                res += ls[i]
        return res

if __name__ == '__main__':
    print(Solution().reverseWords('ab cd'))
    print(Solution().reverseWords('ab       cd'))
    print('\'', Solution().reverseWords('      '), '\'')
    print('\'{}\''.format(Solution().reverseWords('      ')))
