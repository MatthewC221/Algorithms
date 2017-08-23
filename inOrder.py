# Leetcode: https://leetcode.com/submissions/detail/115175620/
# Inorder traverse, not very difficult although I'm not too sure how to do iteratively right now.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        nodes = []
        if (root is None):
            return []
        self.traverse(root, nodes)
        return nodes
    
    def traverse(self, root, nodes):
        
        if (root.left):
            self.traverse(root.left, nodes)
        
        nodes.append(root.val)
        
        if (root.right):
            self.traverse(root.right, nodes)
        
