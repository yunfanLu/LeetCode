package p538ConvertBstToGreaterTree;


import java.util.LinkedList;
import java.util.List;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int x) {
        val = x;
    }
}

class Solution {

    int add = 0;
    public TreeNode convertBST(TreeNode root) {
        if (root == null){
            return root;
        }
        convertBST(root.right);
        root.val += add;
        add += root.val;
        convertBST(root.left);
        return root;
    }
}