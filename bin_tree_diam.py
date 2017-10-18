# Leetcode: https://leetcode.com/problems/diameter-of-binary-tree/description/
# Slow as hell.. I think it's because of the constant recomputation of depth. We technically could merge
# maxDepth and depth into one function. This I believe will increase speeds greatly (it does, see commented)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        mx = 0
        return self.maxDepth(root, mx)
    
    def maxDepth(self, root, mx):
        
        if root is None: return mx
        left = self.depth(root.left)
        right = self.depth(root.right)

        # If max left = 1, max right = 5, total = 6 steps
        mx = max(mx, left + right)
        
        return max(self.maxDepth(root.left, mx), self.maxDepth(root.right, mx))
    
    def depth(self, root):
        
        if root is None: return 0
        return 1 + max(self.depth(root.left), self.depth(root.right))

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    mx = 0
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.depth(root)
        return self.mx
    
    def depth(self, root):
        
        if root is None: return 0
        left = self.depth(root.left)
        right = self.depth(root.right)

        # If max left = 1, max right = 5, total = 6 steps
        self.mx = max(self.mx, left + right)      
        return 1 + max(left, right)
    
    
"""
class Solution(object):
    mx = 0
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.depth(root)
        return self.mx
    
    def depth(self, root):
        
        if root is None: return 0
        left = self.depth(root.left)
        right = self.depth(root.right)

        # If max left = 1, max right = 5, total = 6 steps
        self.mx = max(self.mx, left + right)      
        return 1 + max(left, right)
"""
