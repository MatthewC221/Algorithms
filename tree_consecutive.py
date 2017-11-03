# Leetcode: https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/description/
# DFS solution, could do a BFS too. Pretty straight forward if you use external variables such as mx here

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    mx = 1
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        
        self.DFS(root.left, root.val, 1)
        self.DFS(root.right, root.val, 1)
            
        return self.mx

    def DFS(self, root, prev, con):
        
        if not root: return 0

        if root.val == prev + 1: 
            con += 1
        else: 
            con = 1
        
        self.mx = max(self.mx, con)
        self.DFS(root.left, root.val, con)
        self.DFS(root.right, root.val, con)
