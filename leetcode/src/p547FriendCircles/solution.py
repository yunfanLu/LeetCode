# -*- coding: utf-8 -*-
# @Time    : 2018/8/28 18:43
# @Author  : yunfan

"""
There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature.
For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C.
And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1,
then the ith and jth students are direct friends with each other, otherwise not.
And you have to output the total number of friend circles among all the students.

Example 1:
Input:
[[1,1,0],
 [1,1,0],
 [0,0,1]]
Output: 2
Explanation:The 0th and 1st students are direct friends, so they are in a friend circle.
The 2nd student himself is in a friend circle. So return 2.
Example 2:
Input:
[[1,1,0],
 [1,1,1],
 [0,1,1]]
Output: 1
Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends,
so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.
Note:
N is in range [1,200].
M[i][i] = 1 for all students.
If M[i][j] = 1, then M[j][i] = 1.

这道题可以采用并查集做，也可以用搜索做。
"""


class UnionFindSet:
    def __init__(self, N):
        self.N = N
        self.par = [i for i in range(N)]
        self.rank = [0 for i in range(N)]

    def find(self, x):
        if x == self.par[x]:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if self.rank[x] == self.rank[y]:
            self.par[x] = y
            self.rank[y] += 1
        elif self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def count_circles(self):
        root_set = dict()
        for i in range(self.N):
            root = self.find(i)
            root_set[root] = 1
        return len(root_set)


class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if len(M) == 0:
            return 0
        N = len(M)
        ufset = UnionFindSet(N)
        for i in range(N):
            for j in range(N):
                if M[i][j] == 1:
                    ufset.union(i, j)
        return ufset.count_circles()


if __name__ == '__main__':
    a = [[1, 1, 0],
         [1, 1, 0],
         [0, 0, 1]]
    print(Solution().findCircleNum(a))
