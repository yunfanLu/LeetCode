package p513FindBottomLeftTreeValue;

import java.util.LinkedList;
import java.util.Queue;

/**
 * Created by onion on 2017/2/26.
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
    public int findBottomLeftValue(TreeNode root) {
        if(root == null) return -1;
        LinkedList<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        int ans = root.val;
        while (queue.isEmpty() == false) {
            ans = queue.getFirst().val;
            int size = queue.size();
            for(int i = 0; i < size; i ++){
                TreeNode node = queue.poll();
                if(node.left != null) queue.offer(node.left);
                if(node.right != null) queue.offer(node.right);
            }
        }
        return ans;
    }

    public static void main(String[] args){
        TreeNode node = new TreeNode(0);
        node.right = new TreeNode(1);
        node.left = new TreeNode(2);
        node.left.left = new TreeNode(3);
        System.out.print(new Solution().findBottomLeftValue(node));
    }
}
