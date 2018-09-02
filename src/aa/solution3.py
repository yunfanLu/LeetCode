# -*- coding: utf-8 -*-
# @Time    : 2018/9/2 13:53
# @Author  : yunfan

class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for ch in s:
            if ch == ']':
                res = ''
                while len(stack) > 0 and stack[-1] != '[':
                    res = stack.pop() + res
                stack.pop()
                cnt = ''
                while len(stack) > 0 and len(stack[-1]) <= 1 and \
                        (ord(stack[-1]) - ord('0')) < 10 and (ord(stack[-1]) - ord('0')) >= 0:
                    cnt = stack.pop() + cnt
                tmp = res * int(cnt)
                stack.append(tmp)
            else:
                stack.append(ch)
        res = ''
        for cc in stack:
            res += cc
        return res


if __name__ == '__main__':
    print(Solution().decodeString("100[leetcode]"))
    print(Solution().decodeString("2[abc]3[cd]ef"))
