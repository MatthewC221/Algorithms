# Leetcode: https://leetcode.com/problems/balanced-binary-tree/description/
# O(n^2) based on calculating height, can be O(n) with DFS (bottom-up approach), saving the heights

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# O(n^2) solution
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        return self.traverse(root)
    
    def traverse(self, root):
        
        if not root: return True
        
        if (abs(self.getHeight(root.left, 0) - self.getHeight(root.right, 0)) > 1):
            return False

        return self.traverse(root.left) and self.traverse(root.right)

    def getHeight(self, root, cur):
        
        if (not root):
            return cur
        
        return max(self.getHeight(root.left, cur + 1), self.getHeight(root.right, cur + 1))
