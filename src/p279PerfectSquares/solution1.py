# -*- coding: utf-8 -*-
# @Time    : 2018/8/31 19:40
# @Author  : yunfan

class Solution:

    def _get_sqrnum_list(self, n):
        res = []
        for i in range(1, n + 1):
            tmp = i * i
            if tmp <= n:
                res.append(tmp)
            else:
                break
        return res


    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        used = {}
        sqr_list = self._get_sqrnum_list(n)
        queue = [n]
        cnt = 1
        while True:
            size = len(queue)
            for i in range(size):
                tmp = queue[i]
                for sqr in sqr_list:
                    if sqr > tmp:
                        break
                    else:
                        foo = tmp - sqr
                        if foo == 0:
                            return cnt
                        if foo not in used.keys():
                            used[foo] = True
                            queue.append(foo)
            cnt += 1

if __name__ == '__main__':
    ss = Solution()
    print(ss.numSquares(4))
    print(ss.numSquares(1))
    print(ss.numSquares(6))
    print(ss.numSquares(8))
    print(ss.numSquares(9))
    print(ss.numSquares(13))
    print(ss.numSquares(12))
    print(ss.numSquares(0))