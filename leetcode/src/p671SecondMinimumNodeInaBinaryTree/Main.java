package p671SecondMinimumNodeInaBinaryTree;

import java.util.Map;
import java.util.TreeMap;

/**
 * Definition for a binary tree node.
 */

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int x) {
        val = x;
    }
}

class Solution {
    private void bar(int t, int[] r){
        if (t > r[1]){
            return;
        }else if (t < r[1] && t > r[0]){
            r[1] = t;
        }else{
            r[1] = r[0];
            r[0] = t;
        }
    }

    private void bfs(TreeNode root, int[] map){
        if (root.left != null && root.right != null){
            bar(Integer.min(root.left.val, root.right.val), map);
            bfs(root.left, map);
            bfs(root.right, map);
        }else{
            bar(root.val, map);
        }
    }

    public int findSecondMinimumValue(TreeNode root) {
        int[] fir_sec = new int[]{Integer.MAX_VALUE, Integer.MAX_VALUE};
        bfs(root, fir_sec);
        return fir_sec[1];
    }
}

public class Main {

}