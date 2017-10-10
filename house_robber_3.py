# Leetcode: https://leetcode.com/problems/house-robber-iii/description/
# This problem was difficult, I did use lots of help from solutions, I think I had the right idea
# all along but wasn't entirely sure how to implement. The initial recursive solution (w/o dict) times out

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        # DP approach: max amount robbed in each subtree
        # Then the max will be (max of parent + grandchildren) vs (max of child) recursively
        H = {}
        return self.rob_saved(root, H)
    
    def rob_saved(self, root, H):

        if root is None: return 0
        if root in H: return H[root]
        
        tot = 0
        if root.left:
            tot += self.rob_saved(root.left.left, H) + self.rob_saved(root.left.right, H)
                
        if root.right:
            tot += self.rob_saved(root.right.left, H) + self.rob_saved(root.right.right, H)
        
        cur = max(tot + root.val, self.rob_saved(root.right, H) + self.rob_saved(root.left, H))
        H[root] = cur
        
        return cur
        
