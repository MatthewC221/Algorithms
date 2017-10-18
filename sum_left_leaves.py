# Leetcode: https://leetcode.com/problems/sum-of-left-leaves/description/
# Beats 90%, made a small miscalculation (in lines 28-30). Can't return on line 29 because there could still be more
# on the right subtree (this is a 2 step look ahead)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        # Left leaves, do DFS
        return self.DFS(root)
    
    def DFS(self, root):
        
        if not root: return 0
        
        cur = 0
        # The one case where we sum the value (left leaves only)
        if (root.left):
            if (root.left.left is None and root.left.right is None):
                cur = root.left.val
        
        return self.DFS(root.left) + self.DFS(root.right) + cur
