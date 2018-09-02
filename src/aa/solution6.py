# -*- coding: utf-8 -*-
# @Time    : 2018/9/2 22:10
# @Author  : yunfan

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """

        def dfs(root, cnt, sum):
            if root is None:
                return False
            if cnt > sum:
                return False
            if (root.right is None) and (root.left is None):
                if cnt + root.val == sum:
                    return True
                else:
                    return False
            return dfs(root.left, cnt + root.val, sum) or dfs(root.right, cnt + root.val, sum)

        return dfs(root, 0, sum)

"""
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
"""

if __name__ == '__main__':
    n5 = TreeNode(5)
    n4 = TreeNode(4)
    n11 = TreeNode(11)
    n7 = TreeNode(7)
    n2 = TreeNode(2)
    n8 = TreeNode(8)
    n13 = TreeNode(13)
    n4 = TreeNode(4)
    n1 = TreeNode(1)

    n5.left = n4
    n5.right = n8
    n4.left = n11
    n11.left = n7
    n11.right = n2
    n8.left = n13
    n8.right = n4
    n4.right = n1

    print(Solution().hasPathSum(n5, 22))