/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

class Solution {
    public static void main(String[] args) {
        Solution s = new Solution();
        s.buildTree(new int[]{3, 9, 20, 15, 7}, new int[]{9, 3, 15, 20, 7});
    }

    private int indexof(int[] list, int tag) {
        for (int i = 0; i < list.length; i++) {
            if (list[i] == tag) {
                return i;
            }
        }
        return -1;
    }

    private int[] split(int[] list, int begin, int end) {
        int length = end - begin + 1;
        int[] res = new int[length];
        for (int i = 0; i < length; i++) {
            res[i] = list[i + begin];
        }
        return res;
    }

    public TreeNode buildTree(int[] preorder, int[] inorder) {
        if (preorder.length < 1){
            return null;
        }
        if (preorder.length == 1 && inorder.length == 1) {
            return new TreeNode(preorder[0]);
        }
        int left_len = indexof(inorder, preorder[0]);
        int[] preleft = split(preorder, 1, left_len);
        int[] preright = split(preorder, 1 + left_len, preorder.length - 1);
        int[] inleft = split(inorder, 0, left_len - 1);
        int[] inright = split(inorder, left_len + 1, inorder.length - 1);
        TreeNode root = new TreeNode(preorder[0]);
        root.left = buildTree(preleft, inleft);
        root.right = buildTree(preright, inright);
        return root;
    }
}