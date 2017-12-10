package p101SymmetricTree;

/**
 * Created by onion on 2017/3/1.
 */
//Definition for a binary tree node.
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int x) {
        val = x;
    }
}

public class Solution {
    public boolean isSymmetric(TreeNode root) {
        if (root == null) return true;
        return isSymmetric(root.left, root.right);
    }

    private boolean isSymmetric(TreeNode l, TreeNode r) {
        if (l == null && r == null) return true;
        if (l == null || r == null) return false;
        if(l.val != r.val) return false;
        return isSymmetric(l.left, r.right) && isSymmetric(l.right, r.left);
    }
}