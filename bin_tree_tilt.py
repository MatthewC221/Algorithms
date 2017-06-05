# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# https://leetcode.com/problems/binary-tree-tilt/#/description
class Solution(object):
    
    total_sum = 0
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if (root == None):
            return 0
            
        self.total_sum = 0
        self.traversal(root)
        return self.total_sum
    
    # Traverses the tree (doesn't matter what order)
    def traversal(self, root):
    
        if (root == None):
            return 
        
        difference = abs(self.sum_tree(root.left) - self.sum_tree(root.right))
        self.total_sum += difference
        self.traversal(root.left)
        self.traversal(root.right)
    
    # Sums the subtree (including the root)
    def sum_tree(self, root):
        
        if (root == None):
            return 0
        
        if (root.left == None and root.right == None):
            return root.val
        
        if (root.left != None and root.right != None):
            return root.val + self.sum_tree(root.left) + self.sum_tree(root.right)
        elif (root.left != None):
            return root.val + self.sum_tree(root.left)
        elif (root.right != None):
            return root.val + self.sum_tree(root.right)
        
