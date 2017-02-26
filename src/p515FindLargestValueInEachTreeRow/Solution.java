package p515FindLargestValueInEachTreeRow;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

import javax.management.Query;

// * Definition for a binary tree node.

class TreeNode {
	int val;
	TreeNode left;
	TreeNode right;

	TreeNode(int x) {
		val = x;
	}
}

public class Solution {
	public List<Integer> largestValues(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        Queue<TreeNode> queue = new LinkedList<>();
        
        if(root != null) queue.offer(root);
        while(queue.isEmpty() == false){
        	int max = Integer.MIN_VALUE;
        	int size = queue.size();
        	for(int i = 0; i < size; i ++){
        		TreeNode node = queue.poll();
        		max = Math.max(max, node.val);
        		if(node.left != null) queue.offer(node.left);
        		if(node.right != null) queue.offer(node.right);
        	}
        	res.add(max);
        }
        
        return res;
    }
	
	public static void main(String[] args) {
		TreeNode treeNode = new TreeNode(1);
		treeNode.left = new TreeNode(2);
		treeNode.right = new TreeNode(3);
		treeNode.left.left = new TreeNode(4);
		treeNode.left.right = new TreeNode(5);
		treeNode.right.right = new TreeNode(6);
		
		System.out.println(new Solution().largestValues(treeNode));		
	}
}