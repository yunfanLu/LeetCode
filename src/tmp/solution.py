# -*- coding: utf-8 -*-
# @Time    : 2018/7/7 21:06
# @Author  : yunfan

class Solution1(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        l = []
        dominoes = list('#' + dominoes + "#")
        last = 0
        for i in range(1, len(dominoes)):
            if dominoes[i] != '.':
                l.append((last, dominoes[last], i, dominoes[i]))
                last = i
        for i in l:
            l_ind, ch1, r_ind, ch2 = i
            if ch1 == "#":
                if ch2 == 'L':
                    for j in range(l_ind + 1, r_ind):
                        dominoes[j] = 'L'
            elif ch1 == "L":
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


# .L.R...LR..L..
# 12345678901234

class Solution(object):
    def new21Game(self, N, K, W):
        """
        :type N: int
        :type K: int
        :type W: int
        :rtype: float
        """
        a = [0 for i in range(K + W + 1)]
        b = [0 for i in range(K + W + 1)]
        for i in range(W + 1):
            a[i] = 1
        for _i in range(K):
            for i in range(K):
                if a[i] != 0:
                    for j in range(1, W + 1):
                        b[a[i] + j] += a[i]
            a = b
            b = [0 for i in range(K + W)]
        sum = 0
        for i in range(K, K + W):
            sum += a[i]
        cnt = 0
        for i in range(K, N + 1):
            cnt += a[i]
        return cnt / sum

if __name__ == '__main__':
    print(Solution().new21Game(10,1,10))
    print(Solution().new21Game(6,1,10))
    print(Solution().new21Game(27,17,10))