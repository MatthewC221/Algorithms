# Leetcode: https://leetcode.com/problems/sum-root-to-leaf-numbers/description/
# Elegant solution, beats 80% (still can be better). I think DFS/BFS w/o recursion will improve on speed
# Recursion itself isn't very fast and there's not much you can do to optimise 'traverse'

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        return self.traverse(root, root.val)
        
    def traverse(self, root, cur_sum):
        
        if (root.left and root.right):
            return self.traverse(root.left, (cur_sum * 10) + root.left.val) + self.traverse(root.right, (cur_sum * 10) + root.right.val) 
        
        if (root.left):
            return self.traverse(root.left, (cur_sum * 10) + root.left.val) 
        
        if (root.right):
            return self.traverse(root.right, (cur_sum * 10) + root.right.val) 
        
        return cur_sum
