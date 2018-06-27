package p199BinaryTreeRightSideView;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

/**
 * Created by onion on 2017/3/4.
 */


class TreeNode {
    int val;
    TreeNode right;
    TreeNode left;
    TreeNode(int x) {
        val = x;
    }
}

public class Solution {
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> res = new ArrayList<>();

        LinkedList<TreeNode> queue = new LinkedList<>();
        if (root != null) queue.add(root);
        while (queue.isEmpty() == false) {
            res.add(queue.getLast().val);
            int size = queue.size();
            for (int i = 0; i < size; i++){
                TreeNode node = queue.poll();
                if(node.left != null) queue.add(node.left);
                if(node.right != null) queue.add(node.right);
            }
        }

        return res;
    }
}