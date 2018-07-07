# -*- coding: utf-8 -*-
# @Time    : 2018/7/7 20:04
# @Author  : yunfan

class Solution:
    def shortestSubarray(self, A, K):
        import collections
        from itertools import accumulate

        A_sum = [0] + list(accumulate(A))

        ret = len(A) + 1
        idx_checking = collections.deque()
        for idx, val in enumerate(A_sum):
            # removing from right to left if the right value is less than val
            # this keeps the deque decreasing
            while idx_checking and val < A_sum[idx_checking[-1]]:
                idx_checking.pop()

            # removing from left to right if the condition satisfied
            while idx_checking and val - A_sum[idx_checking[0]] >= K:
                ret = min(ret, idx - idx_checking.popleft())

            idx_checking.append(idx)

        return ret if ret < len(A) + 1 else -1


if __name__ == '__main__':
    print(Solution().shortestSubarray([2, 1], 3))
