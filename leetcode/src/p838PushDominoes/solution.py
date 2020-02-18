# -*- coding: utf-8 -*-
# @Time    : 2018/7/7 22:39
# @Author  : yunfan

"""
There are N dominoes in a line, and we place each domino vertically upright.
In the beginning, we simultaneously push some of the dominoes either to the left or to the right.
After each second, each domino that is falling to the left pushes the adjacent domino on the left.
Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.
When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.
For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.
Given a string "S" representing the initial state. S[i] = 'L', if the i-th domino has been pushed to the left; S[i] = 'R', if the i-th domino has been pushed to the right; S[i] = '.', if the i-th domino has not been pushed.
Return a string representing the final state.

Example 1:
Input: ".L.R...LR..L.."
Output: "LL.RR.LLRRLL.."
Example 2:

Input: "RR.L"
Output: "RR.L"
Explanation: The first domino expends no additional force on the second domino.
Note:

0 <= N <= 10^5
String dominoes contains only 'L', 'R' and '.'
"""


class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        l = []
        dominoes = list('L' + dominoes + "R")
        last = 0
        for i in range(1, len(dominoes)):
            if dominoes[i] != '.':
                l.append((last, dominoes[last], i, dominoes[i]))
                last = i
        for i in l:
            l_ind, ch1, r_ind, ch2 = i
            if ch1 == "L":
                if ch2 == 'L':
                    for j in range(l_ind, r_ind):
                        dominoes[j] = 'L'
            elif ch1 == 'R':
                if ch2 == 'L':
                    mid_ind = l_ind + (r_ind - l_ind + 1) // 2
                    has_mid = (r_ind - l_ind + 1) % 2
                    for j in range(l_ind + 1, mid_ind):
                        dominoes[j] = 'R'
                    for j in range(mid_ind + has_mid, r_ind):
                        dominoes[j] = 'L'
                else:
                    for j in range(l_ind, r_ind):
                        dominoes[j] = 'R'
        return "".join(dominoes[1:-1])
# LL.RR.LLRRLL..
# LL.RR.LLRRLL..
# .L.R...LR..L..
# 12345678901234

if __name__ == '__main__':
    print(Solution().pushDominoes(".L.R...LR..L.."))
    print(Solution().pushDominoes("R..L"))
    print(Solution().pushDominoes("R...L"))