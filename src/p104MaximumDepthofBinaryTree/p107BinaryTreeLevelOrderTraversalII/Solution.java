package p104MaximumDepthofBinaryTree.p107BinaryTreeLevelOrderTraversalII;


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

public class Solution {
    public List<List<Integer>> levelOrderBottom(TreeNode root) {
        List<List<Integer>> res = new LinkedList<>();

        LinkedList<TreeNode> queue = new LinkedList<>();
        if (root != null) queue.add(root);
        while (queue.isEmpty() == false) {
            int size = queue.size();
            List<Integer> foo = new LinkedList<>();
            for (int i = 0; i < size; i++) {
                TreeNode node = queue.poll();
                if(node.left != null) queue.add(node.left);
                if(node.right != null) queue.add(node.right);
                foo.add(node.val);
            }
            res.add(0,foo);
        }
        return res;
    }
}