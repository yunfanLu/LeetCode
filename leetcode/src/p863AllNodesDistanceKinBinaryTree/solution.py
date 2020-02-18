# -*- coding: utf-8 -*-
# @Time    : 2018/7/7 15:52
# @Author  : yunfan

"""
We are given a binary tree (with root node root), a target node, and an integer value K.

Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any order.



Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2

Output: [7,4,1]

Explanation:
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.



Note that the inputs "root" and "target" are actually TreeNodes.
The descriptions of the inputs above are just serializations of these objects.


Note:

The given tree is non-empty.
Each node in the tree has unique values 0 <= node.val <= 500.
The target node is a node in the tree.
0 <= K <= 1000.

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution1:
    class TreeParentNode:
        def __init__(self, treeNode, leftTreeParentNode, righrTreeParentNode, parentTreeParentNode):
            self.node = treeNode
            self.left = leftTreeParentNode
            self.right = righrTreeParentNode
            self.parent = parentTreeParentNode

    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        treeParentRootNode = self._treeNode2ParentNode(root, None)
        self._konwParent(treeParentRootNode, None)
        targetNode = self._findTargetNode(treeParentRootNode, target)
        res = self._bfs(targetNode, None, K)
        return res

    def _bfs(self, node, fromNode, K):
        """
        :param node: TreeParentNode
        :param fromNode: TreeParentNode
        :param K: int
        :return: List[int]
        """
        if node == None:
            return []
        res = []
        if K == 0:
            return [node.node.val]
        else:
            nodeList = [node.left, node.right, node.parent]
            for iNode in nodeList:
                if iNode != None and iNode != fromNode:
                    res += self._bfs(iNode, node, K - 1)
        return res

    def _findTargetNode(self, node, taget):
        """"
        :param node: TreeParentNode
        :param taget: TreeNode
        :return: TreeParentNode
        """
        if node.node.val == taget.val:
            return node
        else:
            if node.left != None:
                left = self._findTargetNode(node.left, taget)
                if left != None:
                    return left
            if node.right != None:
                righe = self._findTargetNode(node.right, taget)
                if righe != None:
                    return righe
        return None

    def _konwParent(self, treeParentNode, parent):
        if treeParentNode == None:
            return
        treeParentNode.parent = parent
        self._konwParent(treeParentNode.left, treeParentNode)
        self._konwParent(treeParentNode.right, treeParentNode)

    def _treeNode2ParentNode(self, node, parent):
        rightTreeParentNode = None
        leftTreeParentNode = None
        if node.right != None:
            rightTreeParentNode = self._treeNode2ParentNode(node.right, None)
        if node.left != None:
            leftTreeParentNode = self._treeNode2ParentNode(node.left, None)
        root = self.TreeParentNode(node, leftTreeParentNode, rightTreeParentNode, None)
        return root


class Solution:
    def _dfs(self, node, parent):
        """
        :param node: TreeNode
        :param parent: TreeNode
        :return: void
        """
        if node is None:
            return
        node.parent = parent
        self._dfs(node.left, node)
        self._dfs(node.right, node)

    def _bfs(self, node, from_node, K):
        """
        :param node:
        :param from_node:
        :param K:
        :return:
        """
        if node is None:
            return []

        if K == 0:
            return [node.val]

        res = []
        node_list = [node.left, node.right, node.parent]
        for i_node in node_list:
            if i_node!= from_node:
                res += self._bfs(i_node, node, K - 1)
        return res

    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        root = self._dfs(root, None)
        res = self._bfs(target, None, K)
        return res


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    root.right = TreeNode(1)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)

    print(Solution().distanceK(root, root.left, 2))
