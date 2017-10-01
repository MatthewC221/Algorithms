# Leetcode: https://leetcode.com/problems/delete-node-in-a-bst/description/
# I had forgotten how to delete a node (when there's right and left it's a bit more complex)
# Revise on how to do that first probably
  
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        
        # When deleting node, if leaf, just delete it. Otherwise replace it with the smallest of 
        # right subtree
        
        if not root: return None
        
        if (key < root.val):
            root.left = self.deleteNode(root.left, key)
        elif (key > root.val):
            root.right = self.deleteNode(root.right, key)
        else:
            if (not root.left):
                return root.right
            elif (not root.right):
                return root.left
            
            new_val = self.findMin(root.right)
            root.val = new_val
            root.right = self.deleteNode(root.right, root.val)
        
        return root
    
    def findMin(self, node):
        
        while (node.left):
            node = node.left
        
        return node.val
