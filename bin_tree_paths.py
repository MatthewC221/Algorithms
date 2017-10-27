# Leetcode: https://leetcode.com/problems/binary-tree-paths/description/
# This was surprisingly difficult. Maybe just having an off day.
# Structure it so the strings are appended in one pass, as opposed to making lists then converting, etc.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        
        if not root: return []
        ret = []
        empty = ""
        self.traverse(root, empty, ret)
        return ret
    
    def traverse(self, root, cur, ret):
        
        if root.left is None and root.right is None: 
          ret.append(cur + str(root.val))
        if root.left is not None: 
          self.traverse(root.left, cur + str(root.val) + "->", ret)
        if root.right is not None: 
          self.traverse(root.right, cur + str(root.val) + "->", ret)
        
