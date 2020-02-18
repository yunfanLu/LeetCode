# -*- coding: utf-8 -*-
# @Time    : 2018/9/5 08:10
# @Author  : yunfan

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def _dfs(self, node, res):
        if node is not None:
            self._dfs(node.left, res)
            res.append(node.val)
            self._dfs(node.right, res)

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self._dfs(root, res)
        return res
