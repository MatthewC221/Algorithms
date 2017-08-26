# Leetcode: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
# This was okay because I saw a similar question before (postorder and inorder), I got stuck before and saw a solution

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        
        if (not preorder or not inorder):
            return None
        
        root = TreeNode(preorder.pop(0))
        index = inorder.index(root.val)
        
        root.left = self.buildTree(preorder, inorder[:index])
        root.right = self.buildTree(preorder, inorder[index+1:])
        
        return root
