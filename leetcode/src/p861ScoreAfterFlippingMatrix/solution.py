# -*- coding: utf-8 -*-
# @Time    : 2018/7/7 15:02
# @Author  : yunfan

"""
We have a two dimensional matrix A where each value is 0 or 1.
A move consists of choosing any row or column, and toggling each value in that row or column: changing all 0s to 1s, and all 1s to 0s.
After making any number of moves, every row of this matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.
Return the highest possible score.

Example 1:

Input: [
[0,0,1,1],
[1,0,1,0],
[1,1,0,0]]

Output: 39

Explanation:
Toggled to [
[1,1,1,1],
[1,0,0,1],
[1,1,1,1]].
0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39

Note:
1 <= A.length <= 20
1 <= A[0].length <= 20
A[i][j] is 0 or 1.
"""


class Solution:
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        if A is None or len(A) == 0:
            return 0
        n, m = len(A), len(A[0])
        for i in range(n):
            if A[i][0] == 0:
                for j in range(m):
                    A[i][j] = (A[i][j] + 1) % 2
        res = 0
        for j in range(m):
            cnt = 0
            for i in range(n):
                cnt += A[i][j]
            res *= 2
            res += max(cnt, n - cnt)
        return res

if __name__ == '__main__':
    print(Solution().matrixScore([
        [0,0,1,1],
        [1,0,1,0],
        [1,1,0,0]]))