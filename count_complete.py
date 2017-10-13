# Leetcode: https://leetcode.com/problems/count-complete-tree-nodes/description/
# Definitely had the right technique, but found it difficult to properly execute the optimisation

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        # DFS to find depth (keep going left)
        
        L_height = R_height = 0
        L = R = root
        
        while L:
            L = L.left
            L_height += 1
        
        while R:
            R = R.right
            R_height += 1
            
        if (L_height == R_height): return pow(2, L_height) - 1
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
            
