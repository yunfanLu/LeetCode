package p098ValidateBinarySearchTree;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by onion on 2017/3/3.
 */


class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int x) {
        val = x;
    }
}

public class Solution {
    public boolean isValidBST(TreeNode root) {
        ArrayList<Integer> headInMide = new ArrayList<>();
        fird(root,headInMide);
        for(int i = 1; i < headInMide.size(); i ++){
            if(headInMide.get(i) <= headInMide.get(i - 1)) return false;
        }
        return true;
    }

    private void fird(TreeNode root, List<Integer> headInMide) {
        if(root == null) return;
        fird(root.left, headInMide);
        headInMide.add(root.val);
        fird(root.right, headInMide);
    }
}