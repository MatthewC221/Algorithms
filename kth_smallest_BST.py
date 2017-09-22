# Leetcode: https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/
# Once you know you can get the ascedning order of a tree using an inorder traversal it's easy
# Just need to draw it out a few times

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        
        # Inorder traversal will get you an ascending array
        
        if not root: return None
        
        cur = []
        self.inorder(root, cur)
        return cur[k - 1]
    
    def inorder(self, root, order):
        
        if (root == None):
            return None
        
        self.inorder(root.left, order)
        order.append(root.val)
        self.inorder(root.right, order)
